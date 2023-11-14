import enum
from os import path

import pygame as pg

directions = enum.Enum('directions', 'up right down left')

TARGETFPS = 60

Walls = [
    pg.image.load(path.join(path.dirname(__file__), 'Floor/ancient_debris_side.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/bedrock.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/black_glazed_terracotta.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/blue_glazed_terracotta.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/coal_block.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/cobbled_deepslate.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/cracked_polished_blackstone_bricks.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/crying_obsidian.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/deepslate.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/gray_glazed_terracotta.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/obsidian.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Floor/polished_blackstone.png'))
]

Floors = [
    pg.image.load(path.join(path.dirname(__file__), 'Walls/black_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/blue_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/brown_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/cyan_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/gray_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/green_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/light_blue_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/light_gray_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/lime_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/magenta_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/netherrack.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/orange_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/pink_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/purple_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/red_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/white_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/yellow_wool.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Walls/bricks.png'))
]

Exits = [
    pg.image.load(path.join(path.dirname(__file__), 'Exits/cow.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Exits/pig.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Exits/sheep.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Exits/alex.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Exits/steve.png'))
]

Players = [
    pg.image.load(path.join(path.dirname(__file__), 'Players/alex.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Players/steve.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Players/alex.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Players/enderman.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Players/creeper.png'))
]

Explosion_animation = [
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_0.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_1.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_2.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_3.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_4.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_5.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_6.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_7.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_8.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_9.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_10.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_11.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_12.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_13.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_14.png')),
    pg.image.load(path.join(path.dirname(__file__), 'Explosion/explosion_15.png'))
]

Firework_anim = pg.image.load(path.join(path.dirname(__file__), 'Firework.png'))
