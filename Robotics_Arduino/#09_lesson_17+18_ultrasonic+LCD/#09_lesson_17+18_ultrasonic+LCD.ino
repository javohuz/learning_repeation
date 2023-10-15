#include <LiquidCrystal.h>

LiquidCrystal LCD(12, 11, 6, 5, 4, 3);
int trigpin=9 , echopin=8 ,distance ; 
float time ; 

void setup() {

LCD.begin(16,2);
LCD.setCursor(0,0);
LCD.print("Distance is");
pinMode(trigpin , OUTPUT);
pinMode(echopin , INPUT);
}

void loop() {

digitalWrite(trigpin , LOW);
delayMicroseconds(2000);
digitalWrite(trigpin, HIGH);
delayMicroseconds(10);
digitalWrite(trigpin, LOW);

time = pulseIn(echopin,HIGH);
distance = time*343/20000;

LCD.setCursor(0,1);
LCD.print(distance);
LCD.print(" sm");

}
