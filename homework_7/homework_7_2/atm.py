class Atm:
    def __init__(self, twenties: int, fifties: int, hundreds: int) -> None:
        if any(not self.__is_valid_amount(count) for count in (twenties, fifties, hundreds)):
            raise ValueError("Количество купюр должно быть неотрицательным целым числом")

        self.__banknotes = {
            20: twenties,
            50: fifties,
            100: hundreds
        }

    def add_money(self, twenties: int, fifties: int, hundreds: int) -> None:
        new_banknotes = {
            20: twenties,
            50: fifties,
            100: hundreds
        }

        if any(not self.__is_valid_amount(count) for count in new_banknotes.values()):
            raise ValueError("Количество купюр должно быть неотрицательным целым числом")

        for nominal, count in new_banknotes.items():
            self.__banknotes[nominal] += count

    def withdraw(self, amount: int) -> bool:
        if not self.__is_valid_amount(amount):
            raise ValueError("Сумма для снятия должна быть неотрицательным целым числом")

        issued_banknotes = self.__calculate_banknotes(amount)

        if issued_banknotes is None:
            return False

        for nominal, count in issued_banknotes.items():
            self.__banknotes[nominal] -= count

        self.__show_banknotes_count(issued_banknotes)
        return True

    def show_info(self) -> None:
        total = sum(nominal * count for nominal, count in self.__banknotes.items())

        print(f"\nСумма в банкомате: {total}")
        self.__show_banknotes_count(self.__banknotes)

    def __calculate_banknotes(self, amount: int) -> dict[int, int] | None:
        for hundreds in range(min(amount // 100, self.__banknotes[100]), -1, -1):
            remaining_after_hundreds = amount - hundreds * 100

            for fifties in range(min(remaining_after_hundreds // 50, self.__banknotes[50]), -1, -1):
                remaining_after_fifties = remaining_after_hundreds - fifties * 50

                if remaining_after_fifties % 20 != 0:
                    continue

                twenties = remaining_after_fifties // 20

                if twenties <= self.__banknotes[20]:
                    return {
                        20: twenties,
                        50: fifties,
                        100: hundreds
                    }

        return None

    @staticmethod
    def __show_banknotes_count(banknotes: dict[int, int]) -> None:
        for nominal, count in banknotes.items():
            print(f"Количество купюр номиналом {nominal}: {count}")

    @staticmethod
    def __is_valid_amount(value: int) -> bool:
        return type(value) is int and value >= 0
