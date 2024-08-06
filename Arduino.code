#include <MeMCore.h>

MeDCMotor motorLeft(M1);
MeDCMotor motorRight(M2);

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();  // Clean up the command string

    if (command == "drive_to_zoey's") {
      driveToZoeys();
    } else if (command == "drive_to_ava's") {
      driveToAvas();
    } else {
      Serial.println("Command not recognized.");
    }
  }
}

void driveToZoeys() {
  Serial.println("Driving to Zoey's house.");
  motorLeft.run(200);
  motorRight.run(200);
  delay(5000);  // Adjust time based on real-world testing
  motorLeft.stop();
  motorRight.stop();
}

void driveToAvas() {
  Serial.println("Driving to Ava's house.");
  motorLeft.run(200);
  motorRight.run(200);
  delay(5000);  // Adjust time based on real-world testing
  motorLeft.stop();
  motorRight.stop();
}
