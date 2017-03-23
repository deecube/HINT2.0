//define analog pin 0 as input of moisture sensor
int moistureSensor = A0;

void setup() {
  // put your setup code here, to run once:
  //define moisture pin as input
pinMode(moistureSensor, INPUT); 
}

void loop() {
  // put your main code here, to run repeatedly:
  //reading the moisture value in 10bit code and converting to %
float moistureValue = analogRead(moistureSensor);
float moisturePercent = ((1023-moistureValue)/1023)*100;
//printing moisture content on serial window
Serial.print("Moisture: ");
Serial.print(moisturePercent);
}
