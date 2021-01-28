void setup() {
  Serial.begin(115200);
}

void loop() { // Generate a Sine wave
  for (int deg = 0; deg < 360; deg = deg + 8){
    dacWrite(25, int(128 + 80 * (sin(deg*PI/180)+sin(3*deg*PI/180)/3+sin(5*deg*PI/180)/5+sin(7*deg*PI/180)/7+sin(9*deg*PI/180)/9+sin(11*deg*PI/180)/11))); // Square
  }
}
