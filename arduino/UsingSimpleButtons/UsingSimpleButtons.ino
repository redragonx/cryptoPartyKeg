#include <btn.h>
const uint8_t tapBtn = 4;
const uint8_t ledPin = 13;
uint32_t timeoutStart = 0;
uint32_t timeout = 3000;
uint32_t tabMillis = 0;

btn tap(tapBtn,1);


void setup() {
 
  Serial.begin(57600);
    while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  Serial.println("Serial Started");


   // Setup the button with an internal pull-up :
   pinMode(tapBtn, INPUT_PULLUP);

   // Setup the LED :
   pinMode(ledPin, OUTPUT);
}

void loop() {
  tap.state(digitalRead(tapBtn),false);
  digitalWrite(ledPin, tap.press);
  if(tap.commit){
    //Serial.println(tap.hold);
    tabMillis += tap.hold;
    tap.commit = false;
    timeoutStart = millis();
  }
  if(((millis()-timeoutStart)>timeout)&& (tabMillis >0) && (!(tap.press))){
    Serial.println(tabMillis);
    tabMillis = 0;
  }
}
