import pygame


class soundManger:
    def __init__(self):
        super().__init__()
        self.back_sound = pygame.mixer.Sound("Assets/Sounds/back_music.wav")

    def play_back_sound(self):
        try:
            pygame.mixer.Sound.play(self.back_sound)
        except EOFError:
            print(EOFError)

    def set_volume(self, volume=10.0):
        try:
            self.back_sound.set_volume(float(volume))
        except EOFError:
            print(EOFError)

    def stop(self):
        try:
            pygame.mixer.Sound.stop()
        except EOFError:
            print(EOFError)
