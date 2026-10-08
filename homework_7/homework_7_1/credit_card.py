class CreditCard:
    def __init__(self, account_number: str, balance: float) -> None:
        if balance < 0:
            raise ValueError("Начальный баланс карты не может быть отрицательным")

        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        self.__validate_amount(amount)
        self.__balance += amount
        print(f"Счет {self.account_number} пополнен на сумму {amount}")

    def withdraw(self, amount: float) -> None:
        self.__validate_amount(amount)
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Со счета {self.account_number} снята сумма {amount}")
        else:
            print("Недостаточно денег для совершения операции")

    def show_info(self) -> None:
        print(f"Счет карты: {self.account_number}")
        print(f"Баланс карты: {self.__balance}")

    @staticmethod
    def __validate_amount(amount: float) -> None:
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
