/*************************************************************

quantum node rho for use with BLYNK IOT Phone App
written by John Campbell

Now with some new lines in the void loop for time complexity measures
which print out in the serial monitor 
 *************************************************************/

// Template ID, Device Name and Auth Token are provided by the Blynk.Cloud
// See the Device Info tab, or Template settings
#define BLYNK_PRINT Serial

#include <SPI.h>
#include <Ethernet.h>
#include <BlynkSimpleEthernet.h>

#define BLYNK_TEMPLATE_ID "TMPLve3FHVE9"
#define BLYNK_DEVICE_NAME "Quantum Node Rho "
#define BLYNK_AUTH_TOKEN "enterauthkeyhere"

#define W5100_CS  10
#define SDCARD_CS 4


char auth[] = BLYNK_AUTH_TOKEN;


int triggerPin = 2;
int hPin = A0;
int vPin = A1;
float H = 0;
float V = 0;
bool xtra = 0;
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

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(triggerPin, OUTPUT);
  Blynk.begin(auth, "blynk.cloud", 80);
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
  //now with time complexity measures
  // 1. Store the start time
  unsigned long timeBegin = micros();
  // 2. Execute main action
  Blynk.run();
  timer.run(); 
  // 3. Store the end time
  unsigned long timeEnd = micros();
  // 4. Compute duration
  unsigned long duration = timeEnd - timeBegin;
  double averageDuration = duration / 1000;
  Serial.println(averageDuration);
}
