#include <Servo.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
Servo drain;
LiquidCrystal_I2C lcd(0x27,16,2);


int trig = 3;
int echo = 4;
float jarak;
long durasi;
bool open = false;
bool pressed = false;
int setd = 30;
 
int drainpin = 7;


int buttonState = 0;


void setup()
{
  lcd.init();                      // initialize the lcd
  lcd.init();
 
 
  drain.attach(drainpin);
  pinMode(2, INPUT);
 
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
 
  Serial.begin(9600);
}


void loop() {
 
  lcd.backlight();
 
 
  digitalWrite(trig, LOW);
  delayMicroseconds(5);
  digitalWrite(trig, HIGH);
  delayMicroseconds(5);
  digitalWrite(trig, LOW);
  delayMicroseconds(5);
 
  durasi = pulseIn(echo, HIGH);
  jarak = (durasi / 2) / 29.1;
  Serial.println(jarak);
 
{
  buttonState = digitalRead(2);
  if (buttonState == HIGH and jarak < setd) {
      open = true;
      pressed = true;
    }
  else if (buttonState == HIGH and jarak > setd)
  {
    open = false;
  }    
  else if (buttonState == LOW and jarak < setd and open == true and pressed == true)  
  {
   open = true;
   delay(3000) ;
  }
  else if (buttonState == LOW and jarak < setd and open == false)  
  {
   open = false;
  }
  else
  {
   open = false;
   pressed = false;
  }
 
  if (open == true) {
    drain.write(135);
    if (Serial.available()) {
      int data = Serial.parseInt();
      Serial.println(data);
      if (data > 99){
        lcd.setCursor(0, 0);
        lcd.print("PARKIR ANDA:     ");
        lcd.setCursor(0, 1);
        lcd.print(data % 99);
        lcd.print("                ");
      }
  }
  }
  else {
   
    drain.write(45);
   
    if (Serial.available() > 0) {
      int numFree = Serial.parseInt();  // menerima data jumlah tempat parkir kosong dari Python
      Serial.println(numFree);
      if (numFree < 99){
        lcd.setCursor(0, 0);
        lcd.print("PARKIR TERSEDIA: ");
        lcd.setCursor(0, 1);
        lcd.print(numFree);
        lcd.print("                ");
      }
  }
  }


    delay(5);
  }
  Serial.println(open);
}

