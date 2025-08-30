#Задание 2
class turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x  # текущая позиция X
        self.y = y  # текущая позиция Y
        self.s = s  # шаг (количество клеток за ход)

    def go_up(self): # увеличивает y на s
        self.y += self.s

    def go_down(self): # уменьшает y на s
        self.y -= self.s

    def go_left(self): # уменьшает x на s
        self.x -= self.s

    def go_right(self): # увеличивает y на s
        self.x += self.s

    def evolve(self): # увеличивает s на 1
        self.s += 1

    def degrade(self): # уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Шаг не может быть ≤ 0!")

    def count_moves(self, x2, y2): # возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        move
