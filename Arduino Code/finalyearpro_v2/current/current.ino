#include <LiquidCrystal.h>
LiquidCrystal lcd(7, 6, 2, 3, 4, 5);

const int currentPin = A0;
int sensitivity = 66;
int adcValue= 0;
int offsetVoltage = 2500;
double adcVoltage = 0;
double currentValue = 0;
//double watt = 0;
double fullday = 0;

int light = 8;
int fan = 9;
char sms;

void setup() {
  pinMode(led, OUTPUT);
  lcd.begin(16,2);

  Serial.begin(9600);
  pinMode(light,OUTPUT);
  pinMode(fan,OUTPUT);
}

void loop() {

  adcValue = analogRead(currentPin);
  adcVoltage = (adcValue / 1024.0) * 5000;
  currentValue = ((adcVoltage - offsetVoltage) / sensitivity);
  double watt = currentValue*220;
  fullday = fullday+watt;
  if(fullday >= 1500){
    fullday = 0;

      if(Serial.available()!=0){
        sms = Serial.read();
        }
      if(sms=='1'){
        digitalWrite(light,HIGH);
        }
      if(sms=='2'){
        digitalWrite(light,LOW);
        }
      if(sms=='3'){
        digitalWrite(fan,HIGH);
        }
      if(sms=='4'){
        digitalWrite(fan,LOW);
        }
  }
  
  lcd.setCursor(8,1);
  lcd.print(fullday);
  lcd.print("w");
  delay(500);
}
