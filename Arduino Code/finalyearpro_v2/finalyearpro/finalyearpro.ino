int light = 8;
int fan = 9;
char sms;

void setup() {
  Serial.begin(9600);
  pinMode(light,OUTPUT);
  pinMode(fan,OUTPUT);
}

void loop() {
  
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
