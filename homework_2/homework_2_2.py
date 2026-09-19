CORRECT_PASSWORD = "Python123"
MAX_ATTEMPTS = 3


def authorize_user() -> None:
    for attempt in range(1, MAX_ATTEMPTS + 1):
        password = input("Введите пароль: ")

        if password == CORRECT_PASSWORD:
            print("Авторизация успешна!")
            return

        attempts_left = MAX_ATTEMPTS - attempt
        if attempts_left > 0:
            print(f"Неверный пароль. Осталось попыток: {attempts_left}")

    print("Доступ заблокирован: попытки исчерпаны.")


authorize_user()
