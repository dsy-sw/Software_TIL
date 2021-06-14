int EN1Pin = 9;
int in1Pin = 8;
int in2Pin = 7;
int EN2Pin = 3;
int in4Pin = 4;
int in3Pin = 5;

void setup() {
  Serial.begin(9600);

  pinMode(EN1Pin, OUTPUT);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(EN2Pin, OUTPUT);
  pinMode(in3Pin, OUTPUT);
  pinMode(in4Pin, OUTPUT);
  
  analogWrite(EN1Pin, 200);
  analogWrite(EN2Pin, 200);
}

void loop() {
  Serial.println("Forward");
  digitalWrite(in1Pin, HIGH);
  digitalWrite(in2Pin, LOW);
  digitalWrite(in3Pin, HIGH);
  digitalWrite(in4Pin, LOW);
  delay(500);

  Serial.println("Stop");
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, LOW);
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);
  delay(1000);

  Serial.println("Forward");
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, HIGH);
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, HIGH);
  delay(500);

  Serial.println("Stop");
  digitalWrite(in1Pin, LOW);
  digitalWrite(in2Pin, LOW);
  digitalWrite(in3Pin, LOW);
  digitalWrite(in4Pin, LOW);
  delay(1000);
}