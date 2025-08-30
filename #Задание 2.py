#Задание 2
class turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x  # текущая позиция X
        self.y = y  # текущая позиция Y
        self.s = s  # шаг (количество клеток за ход)

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Шаг не может быть ≤ 0!")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        move
