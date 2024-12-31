import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pixel Line Drawing Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Pixel size
pixel_size = 10

# Start and end positions
start_pos = (50, 50)
end_pos = (700, 500)

# Current drawing position
current_pos = list(start_pos)

# List to store the line
line = [start_pos]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_pos[0] -= pixel_size
            elif event.key == pygame.K_RIGHT:
                current_pos[0] += pixel_size
            elif event.key == pygame.K_UP:
                current_pos[1] -= pixel_size
            elif event.key == pygame.K_DOWN:
                current_pos[1] += pixel_size
            
            # Add the new position to the line
            line.append(tuple(current_pos))

    # Clear the screen
    screen.fill(BLACK)

    # Draw the line
    if len(line) > 1:
        pygame.draw.lines(screen, WHITE, False, line, pixel_size)

    # Draw start and end points
    pygame.draw.rect(screen, GREEN, (start_pos[0], start_pos[1], pixel_size, pixel_size))
    pygame.draw.rect(screen, RED, (end_pos[0], end_pos[1], pixel_size, pixel_size))

    # Draw current position
    pygame.draw.rect(screen, BLUE, (current_pos[0], current_pos[1], pixel_size, pixel_size))

    # Check if the end point is reached
    if tuple(current_pos) == end_pos:
        font = pygame.font.Font(None, 36)
        text = font.render("You Win!", True, WHITE)
        screen.blit(text, (width // 2 - 50, height // 2))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()

