#include <LiquidCrystal.h>
LiquidCrystal lcd(7, 6, 2, 3, 4, 5);

int led = 8;
const int currentPin = A0;
int sensitivity = 66;
int adcValue= 0;
int offsetVoltage = 2500;
double adcVoltage = 0;
double currentValue = 0;
//double watt = 0;
double fullday = 0;

void setup() {
  pinMode(led, OUTPUT);
  lcd.begin(16,2);
}

void loop() {
  digitalWrite(led,HIGH);

  adcValue = analogRead(currentPin);
  adcVoltage = (adcValue / 1024.0) * 5000;
  currentValue = ((adcVoltage - offsetVoltage) / sensitivity);
  double watt = currentValue*220;
  fullday = fullday+watt;
  if(fullday >= 1500){
    fullday = 0;
  }
  
  lcd.setCursor(8,1);
  lcd.print(fullday);
  lcd.print("w");
  delay(500);
}
