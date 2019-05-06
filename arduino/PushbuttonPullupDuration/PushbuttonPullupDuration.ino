/*
  DESCRIPTION
  ====================
  Reports through serial (57600 baud) the time since
  a button press (transition from HIGH to LOW).

*/

// Include the Bounce2 library found here :
// https://github.com/thomasfredericks/Bounce2
#include <Bounce2.h>


#define BUTTON_PIN 4
#define LED_PIN 13

// Instantiate a Bounce object :
Bounce debouncer = Bounce();

unsigned long buttonPressTimeStamp;
bool newBtnState = LOW;
// bool ledState = LOW;

void setup() {

  Serial.begin(57600);
   while (!Serial) {
   ; // wait for serial port to connect. Needed for native USB port only
 }
 Serial.println("Serial Started");


  // Setup the button with an internal pull-up :
  pinMode(BUTTON_PIN, INPUT_PULLUP);


  // After setting up the button, setup the Bounce instance :
  debouncer.attach(BUTTON_PIN);
  debouncer.interval(5);

  // Setup the LED :
  pinMode(LED_PIN, OUTPUT);
  //  digitalWrite(LED_PIN, ledState);
}

void loop() {

  // Update the Bounce instance :
  debouncer.update();

  newBtnState = debouncer.read();

  if (newBtnState == LOW) {
    digitalWrite(LED_PIN, LOW);
    Serial.println("-1");



  }

  if (newBtnState == HIGH) {
    digitalWrite(LED_PIN, HIGH);
    Serial.println(debouncer.duration());

    //  Serial.println("end");


  }

}
