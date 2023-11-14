import config
import pygame as pg
from os import path


class Player(pg.sprite.Sprite):
    def __init__(self, maze, block_size, maze_size, is_animated=True):
        pg.sprite.Sprite.__init__(self)
        self.block_size = block_size
        self.Maze_size = maze_size
        self.image = pg.image.load(path.join(path.dirname(__file__), "Players/steve.png")).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pg.transform.scale(self.image, (block_size, block_size))
        self.rect = self.image.get_rect()
        self.maze = maze
        self.rect.width = block_size
        self.rect.height = block_size
        self.rect.top = 0
        self.rect.left = 0
        self.is_animated = is_animated
        self.direction = None
        self.x = 0
        self.y = 0
        self.target_x = 0
        self.target_y = 0
        self.move_sound = pg.mixer.Sound(path.join(path.dirname(__file__), "sounds/walk.ogg"))
        self.hit_sound = pg.mixer.Sound(path.join(path.dirname(__file__), "sounds/hit.ogg"))

    def short_move(self, direction):
        if direction is None:
            return
        if self.maze.started_time == 0:
            self.maze.started_time = pg.time.get_ticks()
        self.direction = direction
        if direction == config.directions.up:
            if self.target_y > 0 and self.maze.maze[self.target_x][self.target_y - 1] == 0:
                self.target_y -= 1
        elif direction == config.directions.right:
            if self.target_x < self.Maze_size * 2 - 2 and self.maze.maze[self.target_x + 1][self.target_y] == 0:
                self.target_x += 1
        elif direction == config.directions.down:
            if self.target_y < self.Maze_size * 2 - 2 and self.maze.maze[self.target_x][self.target_y + 1] == 0:
                self.target_y += 1
        elif direction == config.directions.left:
            if self.target_x > 0 and self.maze.maze[self.target_x - 1][self.target_y] == 0:
                self.target_x -= 1
        self.play_sound()

    def move(self, direction):
        if direction is None:
            return
        if self.maze.started_time == 0:
            self.maze.started_time = pg.time.get_ticks()
        self.drop_animation()
        self.direction = direction
        if direction == config.directions.up:
            if self.target_y > 0 and self.maze.maze[self.target_x][self.target_y - 1] == 0:
                self.target_y -= 1
            while self.target_y > 0 and self.maze.maze[self.target_x][self.target_y - 1] == 0 and self.maze.maze[
                self.target_x + 1][self.target_y] == 1 \
                    and self.maze.maze[self.target_x - 1][self.target_y] == 1:
                self.target_y -= 1
        elif direction == config.directions.right:
            if self.target_x < self.Maze_size * 2 - 2 and self.maze.maze[self.target_x + 1][self.target_y] == 0:
                self.target_x += 1
            while self.target_x < self.Maze_size * 2 - 2 and self.maze.maze[self.target_x + 1][
                self.target_y] == 0 and self.maze.maze[
                self.target_x][
                self.target_y + 1] == 1 \
                    and self.maze.maze[self.target_x][self.target_y - 1] == 1:
                self.target_x += 1
        elif direction == config.directions.down:
            if self.target_y < self.Maze_size * 2 - 2 and self.maze.maze[self.target_x][self.target_y + 1] == 0:
                self.target_y += 1
            while self.target_y < self.Maze_size * 2 - 2 and self.maze.maze[self.target_x][
                self.target_y + 1] == 0 and \
                    self.maze.maze[self.target_x + 1][self.target_y] == 1 \
                    and self.maze.maze[self.target_x - 1][self.target_y] == 1:
                self.target_y += 1
        elif direction == config.directions.left:
            if self.target_x > 0 and self.maze.maze[self.target_x - 1][self.target_y] == 0:
                self.target_x -= 1
            while self.target_x > 0 and self.maze.maze[self.target_x - 1][self.target_y] == 0 and self.maze.maze[
                self.target_x][self.target_y + 1] == 1 \
                    and self.maze.maze[self.target_x][self.target_y - 1] == 1:
                self.target_x -= 1
        self.play_sound()

    def play_sound(self):
        if self.x == self.target_x and self.y == self.target_y:
            pg.mixer.Sound.stop(self.hit_sound)
            pg.mixer.Sound.set_volume(self.hit_sound, 0.3)
            pg.mixer.Sound.play(self.hit_sound)
        else:
            pg.mixer.Sound.stop(self.move_sound)
            pg.mixer.Sound.play(self.move_sound)

    def drop_animation(self):
        self.x = self.target_x
        self.y = self.target_y
        self.direction = None

    def teleport(self, x, y):
        self.x = self.target_x = x
        self.y = self.target_y = y
        self.direction = None

    def move_to_start(self):
        self.x = 0
        self.y = 0
        self.direction = None
        self.target_x = 0
        self.target_y = 0

    def update(self):
        if not self.is_animated:
            self.x = self.target_x
            self.y = self.target_y
            return
        if self.x != self.target_x or self.y != self.target_y:
            if self.direction == config.directions.up:
                self.y -= 1
            elif self.direction == config.directions.right:
                self.x += 1
            elif self.direction == config.directions.down:
                self.y += 1
            elif self.direction == config.directions.left:
                self.x -= 1
        else:
            self.direction = None
        self.rect.left = self.x * self.block_size
        self.rect.top = self.y * self.block_size

    def set_image(self, image):
        self.image = pg.transform.scale(image, (self.block_size, self.block_size))
        self.rect = self.image.get_rect()
