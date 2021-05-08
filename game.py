import sys

import pygame

import pytmx

import pyscroll

from src.Player import Player


class Game:
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Desert-island-adventure")

        # Map data
        tmx_data = pytmx.util_pygame.load_pygame('main_map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 1.8

        # Player spawn
        self.player_spawn = tmx_data.get_object_by_name("spawn")

        # Player instence
        self.player = Player(self.player_spawn.x, self.player_spawn.y)
        # group with map
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=4)
        self.group.add(self.player)

    def handle(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player.move_up()
            self.player.change_image('up')
        elif keys[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_image('down')
        elif keys[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_image('left')
        elif keys[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_image('right')

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            self.handle()
            self.group.update()
            self.group.draw(self.screen)
            self.group.center(self.player.rect.center)
            # Refresh window
            pygame.display.flip()

            # Pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    print("✅ - Window closes")
                    sys.exit(0)
                    running = False

            clock.tick(60)