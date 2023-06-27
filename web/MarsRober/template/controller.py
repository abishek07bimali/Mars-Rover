import pygame
import serial

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
width = 640
height = 480
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Controller")

# Establish serial connection
ser = serial.Serial('COM5', 9600) 

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ser.write(b's')  # Send 'w' to Arduino for forward movement
    elif keys[pygame.K_s]:
        ser.write(b'w')  # Send 's' to Arduino for backward movement

pygame.quit()


# ARDUINO file code
# // Motor A connections
# int enA1 = 0;
# int in1_1 = 1;
# int in2_1 = 2;
# // Motor B connections
# int enB1 = 5;
# int in3_1 = 3;
# int in4_1 = 4;

# // Motor A2 connections
# int enA2 = 27;
# int in1_2 = 25;
# int in2_2 = 23;
# // Motor B2 connections
# int enB2 = 22;
# int in3_2 = 24;
# int in4_2 = 26;

# // Motor A3 connections
# int enA3 = 14;
# int in1_3 = 15;
# int in2_3 = 16;
# // Motor B3 connections
# int enB3 = 19;
# int in3_3 = 18;
# int in4_3 = 17;

# void setup() {
#   Serial.begin(9600);
#   // Set all the motor control pins to outputs
#   pinMode(enA1, OUTPUT);
#   pinMode(enB1, OUTPUT);
#   pinMode(in1_1, OUTPUT);
#   pinMode(in2_1, OUTPUT);
#   pinMode(in3_1, OUTPUT);
#   pinMode(in4_1, OUTPUT);

#   pinMode(enA2, OUTPUT);
#   pinMode(enB2, OUTPUT);
#   pinMode(in1_2, OUTPUT);
#   pinMode(in2_2, OUTPUT);
#   pinMode(in3_2, OUTPUT);
#   pinMode(in4_2, OUTPUT);

#   pinMode(enA3, OUTPUT);
#   pinMode(enB3, OUTPUT);
#   pinMode(in1_3, OUTPUT);
#   pinMode(in2_3, OUTPUT);
#   pinMode(in3_3, OUTPUT);
#   pinMode(in4_3, OUTPUT);
# }

# void moveForward() {
#   // Turn on motors
#   digitalWrite(enA1, HIGH);
#   digitalWrite(enB1, HIGH);
#   digitalWrite(enA2, HIGH);
#   digitalWrite(enB2, HIGH);
#   digitalWrite(enA3, HIGH);
#   digitalWrite(enB3, HIGH);

#   // Set motor directions for forward movement
#   digitalWrite(in1_1, LOW);
#   digitalWrite(in2_1, HIGH);
#   digitalWrite(in3_1, LOW);
#   digitalWrite(in4_1, HIGH);
  
#   digitalWrite(in1_2, LOW);
#   digitalWrite(in2_2, HIGH);
#   digitalWrite(in3_2, LOW);
#   digitalWrite(in4_2, HIGH);
  
#   digitalWrite(in1_3, LOW);
#   digitalWrite(in2_3, HIGH);
#   digitalWrite(in3_3, LOW);
#   digitalWrite(in4_3, HIGH);
# }

# void moveBackward() {
#   // Turn on motors
#   digitalWrite(enA1, HIGH);
#   digitalWrite(enB1, HIGH);
#   digitalWrite(enA2, HIGH);
#   digitalWrite(enB2, HIGH);
#   digitalWrite(enA3, HIGH);
#   digitalWrite(enB3, HIGH);

#   // Set motor directions for backward movement
#   digitalWrite(in1_1, HIGH);
#   digitalWrite(in2_1, LOW);
#   digitalWrite(in3_1, HIGH);
#   digitalWrite(in4_1, LOW);
  
#   digitalWrite(in1_2, HIGH);
#   digitalWrite(in2_2, LOW);
#   digitalWrite(in3_2, HIGH);
#   digitalWrite(in4_2, LOW);
  
#   digitalWrite(in1_3, HIGH);
#   digitalWrite(in2_3, LOW);
#   digitalWrite(in3_3, HIGH);
#   digitalWrite(in4_3, LOW);
# }

# void stopMotors() {
#   // Turn off motors
#   digitalWrite(enA1, LOW);
#   digitalWrite(enB1, LOW);
#   digitalWrite(enA2, LOW);
#   digitalWrite(enB2, LOW);
#   digitalWrite(enA3, LOW);
#   digitalWrite(enB3, LOW);
# }

# void loop() {
#   if (Serial.available() > 0) {
#     char command = Serial.read();  // Read the incoming serial data

#     // Perform actions based on the received command
#     switch (command) {
#       case 'w':
#         moveForward();
#         break;
      
#       case 's':
#         moveBackward();
#         break;

#       default:
#         stopMotors();
#         break;
#     }
#   }
# }
