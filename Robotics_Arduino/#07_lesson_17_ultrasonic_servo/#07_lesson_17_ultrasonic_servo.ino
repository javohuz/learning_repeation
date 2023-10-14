#include <Servo.h>

int trigpin=13 , echopin=11  , v=340 , servopin=9 ;
float s , t ;
Servo myservo ;

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(trigpin , OUTPUT);
pinMode(echopin,INPUT);
myservo.attach(servopin);
}

void loop() {
  // put your main code here, to run repeatedly:

digitalWrite(trigpin,LOW );
delayMicroseconds(2000);
digitalWrite(trigpin , HIGH);
delayMicroseconds(10);
digitalWrite(trigpin,LOW );

t=pulseIn(echopin , HIGH); // microsecond
s=(t*v)/20000; // s => on sm 
Serial.print(s);
Serial.println(" sm");


if (s<=7 and s>=1) {
  myservo.write(180);
}
else {
  myservo.write(0);
}
}
