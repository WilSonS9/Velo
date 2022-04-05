#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <DNSServer.h>            //Local DNS Server used for redirecting all requests to the configuration portal
#include <ESP8266WebServer.h>     //Local WebServer used to serve the configuration portal
#include <Wire.h>
#include <WiFiManager.h>

// Host URL for the API, paste your AWS URL
const String host = "8s6uuofzza.execute-api.us-east-1.amazonaws.com";

const char *fingerprint = "15:67:15:46:21:35:29:05:E5:16:E9:0B:31:15:1F:42:3E:06:F6:D9";

const int a = A0;
float inpValue;
float v;
int k = 2; // From the ration of the voltage division

bool isLoggedIn = false;
String loggedInUser = "0";

// HTTP response object
struct Response
{
  // HTTP status code
  int statusCode = -1;
  // Response message
  String payload = "";
};

// HTTPS client
WiFiClientSecure client;

// Important values from database
bool isRegistered = false;
int updateInterval = 1800;

Response makeRequest(String type, String uri, String query, String payload)
{
  // Connect to API host
  if(client.connect(host, 443))
  {
      Serial.println(type   +"   "+host + uri + "?" + query + " HTTP/1.1");
    // Serial.println(payload);
    // // Writing HTTP request
    client.println(type + uri + " HTTP/1.1");
    client.println("Host: " + host);
    client.println("Connection: close");
    
    // If there's a payload, include content-length
    if(payload.length() > 0)
    {
      client.println("Content-Type: application/json");
      client.print("Content-Length: ");
      client.println(payload.length());
      client.println();
      client.println(payload);
      client.println();
    }
    else
    {
      client.println();
    }

    // An empty println means the end of the request

    // Placeholder for response data
    String line;
    // Response object
    Response res;
    // While connection is alive
    while(client.connected())
    {
      // Read one line
      line = client.readStringUntil('\n');

      // Print response to serial monitor
      // Serial.println(line);
      
      // A line starting with HTTP contains the status code
      if(line.startsWith("HTTP") && res.statusCode < 0)
      {
        // Take the appropriate substring and convert to an integer
        res.statusCode = line.substring(9, 12).toInt();
      }
      
      // If the line starts with a hard bracket we have our response payload
      if(line.startsWith("["))
      {
        // End the connection
        client.stop();
        // Set the payload in our response object
        res.payload = line;
      }
    }

    // Return our response
    return res;
  }
  else
  {
    // Connection failed
    Serial.println("Misslyckades med att ansluta till AWS.");
    Response res;
    res.statusCode = -1;
    res.payload = "no connection";
    // Return a "no connection" response
    return res;
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

   delay(1000);

  Serial.print("Ansluter till ");
  Serial.print(".");
  WiFiManager wifiManager;
  wifiManager.autoConnect("ABBgym_2.4");

  Serial.print("Klar\nLokal IP-adress: ");
  Serial.println(WiFi.localIP());

  // Sets the fingerprint for SSL encrypted connection
  client.setFingerprint(fingerprint);
}

void getLogin() {
  Response getRes = makeRequest("GET ", "/isLoggedIn", "" , "");
  Serial.println(getRes.statusCode);
  Serial.println(getRes.payload);
  isLoggedIn = getRes.payload[1] == 't';
  bool firstFound = false;
  bool secondFound = false;
  loggedInUser = "";

  for (int i = 0; i < getRes.payload.length(); i++) {
    if (firstFound)
    {
      secondFound = getRes.payload[i] == '\"';
      if (secondFound) {
        i = getRes.payload.length();
      }
      else {
        loggedInUser += getRes.payload[i];
      }
    }
    else {
      firstFound = getRes.payload[i] == '\"';
    }
  }

  Serial.println(isLoggedIn);
  Serial.println(loggedInUser);
}

void postPowerEnergy(float power, float energy, String ID) {
  String query = "BicycleID=" + ID + "&energy=" + String(energy) + "&power=" + String(power);
  Serial.println(query);
  makeRequest("POST ", "/addPowerEnergy", query, "{\"test\": \"aaaa\"}");  
}

void onLogin() {
  getLogin();
  if (isLoggedIn) {
    // TODO: Measure and post power
    float energy = 1.2;
    float power = 4.3;
    postPowerEnergy(power, energy, loggedInUser);
    Serial.println(loggedInUser);
    Serial.println("Posted power, waiting 5 seconds...");
    delay(5000);
  }
  else {
    Serial.println("No one logged in, waiting 5 seconds...");
    delay(5000);
  }
}



void loop() {

  // put your main code here, to run repeatedly:
  onLogin();
}

void getVoltage() {
  inpValue = analogRead (a); // Analog Values 0 to 1023
  v = inpValue / 1023;
  v *= 3.3;
  v *= k;
  Serial.print (inpValue);
  Serial.print(" ");
  Serial.println(v);
 }
