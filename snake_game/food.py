import random


class Food:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._pos = (0, 0)
        self.spawn()

    def spawn(self, occupied=None):
        if occupied is None:
            occupied = set()
        available = [(x, y) for x in range(self._width) 
                           for y in range(self._height) 
                           if (x, y) not in occupied]
        self._pos = random.choice(available) if available else (self._width // 2, self._height // 2)

    @property
    def x(self):
        return self._pos[0]

    @property
    def y(self):
        return self._pos[1]
