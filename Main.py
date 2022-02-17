from pynput import keyboard

import os

from datetime import datetime

from Logic import Engine
import ScreenEngine as SE
import settings

engine = Engine()

drawer = SE.GameSurface(SE.MenuWindow(SE.HelpWindow(SE.ScreenHandle())))  # it needs to change. it is only start packet

drawer.connect_engine(engine)

engine.create_game()
# print(drawer.successor.successor.engine)
s_time = datetime.now()
while True:

    with keyboard.Events() as events:
        event = events.get(settings.TIMEOUT/(1.01 ** (engine.snake.length - 2)))

    if type(event) == keyboard.Events.Press and 'char' in dir(event.key):
        if event.key.char == 'h':
            engine.help = not engine.help
            engine.pause = engine.help
        if event.key.char == 'r':
            engine.create_game()
            engine.start_game()
        if event.key.char == 'p':
            engine.pause = not engine.pause
    if engine.screen == 'game':
        print(event)
        if not engine.pause:
            if type(event) == keyboard.Events.Press and 'char' in dir(event.key):
                new_event = False
                if event.key.char == 'w':
                    engine.snake.change_direction('top')
                    if engine.is_take_point(engine.snake_on_map()):
                        engine.snake.grow_up()
                        engine.new_point(engine.snake_on_map())
                    else:
                        engine.snake.step()
                    s_time = datetime.now()
                if event.key.char == 'a':
                    engine.snake.change_direction('left')
                    if engine.is_take_point(engine.snake_on_map()):
                        engine.snake.grow_up()
                        engine.new_point(engine.snake_on_map())
                    else:
                        engine.snake.step()
                    s_time = datetime.now()
                if event.key.char == 's':
                    engine.snake.change_direction('bottom')
                    if engine.is_take_point(engine.snake_on_map()):
                        engine.snake.grow_up()
                        engine.new_point(engine.snake_on_map())
                    else:
                        engine.snake.step()
                    s_time = datetime.now()
                if event.key.char == 'd':
                    engine.snake.change_direction('right')
                    if engine.is_take_point(engine.snake_on_map()):
                        engine.snake.grow_up()
                        engine.new_point(engine.snake_on_map())
                    else:
                        engine.snake.step()
                    s_time = datetime.now()

            if (datetime.now() - s_time).total_seconds() >= settings.TIMEOUT/(1.01 ** (engine.snake.length - 2)):
                if engine.is_take_point(engine.snake_on_map()):
                    engine.snake.grow_up()
                    engine.new_point(engine.snake_on_map())
                else:
                    engine.snake.step()
                s_time = datetime.now()
    os.system('cls')
    if engine.game_over():
        print('Game over')
        input()
        break
    drawer.draw()
