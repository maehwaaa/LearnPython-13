#Задание 1
class Kacca:
    def __init__(self):
        self.balance = 0

    def top_up(self, x):
        self.balance += x
        print(f"Касса пополнена на {x}. Теперь в кассе {self.balance} золотых.")

    def count_1000(self):
        thousands = self.balance // 1000
        print(f"В кассе {thousands} полных тысяч.")
        return thousands

    def take_away(self, x):
        if x > self.balance:
            raise ValueError("Недостаточно денег в кассе!")
        self.balance -= x
        print(f"Из кассы забрали {x}. Остаток: {self.balance} золотых.")
