import settings


class ScreenHandle:
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.successor = args[-1]
        else:
            self.successor = None

    def draw(self):
        if self.successor is not None:
            self.successor.draw()

    def connect_engine(self, engine):
        if self.successor is not None:
            return self.successor.connect_engine(engine)


class GameSurface(ScreenHandle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):

        blocks = {
            -2: '#',
            0: ' ',
            1: '0',
            4: '0',
            3: 'o'
        }
        if self.engine.screen == 'game' and not self.engine.pause:
            for i in self.engine.snake_on_map():
                for ii in i:
                    print(blocks[ii], end='')
                print()
            text = 'Score: ' + str(self.engine.snake.length - 2)
            print(' ' * int(settings.WIDTH / 2 - len(text) / 2) + text)

        else:
            super().connect_engine(self.engine)
            super().draw()

    def connect_engine(self, engine=None):
        self.engine = engine
        super().connect_engine(engine)


class HelpWindow(ScreenHandle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        if self.engine.help:
            text = 'h - help \n' \
                   'r - start/restart \n' \
                   'p - pause\n' \
                   'w/a/s/d - in game'
            print(text)
        else:
            super().connect_engine(self.engine)
            super().draw()

    def connect_engine(self, engine=None):
        self.engine = engine
        super().connect_engine(engine)


class MenuWindow(ScreenHandle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        if self.engine.screen == 'menu' and self.engine.help == False:
            for i in range(settings.HEIGHT):
                if i in [0, settings.HEIGHT - 1]:
                    print('#' * settings.WIDTH)
                elif i != int(settings.HEIGHT / 2):
                    print('#' + ' ' * (settings.WIDTH - 2) + '#')
                else:
                    text = 'Press r to start or h to help'
                    line = '#'
                    line += ' ' * int((settings.WIDTH - 2 - len(text)) / 2)
                    line += text
                    line += ' ' * int((settings.WIDTH - 1 - len(text)) / 2)
                    line += '#'
                    print(line)
        else:
            super().connect_engine(self.engine)
            super().draw()

    def connect_engine(self, engine=None):
        self.engine = engine
        super().connect_engine(engine)
