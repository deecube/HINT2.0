//define analog pin 0 as input of moisture sensor
int moistureSensor = A0;
/*
1 LED - too dry
2 LED - comfort zone
3 LED - comfort zone
4 LED - comfort zone
5 LED - too moist
*/

#include <dht.h>
dht DHT;
#define DHT11_PIN 7

//light LEDs to indicate water level
int led1 = 2;
int led2 = 3;
int led3 = 4;
int led4 = 5;
int led5 = 6;
void setup() {
  // put your setup code here, to run once:
  //define moisture pin as input and actuators as outputs
Serial.begin(9600);  
pinMode(moistureSensor, INPUT); 
pinMode(led1, OUTPUT);
pinMode(led2, OUTPUT);
pinMode(led3, OUTPUT);
pinMode(led4, OUTPUT);
pinMode(led5, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //reading the moisture value in 10bit code and converting to %
float moistureValue = analogRead(moistureSensor);
float moisturePercent = ((1023-moistureValue)/1023)*100;
//reading temperature and humidity values
float temperature,humidity;
int chk = DHT.read11(DHT11_PIN);
humidity = DHT.humidity;
temperature = DHT.temperature;
//printing moisture content, temperature and humidity on serial window
Serial.print("Moisture: ");
  Serial.print(moisturePercent);
  Serial.print(" %");
  Serial.print("\t");
  Serial.print("H: ");
  Serial.print(humidity);
  Serial.print(" %");
  Serial.print("\t");
  Serial.print("T: ");
  Serial.print(temperature);
  Serial.println(" ºC");
//controlling LEDs based on moisture level of soil

if (moistureValue >= 820){
    digitalWrite(led1,HIGH);
    digitalWrite(led2,LOW);
    digitalWrite(led3,LOW);
    digitalWrite(led4,LOW);
    digitalWrite(led5,LOW);
   }
  else if(moistureValue >=720 && moistureValue <820){
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    digitalWrite(led3,LOW);
    digitalWrite(led4,LOW);
    digitalWrite(led5,LOW);
  }
  else if(moistureValue >=620 && moistureValue <720){
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    digitalWrite(led3,HIGH);
    digitalWrite(led4,LOW);
    digitalWrite(led5,LOW);
  }
  else if(moistureValue >=520 && moistureValue <620){
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    digitalWrite(led3,HIGH);
    digitalWrite(led4,HIGH);
    digitalWrite(led5,LOW);
  }
  else if(moistureValue <520){
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    digitalWrite(led3,HIGH);
    digitalWrite(led4,HIGH);
    digitalWrite(led5,HIGH);
   }
 delay(2000); 
}
