/*      Arduino-based Quantum Entangled Entropy Generator
 * Author: j. Campbell
 * 
 * Copyright (c) MuonRay Enterprises 2015
 * 
 */
int triggerPin = 13;
int hPin = A0;
int vPin = A1;
float H = 0;
float V = 0;
bool xtra = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(triggerPin, OUTPUT);
  Serial.begin(9600);

}

float angle() {
  H = analogRead(hPin);
  V = analogRead(vPin);
  float a = degrees(atan(V/H));
  return a;
}

int Random() {
  // Pulse the laser
  digitalWrite(triggerPin, HIGH);
  delay(3);
  digitalWrite(triggerPin, LOW);
  // Read the photodetectors
  H = analogRead(hPin);
  V = analogRead(vPin);
  // Determine random bit
  if(H>V) { // More photons in the H mode, return 0
    return 0;
  } if(H < V) { // More photons in the V mode, return 1
    return 1;
  } else { 
    /* due to entanglement, the same number of photons are in both modes however
        The randomness is in which mode will enter which beamsplitter - there is no way to know or influence which one. It is the perfect 50/50 coin toss as it were.
        the h and v modes are in a state of superposition until 1 is detected. 
        Even though we are not detecting single photons, we can run the function recursively until a random bit can be generated.
     */
    Random();
  }
}


void loop() {
  if(Serial.available()){
    char val = Serial.read();
    if(val == 'r') {
      Serial.print(Random());
    }
    if(val == 'a') {
      Serial.print(angle());
    }
  }
}
