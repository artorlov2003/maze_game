import config
import pygame as pg


class Firework(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.sprite_sheet = config.Firework_anim.convert_alpha()
        self.frames = []
        for i in range(30):
            self.frames.append(self.sprite_sheet.subsurface(((i % 6) * 256, (i // 6) * 256, 256, 256)))
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.animation_frame = 0
        self.rect.center = pos

    def update(self):
        self.animation_frame += 1
        if self.animation_frame == len(self.frames):
            self.kill()
            return
        self.image = self.frames[self.animation_frame]
