#Задание 2
class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x  # текущая позиция X
        self.y = y  # текущая позиция Y
        self.s = s  # шаг (количество клеток за ход)

    def go_up(self):  # увеличивает y на s
        self.y += self.s

    def go_down(self):  # уменьшает y на s
        self.y -= self.s

    def go_left(self):  # уменьшает x на s
        self.x -= self.s

    def go_right(self):  # увеличивает x на s
        self.x += self.s

    def evolve(self):  # увеличивает s на 1
        self.s += 1

    def degrade(self):  # уменьшает s на 1 или ошибка
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError("Шаг не может быть ≤ 0!")

    def count_moves(self, x2, y2):  
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        moves_x = (dx + self.s - 1) // self.s  # делим с округлением вверх
        moves_y = (dy + self.s - 1) // self.s
        return moves_x + moves_y

    def __str__(self):
        return f"Позиция черепашки: ({self.x}, {self.y}), шаг = {self.s}"
    
    def move_to(self, x2, y2): # тут пошаговое движение к конечной точке
        print(f"Старт: ({self.x}, {self.y}), шаг = {self.s}")

        while self.x != x2 or self.y != y2:
            if self.x < x2:
                self.go_right()
            elif self.x > x2:
                self.go_left()

            if self.y < y2:
                self.go_up()
            elif self.y > y2:
                self.go_down()

            print(f"Черепашка сейчас в точке ({self.x}, {self.y})")

        print("Цель достигнута!")

    def __str__(self):
        return f"Позиция черепашки: ({self.x}, {self.y}), шаг = {self.s}"

t = Turtle(0, 0, 1)  # начальная позиция (0,0), шаг = 1
print("Начальная позиция:", t)

x2 = int(input("Введите конечную координату X: "))
y2 = int(input("Введите конечную координату Y: "))

t.move_to(x2, y2)
