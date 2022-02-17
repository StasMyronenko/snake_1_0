import settings
import array


class Map:
    def __init__(self, path_to_map):
        self.width = settings.WIDTH
        self.height = settings.HEIGHT
        self.path_to_map = path_to_map

    def create_map(self):
        if self.path_to_map:
            return 0
        return self._create_simple_map()

    def _create_simple_map(self):
        _map = list()
        for i in range(self.height):
            _map.append(list())
            for ii in range(self.width):
                if ii == 0 or i == 0 or ii == self.width - 1 or i == self.height - 1:
                    _map[i].append(-2)
                else:
                    _map[i].append(0)
        return _map
