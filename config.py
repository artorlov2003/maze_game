import enum
from os import path

import pygame as pg

directions = enum.Enum('directions', 'up right down left')

TARGETFPS = 60

Walls = [
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/ancient_debris_side.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/bedrock.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/black_glazed_terracotta.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/blue_glazed_terracotta.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/coal_block.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/cobbled_deepslate.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/cracked_polished_blackstone_bricks.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/crying_obsidian.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/deepslate.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/gray_glazed_terracotta.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/obsidian.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Floor/polished_blackstone.png'))
]

Floors = [
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/black_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/blue_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/brown_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/cyan_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/gray_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/green_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/light_blue_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/light_gray_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/lime_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/magenta_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/netherrack.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/orange_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/pink_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/purple_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/red_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/white_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/yellow_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Walls/bricks.png'))
]

Exits = [
    pg.image.load(path.join(path.dirname(__file__), 'assets/Exits/cow.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Exits/pig.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Exits/sheep.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Exits/alex.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Exits/steve.png'))
]

Players = [
    pg.image.load(path.join(path.dirname(__file__), 'assets/Players/alex.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Players/steve.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Players/alex.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Players/enderman.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Players/creeper.png'))
]

Explosion_animation = [
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_0.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_1.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_2.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_3.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_4.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_5.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_6.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_7.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_8.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_9.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_10.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_11.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_12.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_13.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_14.png')),
    pg.image.load(path.join(path.dirname(__file__), 'assets/Explosion/explosion_15.png'))
]

Firework_anim = pg.image.load(path.join(path.dirname(__file__), 'assets/Firework.png'))
