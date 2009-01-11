// Home Automation Project
// Arduino Kernel v0.0

#include <SoftwareSerial.h>

#define rxPin 0
#define txPin 1

#include "WProgram.h"
void setup();
void loop();
void setDigital(int pinNum, int pinVal);
SoftwareSerial mySerial = SoftwareSerial(rxPin, txPin);
int KERNEL_VERSION = 0.1;

void setup() {
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  
  mySerial.begin(9600);
}

void loop() {
  mySerial.print("Mode: ");
  char mode = mySerial.read();

// ------------------ SET MODE ------------------
  if(mode == 'S'){
    //Set Command - Digital Support Only
    mySerial.print("Set Digital: ");
    int digital = ( int(mySerial.read()) - 48 );
    mySerial.print(digital);
    
    if(digital == 1){
      //Digital Pins
      mySerial.print(" PinNum: ");
      char pinTens = mySerial.read();
      char pinOnes = mySerial.read();
      int pinNum = (int(pinOnes) - 48) + ( (int(pinTens) - 48) * 10 );
      mySerial.print(pinNum);
      mySerial.print(" Value: ");
    
      int pinVal = int(mySerial.read() - 48);
      mySerial.print(pinVal);
    
      setDigital(pinNum, pinVal);
      mySerial.println(" - OK");
    }else if(digital == 0){
      //Analog Pins
      mySerial.println(" Analog pins unsupported.");
    }else{
      //Invalid Input
      mySerial.println("Invalid Input");
    }

// ------------------ READ MODE ------------------
  }else if(mode == 'R'){
    //Read Command - Digital Support Only
    mySerial.print("Read Digital: ");
    int digital = ( int(mySerial.read()) - 48 );
    mySerial.print(digital);
    
    if(digital == 1){
      //Digital Pins
      mySerial.print(" PinNum: ");
      char pinTens = mySerial.read();
      char pinOnes = mySerial.read();
      int pinNum = (int(pinOnes) -48) + ( (int(pinTens) - 48) * 10 );
      mySerial.print(pinNum);
    
      int pinVal = digitalRead(pinNum);
      mySerial.print(" Value: ");
      mySerial.print(pinVal);
      mySerial.println(" - OK");
    }else if(digital == 0){
      //Analog Pins
      mySerial.print(" PinNum: ");
      char pinOnes = mySerial.read();
      int pinNum = (int(pinOnes) -48);
      mySerial.print(pinNum);
    
      int pinVal = analogRead(pinNum);
      mySerial.print(" Value: ");
      mySerial.print(pinVal);
      mySerial.println(" - OK");
    }else{
      //Invalid Input
      mySerial.println(" Invalid Input");
    }
  }else if(mode == 'V'){
    mySerial.print(" Information Kernel: ");
    mySerial.print(KERNEL_VERSION); 
  }else{
    mySerial.println("Invalid Input");
  }
}

void setDigital(int pinNum, int pinVal){
  if(pinVal == 1){
    digitalWrite(pinNum, HIGH);
  }else if (pinVal == 0){
    digitalWrite(pinNum, LOW);
  }
}

int main(void)
{
	init();

	setup();
    
	for (;;)
		loop();
        
	return 0;
}

