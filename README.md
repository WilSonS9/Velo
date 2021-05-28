# Velo
## About
Velo is the Senior Year Project of three students at ABB Industrial High School in Västerås, Sweden. The goal is to create a bicycle that can generate electricity to power household applications such as a phone charger or a television. We also aim to create a cross-platform application where you can monitor how much electricity you are generating and other interesting data points. The main focus of this repository is to develop and document the application.
## How?
The applicatino is built in Vue, more specifically with the Vue framework Vuetify. To enable cross-platform usage, we have also integrated Cordova, which allows us to build for browsers, iOS and Android.
## How to run
To serve for the desired platform, simply run the command `npm run cordova-serve-*platform*`, where the platform is either `browser`, `ios` or `android`. If you choose `ios` or `android`, Cordova will open an emulator to run in your browser.
