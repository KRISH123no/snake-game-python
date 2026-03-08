import os


class ScoreManager:
    def __init__(self, filename: str):
        self._filename = filename
        self._score = 0
        self._highscore = 0
        self._load()

    def _load(self):
        if os.path.exists(self._filename):
            try:
                with open(self._filename, 'r') as f:
                    self._highscore = int(f.read().strip())
            except:
                self._highscore = 0

    def _save(self):
        try:
            with open(self._filename, 'w') as f:
                f.write(str(self._highscore))
        except:
            pass

    def add(self, points: int):
        self._score += points
        if self._score > self._highscore:
            self._highscore = self._score
            self._save()

    def reset(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @property
    def highscore(self):
        return self._highscore
