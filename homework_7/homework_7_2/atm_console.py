from homework_7.homework_7_2.atm import Atm


class AtmConsole:
    def __init__(self, atm: Atm) -> None:
        self.__atm = atm

    def run_atm(self) -> None:
        print("\n======== Добрый день! ========")

        while True:
            self.__show_menu()
            command = input("Выберите действие: ")

            if command == "4":
                print("Работа завершена. Хорошего дня!")
                break

            self.__handle_command(command)

    def __show_menu(self) -> None:
        print("\n======== ATM ========")
        print("1. Положить деньги")
        print("2. Снять деньги")
        print("3. Показать баланс")
        print("4. Выйти")

    def __handle_command(self, command: str) -> None:
        match command:
            case "1":
                self.__handle_deposit()
            case "2":
                self.__handle_withdraw()
            case "3":
                self.__atm.show_info()
            case _:
                print("Неизвестная команда")

    def __handle_deposit(self) -> None:
        try:
            twenties = int(input("Введите количество купюр с номиналом 20: "))
            fifties = int(input("Введите количество купюр с номиналом 50: "))
            hundred = int(input("Введите количество купюр с номиналом 100: "))

            self.__atm.add_money(twenties, fifties, hundred)
            print("Купюры добавлены")

        except ValueError as error:
            print(f"Ошибка: {error}")

    def __handle_withdraw(self) -> None:
        try:
            amount = int(input("Введите сумму для снятия: "))

            if not self.__atm.withdraw(amount):
                print("Невозможно выдать указанную сумму")

        except ValueError as error:
            print(f"Ошибка: {error}")
