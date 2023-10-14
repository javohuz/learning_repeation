int age ;
float tall ;
String Name ;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600) ;

}

void loop() {
  // put your main code here, to run repeatedly:

Serial.println("Hello , What is your name ? ");
while (Serial.available()==0){ }
Name = Serial.readString() ;

Serial.println("How old are you ");
while (Serial.available()==0 ) { }
age =  Serial.parseInt() ;

Serial.print("How tall are you  ");
while (Serial.available()==0 ) { }
tall = Serial.parseFloat() ;

Serial.println("Hello ");
Serial.print(Name);
Serial.print(", you are ");
Serial.print(age);
Serial.print(", and ");
Serial.println(tall);






}
