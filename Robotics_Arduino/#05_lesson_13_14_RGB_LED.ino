int redPin=11;  //set red LED pin to 11
int greenPin=10; //set green LED pin to 10
int bluePin=6; //set blue LED pin to 6
int brightness=255; //Set brightness to 75
int forred=235  , forgreen=52 , forblue=219  ;
int colorChoice; //Will hold users input of color choice

void setup() {
  // put your setup code here, to run once:

Serial.begin(9600); //Turn on Serial port
pinMode(redPin, OUTPUT); //Set redPin to be an output
pinMode(greenPin, OUTPUT); //Set greenPin to be an output
pinMode(bluePin, OUTPUT); //set bluePin to be an output

}

void loop() {
  if (colorChoice!=1 || colorChoice!=2 || colorChoice != 3 || colorChoice != 4 || colorChoice != 5  ) {

  Serial.println("What color would you like the LED? "); //Prompt user for color
  Serial.println("red=1");
  Serial.println("green=2");
  Serial.println("blue=3");
  Serial.println("pink=4");
  Serial.println("mixed=5");
  while (Serial.available()==0) { }   //Wait for input
  colorChoice = Serial.parseInt();
  }
  
  if (colorChoice==1) {
  
  analogWrite(redPin, brightness); //turn on red pin
  analogWrite(greenPin, 0); //turn off green pin
  analogWrite(bluePin, 0); //write off blue pin
}

  if (colorChoice==3) {
  
  analogWrite(redPin, 0); //turn off red pin
  analogWrite(greenPin, 0); //turn off green pin
  analogWrite(bluePin, brightness); //write on blue pin
}

  if (colorChoice==2) {
  
  analogWrite(redPin, 0); //turn off red pin
  analogWrite(greenPin, brightness); //turn on green pin
  analogWrite(bluePin, 0); //write off blue pin
}

 if (colorChoice==4) {
  
analogWrite(redPin,forred);
analogWrite(greenPin,forgreen);
analogWrite(bluePin,forblue);
 }

 if (colorChoice==5 ){
  while (Serial.available()==1){
  analogWrite(redPin, brightness); //turn on red pin
  delay(500);

  digitalWrite(redPin,LOW);
  analogWrite(greenPin, brightness); //turn on green pin
  delay(500);
 
  digitalWrite(greenPin,LOW);
  analogWrite(bluePin, brightness); //write on blue pin
  delay(500);

  digitalWrite(bluePin,LOW);
  analogWrite(redPin,forred);
  analogWrite(greenPin,forgreen);
  analogWrite(bluePin,forblue);
  delay(500);

  digitalWrite(redPin,LOW);
  digitalWrite(greenPin,LOW);
  digitalWrite(bluePin,LOW);

  }
  colorChoice = Serial.parseInt();

  }
 
 
  if (colorChoice!=1 || colorChoice!=2 || colorChoice != 3 || colorChoice != 4 || colorChoice != 5  ) {
    Serial.println("That is not a valid color choice, please try again");
    Serial.println("");
  }

  
}
