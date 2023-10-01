int red = 3 , green=5 , blue=9 ;
int forred=235  , forgreen=52 , forblue=219  ;
void setup() {
  // put your setup code here, to run once:

  pinMode(red , OUTPUT );
  pinMode(green , OUTPUT );
  pinMode(blue , OUTPUT );
  Serial.begin(9600);


}

void loop() {
  // put your main code here, to run repeatedly:

analogWrite(red,forred);
analogWrite(green,forgreen);
analogWrite(blue,forblue);


}
