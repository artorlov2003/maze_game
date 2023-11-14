import math
import random
from os import path

import pygame as pg

import config


class Explosion(pg.sprite.Sprite):
    def __init__(self, x, y, block_size):
        super().__init__()
        self.block_size = block_size
        self.image = pg.transform.scale(config.Explosion_animation[0], (self.block_size * 6, self.block_size * 6))
        self.anim_index = 0
        self.rect = self.image.get_rect()
        self.pos = (x, y)
        self.rect.center = self.pos

    def update(self):
        self.anim_index += 1
        if self.anim_index == len(config.Explosion_animation):
            self.kill()
            return
        self.image = pg.transform.scale(config.Explosion_animation[self.anim_index],
                                        (self.block_size * 6, self.block_size * 6))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos


class Exit(pg.sprite.Sprite):
    def __init__(self, block_size, sprite_id, x, y):
        super().__init__()
        self.block_size = block_size
        self.image = pg.transform.scale(config.Exits[sprite_id], (self.block_size, self.block_size))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.block_size
        self.rect.y = y * self.block_size


class MazeBlock(pg.sprite.Sprite):
    def __init__(self, x, y, material, block_size):
        super().__init__()
        self.block_size = block_size
        self.image = pg.transform.scale(material, (self.block_size, self.block_size))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.block_size
        self.rect.y = y * self.block_size


class TNT(pg.sprite.Sprite):
    def __init__(self, x, y, block_size):
        super().__init__()
        self.block_size = block_size
        self.image = pg.transform.scale(pg.image.load(path.join(path.dirname(__file__), 'tnt.png')), (self.block_size, self.block_size))
        self.rect = self.image.get_rect()
        self.rect.x = x * self.block_size
        self.rect.y = y * self.block_size


# noinspection PyTypeChecker
class Maze:
    def __init__(self, maze_size, block_size):
        self.block_size = block_size
        self.maze_size = maze_size
        self.current_seed = 0
        self.randomizer = random.Random(self.current_seed)
        self.TNTs = pg.sprite.Group()
        self.MazeBlocks = pg.sprite.Group()
        self.explosions = pg.sprite.Group()
        self.maze = []
        self.exit_x = 0
        self.exit_y = 0
        self.exit = None
        self.wall = None
        self.floor = None
        self.started_time = 0
        self.player_set_image_method = None
        self.explode_sound = pg.mixer.Sound(path.join(path.dirname(__file__), "sounds/explode.ogg"))

    def regenerate(self, seed=None):
        if self.exit is not None:
            self.exit.kill()
        self.started_time = 0
        if seed is not None:
            self.current_seed = seed
        else:
            self.current_seed = random.randint(0, 2 ** 31 - 1)
        self.randomizer.seed(self.current_seed, version=2)
        self.wall = self.randomizer.choice(config.Walls)
        self.floor = self.randomizer.choice(config.Floors)
        player_exit_pair = self.randomizer.randint(0, len(config.Exits) - 1)
        self.player_set_image_method(config.Players[player_exit_pair])
        self.exit_x = self.randomizer.randint(0, self.maze_size - 1) * 2
        self.exit_y = self.randomizer.randint(0, self.maze_size - 1) * 2
        while self.exit_x == 0 and self.exit_y == 0:
            self.exit_x = self.randomizer.randint(0, self.maze_size - 1) * 2
            self.exit_y = self.randomizer.randint(0, self.maze_size - 1) * 2
        self.exit = Exit(self.block_size, player_exit_pair, self.exit_x, self.exit_y)
        num_of_tnts = self.randomizer.randint(0, self.maze_size // 3)
        self.TNTs.empty()
        for i in range(num_of_tnts):
            self.TNTs.add(
                TNT(self.randomizer.randint(0, self.maze_size - 1) * 2,
                    self.randomizer.randint(0, self.maze_size - 1) * 2, self.block_size))
        maze = [[1 for i in range(self.maze_size * 2)] for j in range(self.maze_size * 2)]
        visited = [[0 for i in range(self.maze_size)] for j in range(self.maze_size)]
        stack = [(0, 0)]
        while stack:
            (row, col) = stack[-1]
            visited[row][col] = 1
            maze[row * 2][col * 2] = 0
            neighbors = [
                (row - 1, col, config.directions.up),
                (row, col + 1, config.directions.right),
                (row + 1, col, config.directions.down),
                (row, col - 1, config.directions.left)
            ]
            unvisited_neighbors = []
            for neighbor in neighbors:
                (r, c, d) = neighbor
                if r < 0 or c < 0 or r >= self.maze_size or c >= self.maze_size:
                    continue
                if visited[r][c] == 0:
                    unvisited_neighbors.append(neighbor)
            if unvisited_neighbors:
                next_cell = self.randomizer.choice(unvisited_neighbors)
                (r_next, c_next, d_next) = next_cell
                if d_next == config.directions.up:
                    maze[row * 2 - 1][col * 2] = 0
                elif d_next == config.directions.right:
                    maze[row * 2][col * 2 + 1] = 0
                elif d_next == config.directions.down:
                    maze[row * 2 + 1][col * 2] = 0
                elif d_next == config.directions.left:
                    maze[row * 2][col * 2 - 1] = 0
                visited[r_next][c_next] = 1
                stack.append((r_next, c_next))
            else:
                stack.pop()
        self.maze = maze
        self.draw()

    def draw(self):
        self.MazeBlocks.empty()
        for y in range(self.maze_size * 2 - 1):
            for x in range(self.maze_size * 2 - 1):
                if self.maze[x][y] == 1:
                    self.MazeBlocks.add(MazeBlock(x, y, self.wall, self.block_size))
                else:
                    self.MazeBlocks.add(MazeBlock(x, y, self.floor, self.block_size))

    def explode(self, x, y):
        self.explosions.add(Explosion((x + 0.5) * self.block_size, (y + 0.5) * self.block_size, self.block_size))
        pg.mixer.Sound.stop(self.explode_sound)
        pg.mixer.Sound.set_volume(self.explode_sound, 0.3)
        pg.mixer.Sound.play(self.explode_sound)
        for i in range(x - 3, x + 4):
            for j in range(y - 3, y + 4):
                if i < 0 or i > self.maze_size * 2 - 1 or j < 0 or j > self.maze_size * 2 - 1:
                    continue
                if self.randomizer.random() < (3 - math.sqrt((x - i) ** 2 + (y - j) ** 2)) * 2 / 3:
                    self.maze[i][j] = 0
        self.draw()
