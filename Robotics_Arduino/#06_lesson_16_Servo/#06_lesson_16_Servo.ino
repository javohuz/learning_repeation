#include <Servo.h>
int potpin=A0 ;
int outpin=9 , pos=0 , wait=25 , volue ;
Servo myservo ;


void setup() {

Serial.begin(9600);
myservo.attach(outpin);
pinMode(potpin,INPUT);
}

void loop() {

 // Serial.println("Servo qayerga borishini hohlaysiz gradus ");
 // while (Serial.available()==0){ }
 // pos=Serial.parseInt() ;
 // myservo.write(pos);

 // while ( pos<=180 ) {
 //   pos+=1 ;
  //  myservo.write(pos);
  //  delay(wait);
 // }
 //   while ( pos>=0 ) {
 //   pos-=1 ;
  //  myservo.write(pos);
  //  delay(wait);
 // }

 volue=analogRead(potpin);
 pos=volue/6 ;
 Serial.println(pos);
 myservo.write(pos);
  
} 
