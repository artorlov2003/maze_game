import json
import random

from Firework import Firework
from config import *
from Maze import Maze
from Player import Player

cheat = [pg.K_c, pg.K_h, pg.K_e, pg.K_a, pg.K_t]
cheat_index = 0
epilepsy = False


def key_to_direction(key):
    if key in (pg.K_UP, pg.K_w):
        return directions.up
    elif key in (pg.K_RIGHT, pg.K_d):
        return directions.right
    elif key in (pg.K_DOWN, pg.K_s):
        return directions.down
    elif key in (pg.K_LEFT, pg.K_a):
        return directions.left
    else:
        return None


def save_progress(num_of_tnts, hardness, level):
    with open(path.join(path.dirname(__file__), 'save.json'), 'w') as save_file:
        save = {
            'level': level,
            'hardness': hardness,
            'num_of_tnts': num_of_tnts}
        save_file.write(json.dumps(save))


def main(num_of_tnts, maze_size, level):
    global cheat, cheat_index, epilepsy
    block_size = 400 // maze_size
    pg.init()
    pg.mixer.music.load(path.join(path.dirname(__file__), 'sounds/music.ogg'))
    pg.mixer.music.play(-1)
    pg.init()
    clock = pg.time.Clock()
    window_size = pg.Rect(0, 0, (maze_size * 2 - 1) * block_size,
                          (maze_size * 2 - 1) * block_size + 105)
    screen = pg.display.set_mode(window_size.size)
    pg.display.set_caption("Maze")
    sprites = pg.sprite.Group()
    maze = Maze(maze_size, block_size)
    player = Player(maze, block_size, maze_size)
    maze.player_set_image_method = lambda x: player.set_image(x)
    maze.regenerate()
    maze_blocks = maze.MazeBlocks
    tnts = maze.TNTs
    explosions = maze.explosions
    sprites.add(maze.exit)
    # noinspection PyTypeChecker
    sprites.add(player)
    seed = str(maze.current_seed)
    font = pg.font.Font(path.join(path.dirname(__file__), 'MinecraftRegular-Bmg3.otf'), 32)
    win_pause = False
    lvl_time = 0

    while True:
        clock.tick(TARGETFPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                save_progress(num_of_tnts, maze_size, level)
                exit(0)
            elif event.type == pg.KEYDOWN:
                if event.key == cheat[cheat_index]:
                    cheat_index += 1
                    if cheat_index == len(cheat):
                        epilepsy = True
                        cheat_index = 0
                else:
                    cheat_index = 0
                if event.key == pg.K_SPACE and win_pause:
                    win_pause = False
                    player.move_to_start()
                    maze.regenerate()
                    sprites.add(maze.exit)
                    seed = str(maze.current_seed)
                if event.key == pg.K_EQUALS:
                    main(num_of_tnts, maze_size + 1, level)
                elif event.key == pg.K_MINUS:
                    if maze_size > 2:
                        main(num_of_tnts, maze_size - 1, level)
                elif event.key == pg.K_r:
                    win_pause = False
                    player.move_to_start()
                    maze.regenerate()
                    sprites.add(maze.exit)
                    seed = str(maze.current_seed)
                elif event.key == pg.K_ESCAPE:
                    epilepsy = False
                elif event.key == pg.K_BACKSPACE:
                    seed = seed[:-1]
                elif event.key == pg.K_e:
                    if num_of_tnts > 0:
                        maze.explode(player.x, player.y)
                        num_of_tnts -= 1
                elif event.key in (pg.K_0, pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9):
                    seed += event.unicode
                    win_pause = False
                    player.move_to_start()
                    maze.regenerate(int(seed))
                    sprites.add(maze.exit)
                if pg.key.get_pressed()[pg.K_LSHIFT]:
                    player.short_move(key_to_direction(event.key))
                else:
                    player.move(key_to_direction(event.key))

        if epilepsy:
            background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            maze.regenerate()
            sprites.add(maze.exit)
            seed = str(maze.current_seed)
        else:
            background_color = (255, 255, 255)

        hits = pg.sprite.spritecollide(player, tnts, True)
        num_of_tnts += len(hits)
        for hit in pg.sprite.spritecollide(player, sprites, False):
            if hit == maze.exit:
                save_progress(num_of_tnts, maze_size, level)
                lvl_time = pg.time.get_ticks() - maze.started_time
                hit.kill()
                level += 1
                pg.mixer.Sound.play(pg.mixer.Sound(path.join(path.dirname(__file__), "sounds/win.ogg")))
                explosions.add(Firework(player.rect.center))
                win_pause = True
        screen.fill(background_color)
        seed_txt = font.render("seed:" + seed, True, (0, 0, 0))
        tnt_text = font.render(":" + str(num_of_tnts) + " (E)", True, (0, 0, 0))
        help1_text = font.render("Press R to generate new maze.", True, (0, 0, 0))
        help2_text = font.render("You also may enter your own seed", True, (0, 0, 0))
        hard_text = font.render("Hard:" + str(maze_size) + " (+/-)", True, (0, 0, 0))
        level_text = font.render("Level:" + str(level), True, (0, 0, 0))
        screen.blit(seed_txt, (5, (maze_size * 2 - 1) * block_size + 5))
        screen.blit(tnt_text, (300 + 43, (maze_size * 2 - 1) * block_size + 5))
        screen.blit(hard_text, (520, (maze_size * 2 - 1) * block_size + 5))
        screen.blit(help1_text, (5, (maze_size * 2 - 1) * block_size + 40))
        screen.blit(level_text, (550, (maze_size * 2 - 1) * block_size + 40))
        screen.blit(help2_text, (5, (maze_size * 2 - 1) * block_size + 75))
        screen.blit(pg.transform.scale(pg.image.load(path.join(path.dirname(__file__), 'tnt.png')), (40, 40)),
                    (300, (maze_size * 2 - 1) * block_size + 1))
        sprites.update()
        explosions.update()
        maze_blocks.draw(screen)
        tnts.draw(screen)
        sprites.draw(screen)
        if win_pause:
            time_txt = font.render("Completed in " + str(lvl_time / 1000) + "s", True, (0, 0, 0),
                                   (255, 255, 255))
            continue_txt = font.render("(Space) to continue", True, (0, 0, 0),
                                       (255, 255, 255))
            screen.blit(time_txt, (screen.get_width() / 2 - time_txt.get_width() / 2, screen.get_height() / 2 - 100))
            screen.blit(continue_txt,
                        (screen.get_width() / 2 - continue_txt.get_width() / 2, screen.get_height() / 2 - 70))
        explosions.draw(screen)
        pg.display.flip()


if __name__ == "__main__":
    level = 0
    hardness = 10
    num_of_tnts = 10
    try:
        with open(path.join(path.dirname(__file__), 'save.json'), 'r') as save_file:
            save = json.load(save_file)
            level = save['level']
            hardness = save['hardness']
            num_of_tnts = save['num_of_tnts']
    except:
        pass
    main(num_of_tnts, hardness, level)
