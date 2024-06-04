/*************************************************************

  This is a prototype of sending a command to receiving some quantum RNG by email.
 *************************************************************/

// Template ID, Device Name and Auth Token are provided by the Blynk.Cloud
// See the Device Info tab, or Template settings
#define BLYNK_PRINT Serial

#include <SPI.h>
#include <Ethernet.h>
#include <BlynkSimpleEthernet.h>

#define BLYNK_TEMPLATE_ID "TMPLve3FHVE9"
#define BLYNK_DEVICE_NAME "Quantum Node Rho "
#define BLYNK_AUTH_TOKEN "authkey"

#define W5100_CS  10
#define SDCARD_CS 4


char auth[] = BLYNK_AUTH_TOKEN;


int triggerPin = 2;
int hPin = A0;
int vPin = A1;
float H = 0;
float V = 0;
int x;
int y;
int z;

BlynkTimer timer;

BLYNK_WRITE(V0)
{
  x = param.asInt();
}

BLYNK_WRITE(V2)
{
  y = param.asInt();
}

BLYNK_WRITE(V4)
{
  z = param.asInt();
}


//send data by email
void emailOnButtonPress()
{
  // *** WARNING: You are limited to send ONLY ONE E-MAIL PER 5 SECONDS! ***

  // Let's send an e-mail when you press the button
  // connected to digital pin 2 on your Arduino

  int isButtonPressed = !digitalRead(2); // Invert state, since button is "Active LOW"

  if (isButtonPressed) // You can write any condition to trigger e-mail sending
  {
    Serial.println("Button is pressed."); // This can be seen in the Serial Monitor

    H++;
    V++;

    String body = String("You pushed the button ") + H + V + " H and V Values";

    Blynk.email("your_email@mail.com", "Subject: Button Logger", body);

    // Or, if you want to use the email specified in the App (like for App Export):
    //Blynk.email("Subject: Button Logger", "You just pushed the button...");
  }
}





void setup()
{
  Serial.begin(9600);
  pinMode(SDCARD_CS, OUTPUT);
  digitalWrite(SDCARD_CS, HIGH); // Deselect the SD card

  pinMode(13, OUTPUT);
  pinMode(triggerPin, OUTPUT);
  Blynk.begin(auth, "blynk.cloud", 80);
  // Send e-mail when your hardware gets connected to Blynk Server
  // Just put the recepient's "e-mail address", "Subject" and the "message body"
  // e.g. to announce activation of Quantum Nodes Rho and Sigma, Mu and Nu in the network
  Blynk.email("ektopyrotic@gmail.com", "Node Rho", "Quantum Node Rho is online.");
  // Setting the button
  pinMode(2, INPUT_PULLUP);
  // Attach pin 2 interrupt to our handler
  attachInterrupt(digitalPinToInterrupt(2), emailOnButtonPress, CHANGE);

  timer.setInterval(0L, quantum);
}

float angle() {
  float a = degrees(atan(V / H));
  return a;
}

void HGate() {
  digitalWrite(triggerPin, HIGH);
  digitalWrite(triggerPin, LOW);
  H = analogRead(hPin);
  V = analogRead(vPin);
}

int Rand() {
  HGate();
  if (H > V) {
    return 0;
  } if (H < V) {
    return 1;
  } else {
    Rand();
  }
}
 

void quantum() {
  char val = Serial.read();
  if (z == 1) {
    Serial.print("\nH: ");
    Serial.print(H);
    Blynk.virtualWrite(V5, H);
    Serial.print("\nV: ");
    Serial.print(V);
    Blynk.virtualWrite(V6, V);
    Serial.print('\n');
  }
  if (x == 1) {
    HGate();
    Blynk.virtualWrite(V1, angle());
  }
  if (y == 1) {
    Blynk.virtualWrite(V3, Rand());
  }
  if (val == 't') {
    Serial.print("Success!\n");
  }
  if (val == 'v') {
    Serial.print("Version 1.1\n");
  }
}

void loop()
{
  Blynk.run();
  timer.run();
}
