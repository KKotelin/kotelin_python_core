import json


def print_users(users_data: list[dict]) -> None:
    for user in users_data:
        try:
            login = user["login"]
            password = user["password"]
            expected_result = user["expected_result"]

            print(
                f"Логин: {login}\n"
                f"Пароль: {password}\n"
                f"Ожидаемый результат авторизации: {expected_result}\n"
            )

        except KeyError as e:
            print(f"Ошибка обработки: Отсутствует обязательное поле: {e}\n")


if __name__ == "__main__":
    try:
        with open("test_users.json", "r", encoding="utf-8") as file:
            users = json.load(file)
            print_users(users)

    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")

    except json.JSONDecodeError as e:
        print(f"Некорректный JSON: {e}")
