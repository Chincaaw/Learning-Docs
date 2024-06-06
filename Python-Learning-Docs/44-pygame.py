import pygame

## Initialization
pygame.init()
# Game running variable
running = True

# Create display surface object
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))

# Game object
# Position
x_pos = 250
y_pos = 250

# Size
width = 20
height = 20

# Movement speed
speed = 10

while running:
    pygame.time.delay(10)

    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keyboard input
    keys = pygame.key.get_pressed()

    # Move left
    if keys[pygame.K_LEFT] and x_pos > 0:
        x_pos -= speed
    
    # Move right
    if keys[pygame.K_RIGHT] and x_pos < window_width - width:
        x_pos += speed

    # Move down
    if keys[pygame.K_DOWN] and y_pos < window_height - height:
        y_pos += speed

    # Move up
    if keys[pygame.K_UP] and y_pos > 0:
        y_pos -= speed

    # Game dynamics
    
    # Update assets
    window.fill((255, 255, 255))  # Fill window with white color
    pygame.draw.rect(window, (255, 120, 0), (x_pos, y_pos, width, height))  # Draw character
    # Render to display
    pygame.display.update()

pygame.quit()
