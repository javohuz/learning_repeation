int ledN=13;
int waitTime=1000;

void setup() {
  // put your setup code here, to run once:
  pinMode(ledN,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ledN,HIGH);
  delay(waitTime);
  digitalWrite(ledN,LOW);
  delay(100);
}
