from Map import Map
from Snake import Snake
import settings
from random import randint


class Engine:
    def __init__(self, path_to_map=settings.PATH_TO_MAP):
        self.path_to_map = path_to_map
        self.screen = 'menu'
        self.pause = False
        self.help = False

    def snake_on_map(self):
        map_with_snake = self.map.create_map()
        map_with_snake[self.point[1]][self.point[0]] = 3
        for c in self.snake.coor:
            map_with_snake[c[1]][c[0]] += 1
        return map_with_snake

    def new_point(self, map):

        if not self._point_exist(map):
            x = randint(0, settings.WIDTH - 1)
            y = randint(0, settings.HEIGHT - 1)
            #print('x =', x, '\ny =', y, '\n', len(map), '\n', len(map[0]))

            while map[y][x] != 0:
                x = randint(0, settings.WIDTH - 1)
                y = randint(0, settings.HEIGHT - 1)
            self.point = [x, y]
        return self.point

    def _point_exist(self, map):
        if map[self.point[1]][self.point[0]] == 0:
            return True
        return False

    def is_take_point(self, map):
        for i in map:
            if 4 in i:
                return True
        return False

    def game_over(self):
        """
        2 - snake hit snake
        -1 - shake hit wall
        """
        for l in self.snake_on_map():
            if 2 in l or -1 in l:
                return True
        return False

    def create_game(self):
        self.map = Map(self.path_to_map)
        self.snake = Snake()
        self.point = [0, 0]
        self.point = self.new_point(self.map.create_map())

    def start_game(self):
        self.screen = 'game'
