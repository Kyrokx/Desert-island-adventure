import sys

import pygame


class Game:
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((1080,720))
        pygame.display.set_caption("Desert-island-adventure")

    def run(self):
        running = True

        while running:

            # Refresh window
            pygame.display.flip()

            # Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print("✅ - Window closes")
                    sys.exit(0)
                    running = False
