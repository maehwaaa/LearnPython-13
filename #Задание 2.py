#Задание 2
class Turtle:
    def __init__(self, x=0, y=0, s=1):
        self.x = x  # текущая позиция X
        self.y = y  # текущая позиция Y
        self.s = s  # шаг (количество клеток за ход)

    def go_up(self):  # увеличивает y на s
        self.y += self.s
        print(f"Черепашка пошла вверх. Теперь ({self.x}, {self.y})")

    def go_down(self):  # уменьшает y на s
        self.y -= self.s
        print(f"Черепашка пошла вниз. Теперь ({self.x}, {self.y})")

    def go_left(self):  # уменьшает x на s
        self.x -= self.s
        print(f"Черепашка пошла влево. Теперь ({self.x}, {self.y})")

    def go_right(self):  # увеличивает x на s
        self.x += self.s
        print(f"Черепашка пошла вправо. Теперь ({self.x}, {self.y})")

    def evolve(self):  # увеличивает s на 1
        self.s += 1
        print(f"Шаг увеличен. Теперь шаг = {self.s}")

    def degrade(self):  # уменьшает s на 1 или ошибка
        if self.s > 1:
            self.s -= 1
            print(f"Шаг уменьшен. Теперь шаг = {self.s}")
        else:
            print("Ошибка: шаг не может быть ≤ 0!")

    def count_moves(self, x2, y2):
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        moves_x = (dx + self.s - 1) // self.s
        moves_y = (dy + self.s - 1) // self.s
        return moves_x + moves_y

    def __str__(self):
        return f"Позиция черепашки: ({self.x}, {self.y}), шаг = {self.s}"

# основное
def main():
    t = Turtle(0, 0, 1) # изначальная позиция и шаг
    print("🐢 Игра 'Черепашка'! 🐢")
    print("Команды: up, down, left, right, evolve, degrade, count, status, exit")

    while True:
        command = input("\nВведите команду: ").strip().lower()

        if command == "up":
            t.go_up()
        elif command == "down":
            t.go_down()
        elif command == "left":
            t.go_left()
        elif command == "right":
            t.go_right()
        elif command == "evolve":
            t.evolve()
        elif command == "degrade":
            t.degrade()
        elif command == "count":
            x2 = int(input("Введите конечную X: "))
            y2 = int(input("Введите конечную Y: "))
            moves = t.count_moves(x2, y2)
            print(f"До ({x2}, {y2}) минимум шагов: {moves}")
        elif command == "status":
            print(t)
        elif command == "exit":
            print("Выход из игры. Пока! 🐢")
            break
        else:
            print("Неизвестная команда!")


if __name__ == "__main__":
    main()
