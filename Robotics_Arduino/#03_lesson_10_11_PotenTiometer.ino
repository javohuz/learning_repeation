int potpin=A0 , outpin=9 ;
float value ;
void setup() {
  // put your setup code here, to run once:
pinMode(potpin,INPUT);
Serial.begin(9600);
digitalWrite(outpin,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

value= analogRead(potpin);
Serial.println(value*5/1023);
analogWrite(outpin, value*255/1023 );

}
