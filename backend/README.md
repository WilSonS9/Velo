# Velo API
URL för alla requests: `https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/`

Alla requests använder sig av Query String Parameters, inga request bodies, authentication eller authorization behövs
## Endpoints
Här är alla endpoints

---

### `/getLatestPower`
#### Beskrivning
Hämtar all power och energy för den nuvarande (senaste) sessionen för en viss användare

Power är effekten vid en viss tidpunkt, Energy är totala mängden energi som producerats under sessionen

Returnerar på formen `[Power, Energy]`
#### Argument
- `BicycleId`: ID för önskade användaren [string]

#### Exempel
Request: `GET https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/getLatestPower?BicycleID=1`

Response: `[["2", "2"], ["4.3", "4.3"]]` (Power första, Energy andra)

---

### `/getIt`
#### Beskrivning
Hämtar totala energin producerad av alla Velo-användare

Returnerar ett flyttal
#### Argument
Inga argument

#### Exempel
Request: `GET https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/getIt`

Response: `"34.6"`

---

### `/getItUser`
#### Beskrivning
Hämtar totala energin producerad av en viss Velo-användare

Returnerar ett flyttal
#### Argument
- `BicycleID`: ID för önskad användare [string]

#### Exempel
Request: `GET https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/getItUser?BicycleID=1`

Response: `"34.6"`

---

### `/isLoggedIn`
#### Beskrivning
Kollar om någon användare är inloggad och i sådana fall vilken osm är inloggad

Returnerar på formen `[isLoggedIn, BicycleID]` där `isLoggedIn` är `true` om någon användare är inloggad, annars `false`

Är `isLoggedIn` `false` är `BicycleID` `"0"`
#### Argument
Inga argument

#### Exempel
Request: `GET https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/isLoggedIn`

Response: `[false, "0"]`

---

### `/onLogIn`
#### Beskrivning
POST request som körs för att logga in någon

Returnerar `"Login Failed"` om det inte gick, annars `["User logged in!", BicycleID]` där `BicycleID` är användarens ID
#### Argument
- `username`: Användarens användarnamn [string]
- `pass`: Användarens lösenord [string] (OBS! Lambda kör en direct comparison av det angivna lösenordet och det lagrade lösenordet, så om användarens lösenord är hashat, se till att hasha inputen även här)

#### Exempel
Request: `POST https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/onLogIn?username=user&pass=pass`

Response: `["User logged in!", "1"]`

---

### `/onLogOut`
#### Beskrivning
POST request som körs för att logga ut den nuvarande inloggade användaren

Returnerar `"User logged out!"` om användaren kunde loggas ut, annars om ingen användare var inloggad returneras `"No user logged in!"`
#### Argument
Inga argument (den nuvarande inloggade användaren lagras alltid i databasen då det bara kan vara en användare online vid en given tidpunkt)

#### Exempel
Request: `POST https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/onLogOut`

Response: `"User logged out!"`

---

### `/addUser`
#### Beskrivning
POST request som körs för att skapa en ny användare

Returnerar `"User added!"` om det lyckas
#### Argument
- `username`: Användarens användarnamn [string]
- `pass`: Användarens lösenord [string] (OBS! Inputen här läggs direkt in i databasen utan att hashas, se till att vara konsekvent med hashning med `/onLogIn`, det är detta värde som direkt jämförs med i den requesten)

#### Exempel
Request: `POST https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/addUser?username=pogUser&pass=superPass`

Response: `"User added!"`

---

### `/addPowerEnergy`
#### Beskrivning
POST request som lägger till senaste effekten och energin i den senaste sessionen för en viss användare (ska köras från mikrokontrollern)

Returnerar `"Power and energy added!"` om det lyckas
#### Argument
- `BicycleID`: Användarens ID [string]
- `power`: Effekten som ska läggas in [float] (momentan effekt)
- `energy`: Energin som ska läggas in [float] (kom ihåg att detta är den senaste *totala* energin för sessionen, inte sedan senaste mätning)

#### Exempel
Request: `POST https://8s6uuofzza.execute-api.us-east-1.amazonaws.com/addPowerEnergy?BicycleID=1&energy=4.3&power=2`

Response: `"Power and energy added!"`
