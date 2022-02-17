import settings


class Snake:
    def __init__(self):
        self.length = 2
        self.coor = [[int(settings.WIDTH / 2) + 1, int(settings.HEIGHT / 2)],
                     [int(settings.WIDTH / 2), int(settings.HEIGHT / 2)]]
        self.direction = 'right'

    def change_direction(self, new_direction):
        """for change head direction"""
        directions = {
            'right': 0,
            'left': 0,
            'top': 1,
            'bottom': 1
        }
        if new_direction in directions and directions[new_direction] + directions[self.direction] % 2 == 1:
            self.direction = new_direction

    def step(self):
        directions = {
            'right': (1, 0),
            'left': (-1, 0),
            'top': (0, -1),
            'bottom': (0, 1)
        }
        c_dir = directions[self.direction]
        self.coor.pop()

        self.coor.insert(0, [self.coor[0][0] + c_dir[0], self.coor[0][1] + c_dir[1]])

    def grow_up(self):
        self.length += 1

        directions = {
            'right': (1, 0),
            'left': (-1, 0),
            'top': (0, -1),
            'bottom': (0, 1)
        }
        c_dir = directions[self.direction]

        self.coor.insert(0, [self.coor[0][0] + c_dir[0], self.coor[0][1] + c_dir[1]])
