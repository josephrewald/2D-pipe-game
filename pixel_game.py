import pygame
import sys

class PixelGame:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pixel Line Drawing Game")

        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)

        self.pixel_size = 10
        self.reset()

    def reset(self):
        self.start_pos = [50, 50]
        self.current_pos = self.start_pos.copy()
        self.end_pos = [700, 500]
        self.line = [tuple(self.start_pos)]

    def step(self, action):
        if action == 0:  # Up
            self.current_pos[1] = max(0, self.current_pos[1] - self.pixel_size)
        elif action == 1:  # Down
            self.current_pos[1] = min(self.height - self.pixel_size, self.current_pos[1] + self.pixel_size)
        elif action == 2:  # Left
            self.current_pos[0] = max(0, self.current_pos[0] - self.pixel_size)
        elif action == 3:  # Right
            self.current_pos[0] = min(self.width - self.pixel_size, self.current_pos[0] + self.pixel_size)

        self.line.append(tuple(self.current_pos))

    def render(self):
        self.screen.fill(self.BLACK)
        if len(self.line) > 1:
            pygame.draw.lines(self.screen, self.WHITE, False, self.line, self.pixel_size)
        pygame.draw.rect(self.screen, self.GREEN, (*self.start_pos, self.pixel_size, self.pixel_size))
        pygame.draw.rect(self.screen, self.RED, (*self.end_pos, self.pixel_size, self.pixel_size))
        pygame.draw.rect(self.screen, self.BLUE, (*self.current_pos, self.pixel_size, self.pixel_size))
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.step(0)
                    elif event.key == pygame.K_DOWN:
                        self.step(1)
                    elif event.key == pygame.K_LEFT:
                        self.step(2)
                    elif event.key == pygame.K_RIGHT:
                        self.step(3)
            
            self.render()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = PixelGame()
    game.run()
