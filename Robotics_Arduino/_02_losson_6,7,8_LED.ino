int redpin=3 , redon =250 , redoff = 250 , redtimes ;
int yellowpin=9 , yellowon = 250 , yellowoff=250 , yellowtimes ;

void setup() {
  // put your setup code here, to run once:
pinMode(redpin,OUTPUT);
pinMode(yellowpin,OUTPUT);
Serial.begin(9600);

Serial.println("Enter red LED running times ");
while(Serial.available()==0) { }
redtimes = Serial.parseInt();

Serial.println("Enter yellow LED running times ");
while(Serial.available()==1) { }
yellowtimes = Serial.parseInt();
}

void loop() {


Serial.println("Red LED is Running : ");
int r=1;
while (r<=redtimes){
// for (int j=1; j<=redtimes ; j+=1){
  Serial.print("  Running times : ");
  Serial.println(r);
 // digitalWrite(redpin,HIGH); // digital raqamli , HIGH = 5V
  analogWrite(redpin, 127); // anolog uhshashlik , x=y/51 , x we need value , y we gived value , 255=5v agar y>255 qaytadan ketadi yani y=51=306  , y=0=256
  delay(redon);
  digitalWrite(redpin,LOW);
  delay(redoff);
  r+=1 ;
}
Serial.println(' ');
Serial.println("Yellow LED is Running ");
int y=1 ;
while(y<=yellowtimes){
  Serial.print("  Running times : ");
  Serial.println(y);
  //digitalWrite(yellowpin,HIGH);
  analogWrite(yellowpin,255);
  delay(yellowon);
  digitalWrite(yellowpin,LOW);
  delay(yellowoff);
  y+=1;
}
Serial.println(' ');

}
