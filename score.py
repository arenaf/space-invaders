


class Score:
    def __init__(self):
        self.score = 0
        self.level = 1
        try:
            with open("scores.txt") as file:  # Archivo que guarda el nivel más alto alcanzado
                self.high_score = int(file.read())
        except FileNotFoundError:
            with open("scores.txt", "w") as file:
                file.write("0")
                self.high_score = 0

    def new_score(self):
        self.score += 3
        if self.score > self.high_score:
            self.high_score = self.score
        # return self.score

    def new_level(self):
        self.level += 1

    def highest_score(self):
        with open("scores.txt", "w") as file:
            file.write(str(self.high_score))
