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
        
# сама программка 
def main():
    kassa = Kacca()
    print("💰 Добро пожаловать! 💰")
    print("Доступные команды: top_up, take_away, count_1000, exit")

    while True:
        command = input("\nВведите команду: ").strip().lower()

        if command == "top_up":
            amount = int(input("Введите сумму для пополнения: "))
            kassa.top_up(amount)

        elif command == "take_away":
            amount = int(input("Введите сумму для снятия: "))
            try:
                kassa.take_away(amount)
            except ValueError as e:
                print("Ошибка:", e)

        elif command == "count_1000":
            kassa.count_1000()

        elif command == "exit":
            print("Работа завершена!")
            break

        else:
            print("Неизвестная команда! Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()
