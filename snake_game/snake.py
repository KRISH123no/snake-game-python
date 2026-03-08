from collections import deque


class Snake:
    def __init__(self, width, height, length=3):
        self._width = width
        self._height = height
        self._dir = (1, 0)
        self._next_dir = (1, 0)
        self._body = deque()
        self._init_body(length)

    def _init_body(self, length):
        x = self._width // 2
        y = self._height // 2
        self._body.clear()
        for i in range(length):
            self._body.append((x - i, y))

    def reset(self, length=3):
        self._dir = (1, 0)
        self._next_dir = (1, 0)
        self._init_body(length)

    def set_direction(self, direction):
        opposite = {(-1, 0): (1, 0), (1, 0): (-1, 0), (0, -1): (0, 1), (0, 1): (0, -1)}
        if direction != opposite.get(self._dir):
            self._next_dir = direction

    def update(self):
        self._dir = self._next_dir
        x, y = self._body[0]
        dx, dy = self._dir
        self._body.appendleft((x + dx, y + dy))
        self._body.pop()

    def grow(self):
        self._body.append(self._body[-1])

    def occupied(self):
        return set(self._body)

    def hit_wall(self):
        x, y = self._body[0]
        return x < 0 or x >= self._width or y < 0 or y >= self._height

    def hit_self(self):
        return self._body[0] in list(self._body)[1:]

    @property
    def head(self):
        return self._body[0]

    @property
    def body(self):
        return self._body
