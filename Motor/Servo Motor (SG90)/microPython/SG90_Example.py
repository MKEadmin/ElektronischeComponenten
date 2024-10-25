#include <Servo.h>

Servo myServo;  // Create a Servo object to control the SG90 servo motor

void setup() {
  myServo.attach(9);  // Attach the servo motor to digital pin 9
}

void loop() {
  // Move from 0° to 180°
  for (int angle = 0; angle <= 180; angle++) {
    myServo.write(angle);         // Set the servo position
    delay(15);                    // Wait 15 ms to allow the servo to reach the position
  }
  
  // Move from 180° to 0°
  for (int angle = 180; angle >= 0; angle--) {
    myServo.write(angle);         // Set the servo position
    delay(15);                    // Wait 15 ms to allow the servo to reach the position
  }
}
