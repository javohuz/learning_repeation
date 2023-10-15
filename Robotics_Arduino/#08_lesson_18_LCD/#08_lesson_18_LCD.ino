#include <LiquidCrystal.h>
LiquidCrystal LCD(11 , 10, 9 , 8 , 7 , 6 ) ;
void setup() {
  // put your setup code here, to run once:
LCD.begin(16,2);
LCD.setCursor(0,0);
LCD.print("TIMER ") ;
}

void loop() {
  // put your main code here, to run repeatedly:
for (int i=1 ; i <=10 ; i+=1 ) {
  LCD.setCursor(0,1);
  LCD.print(i);
  LCD.print(" Seconds");  
  delay(1000);
  }

for (int i=10 ; i >=0 ; i-=1 ) {
  LCD.setCursor(0,1);
  LCD.print(i);
  LCD.print(" Seconds");  
  delay(1000);
  }
}
