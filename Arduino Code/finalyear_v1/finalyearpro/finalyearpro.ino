int light = 8;
int fan = 9;
char sms;
int lm = A0;

//testing power supply
int red = 4;
int green = 5;

void setup() {
  Serial.begin(9600);
  pinMode(red,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(light,OUTPUT);
  pinMode(fan,OUTPUT);
  pinMode(lm,INPUT);
}

void loop() {
  //testing power supply
  digitalWrite(red,HIGH);
  digitalWrite(green,HIGH);

  float value = analogRead(A0);
  float milivolt = (value*5000)/1024;
  int temp = milivolt/10;
  Serial.print(temp);
  Serial.print(" ");
  delay(1000);
  
  if(Serial.available()!=0){
    sms = Serial.read();
  }
   if(sms=='1'){
    digitalWrite(light,HIGH);
   }
   if(sms=='2'){
    digitalWrite(light,LOW);
   }
   if(sms=='3' && temp<30){
    digitalWrite(fan,HIGH);
   }
   if(sms=='4'){
    digitalWrite(fan,LOW);
   }
}
