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
ser = serial.Serial('COM8', 9600) 

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
    elif keys[pygame.K_q]:
        ser.write(b'q') # Send 'q' to Arduino for stopping the motor
    elif keys[pygame.K_a]:
        ser.write(b'a') # Send 'a' to Arduino for turning the servo-motor left
    elif keys[pygame.K_d]:
        ser.write(b'd') # Send 'a' to Arduino for turning the servo-motor right
    elif keys[pygame.K_e]:
        ser.write(b'e') # Send 'a' to Arduino for stopping the servo-motor

pygame.quit()