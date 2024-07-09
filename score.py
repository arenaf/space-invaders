


class Score:
    def __init__(self):
        self.score = 0
        self.level = 1

    def new_score(self):
        self.score += 3
        return self.score

    def new_level(self):
        self.level += 1

    def gameover(self):
        pass



