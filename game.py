import sys

import pygame

import pytmx

import pyscroll

from src.Player import Player

from src.SoundManger import soundManger

import time


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

        # Collision avec les mur
        self.objects_in_map = []
        for obj in tmx_data.objects:
            if obj.type == "collid":
                self.objects_in_map.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        sound = soundManger()
        sound.set_volume(100)
        sound.play_back_sound()

    def handle(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_z]:
            self.player.move_up()
            self.player.change_image('up')
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.move_down()
            self.player.change_image('down')
        elif keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.player.move_left()
            self.player.change_image('left')
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.move_right()
            self.player.change_image('right')

    def update(self):
        self.group.update()

        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.objects_in_map) > -1:
                sprite.move_back()

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:

            self.player.save_location()
            self.handle()
            self.update()
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
