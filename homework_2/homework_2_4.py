SECRET_NUMBER = 37


def guess_number() -> None:
    attempts = 0
    while True:
        current_number = int(input("Введите число: "))
        attempts += 1

        if current_number < SECRET_NUMBER:
            print("Введённое число меньше секретного.")
        elif current_number > SECRET_NUMBER:
            print("Введённое число больше секретного.")
        else:
            print(f"Вы угадали! Количество попыток: {attempts}")
            return


guess_number()
