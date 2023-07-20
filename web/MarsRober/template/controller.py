import pygame
import sys
import serial

# Initialize Pygame
pygame.init()

# Establish serial connection
ser = serial.Serial('COM8', 9600)

# Set up the window
width, height = 770, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vehicle Control Buttons")

# Define colors
WHITE = (255, 255, 255)
BLACK = ("#000000")
RED = ("#000000")
GREEN = ("#000000")
BLUE = ("#000000")
YELLOW = ("#000000")
ORANGE = ("#000000")

# Define button dimensions
button_width, button_height = 100, 100
button_padding = 10

# Define button positions
left_button_positions = [
    (50, 75),
    (155, 75),
    (260, 75),
    (50, 190),
    (155, 190),
    (260, 190)
]

right_button_positions = [
    (500, 75),
    (605, 75),
    (710, 75),
    (500, 190),
    (605, 190),
    (710, 190),
    # (815, 130)
]

left_button_labels = ['Q', 'W', 'E', 'A', 'S', 'D']
right_button_labels = ['PageUp', 'UPArrow', 'PageDown', 'LeftArrow', 'DownArrow', 'RightArrow']

# Define button colors
button_colors = [
    RED,
    GREEN,
    BLUE,
    YELLOW,
    ORANGE,
    BLACK,
    BLACK]

# Create the font for button labels
font = pygame.font.Font(None, 24)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_m]:
        ser.write(b'm') # Send 'm' to arduino for auto control mode
    elif keys[pygame.K_w]:
        ser.write(b'w')  # Send 'w' to Arduino for forward movement
    elif keys[pygame.K_s]:
        ser.write(b's')  # Send 's' to Arduino for backward movement
    elif keys[pygame.K_q]:
        ser.write(b'q') # Send 'q' to Arduino for stopping the motor
    elif keys[pygame.K_a]:
        ser.write(b'a') # Send 'a' to Arduino for turning the servo-motor left
    elif keys[pygame.K_d]:
        ser.write(b'd') # Send 'd' to Arduino for turning the servo-motor right
    elif keys[pygame.K_e]:
        ser.write(b'e') # Send 'e' to Arduino for stopping the servo-motor
    elif keys[pygame.K_UP]:
        ser.write(b'UP') # Send '4' to Arduino for turning the camera left
    elif keys[pygame.K_DOWN]:
        ser.write(b'DOWN') # Send '6' to Arduino for turning the camera right
    elif keys[pygame.K_5]:
        ser.write(b'5') # Send '5' to Arduino for stopping the camera
    elif keys[pygame.K_1]:
        ser.write(b'1') # Send '1' to Arduino for stopping the base of camera
    elif keys[pygame.K_LEFT]:
        ser.write(b'LEFT') # Send '2' to Arduino for turning the base of camera left
    elif keys[pygame.K_RIGHT]:
        ser.write(b'RIGHT') # Send '3' to Arduino for turning the base of camera right

    # Clear the screen
    screen.fill(WHITE)

    # Draw left buttons
    for position, color, label in zip(left_button_positions, button_colors, left_button_labels):
        pygame.draw.rect(screen, color, (position[0], position[1], button_width, button_height))
        label_text = font.render(label, True, WHITE)
        label_rect = label_text.get_rect(center=(position[0] + button_width // 2, position[1] + button_height // 2))
        screen.blit(label_text, label_rect)

    # Draw right buttons
    for position, color, label in zip(right_button_positions, button_colors, right_button_labels):
        pygame.draw.rect(screen, color, (position[0] - button_width, position[1], button_width, button_height))
        label_text = font.render(label, True, WHITE)
        label_rect = label_text.get_rect(center=(position[0] - button_width // 2, position[1] + button_height // 2))
        screen.blit(label_text, label_rect)

    # Update the display
    pygame.display.flip()
