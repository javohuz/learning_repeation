int redLEDPin=9; 
int yellowLEDPin=10;
int redOnTime=250;
int redOffTime=250; 
int yellowOnTime=250; 
int yellowOffTime=250; 
int greenLedpin=11,greenon=250,greenoff=250;
String redLEDsms="Red LEd is running :" ;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  String mw1="Hello" , mw2=" welcome to my Program " , mw3 ;
  mw3=mw1+mw2 ;
  Serial.println(mw3);
  pinMode(redLEDPin, OUTPUT);  // Tell Arduino that redLEDPin is an output pin
  pinMode(yellowLEDPin, OUTPUT);  //Tell Arduino that yellowLEDPin is an output pin
  pinMode(greenLedpin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

Serial.println(redLEDsms);
for (int j=1; j<=4; j=j+1) {   
  Serial.print("  running times:");
  Serial.println(j);
    digitalWrite(redLEDPin,HIGH); //Turn red LED on
    delay(redOnTime);             //Leave on for redOnTime
    digitalWrite(redLEDPin,LOW);  //Turn red LED off
    delay(redOffTime);
}
Serial.println(" ");
for (int h=1; h<=2; h=h+1) {
  digitalWrite(yellowLEDPin,HIGH); //Turn yellow LED on
  delay(yellowOnTime);             //Leave on for yellowOnTime
  digitalWrite(yellowLEDPin,LOW);  //Turn yellow LED off
  delay(yellowOffTime);            //Leave off for yellowOffTime
}
for (int g=4; g<=4; g+=1){
  digitalWrite(greenLedpin,HIGH);
  delay(greenon);
  digitalWrite(greenLedpin,LOW);
  delay(greenoff);
}

}
