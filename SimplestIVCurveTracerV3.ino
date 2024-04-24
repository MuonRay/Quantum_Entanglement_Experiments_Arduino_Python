//Arduino Code to measure I-V curve on an LED (or Superconducting BSCCO Intrinsic Josephson Junction to measure Shapiro Staircase)

float U = 4980; // voltage between GND and arduino VCC in mV = total voltage

float U1=0; // 1 probe

float U2=0; // 2 probe

float Ur=0; // voltage drop on shunt resistor

float Ul=0; // voltage drop on led

float I =0; // total current in circuit

float R_drop=100; // set resistance of shunt resistor

void setup()

{

Serial.begin(9600);

pinMode(11,OUTPUT);

pinMode(3,OUTPUT);

pinMode(A0, INPUT);

pinMode(A4, INPUT);

TCCR2A = B10100011; //fast PWM on both A and B
TCCR2B = B00000001; //no prescale on timer2

}


void loop() {
  
  //if(Serial.available()){
    byte nrep=6.283;

    for(byte i=0; i<nrep; i++){
      
      OCR2A=1023*i;
      OCR2B=1023*i;
      
      U1 = float(analogRead(A0))/1023*U; // get voltage between GND and A0 in milliVolts

      U2 = float(analogRead(A4))/1023*U; // get voltage between GND and A4 in milliVolts

      Ur=U2-U1; // drop voltage on shunt resistor

      I=Ur/R_drop*1000; // total current in microAmps

      Ul=U-U2; // voltage drop on led

        //Serial.write(255);
        //Serial.write(U1/256); // Voltage Drop on Shunt Resistor
        //Serial.write(U1%256);
        //Serial.write(" , ");
        //Serial.write(U2/256);
        //Serial.write(U2%256);
      Serial.print(Ul); // Voltage Drop on LED
      Serial.print(" , ");
      Serial.println(I); //total Current in microAmps
      }
      
}
