import test_data


def show_users(users: list) -> None:
    for user in users:
        print(
            f"Логин: {user['user_login']}, "
            f"Возраст: {user['user_age']}, "
            f"Статус: {user['user_status']}"
        )


def show_user_status_statistics(users: list[dict]) -> None:
    print("\nСтатистика пользователей по статусам:")
    statistics = get_user_statistics(users)
    for status, amount in statistics.items():
        print(f"{status}: {amount}")


def get_user_statistics(users: list[dict]) -> dict[str, int]:
    statistics = dict.fromkeys(("ACTIVE", "BLOCKED", "INACTIVE"), 0)
    for user in users:
        statistics[user["user_status"]] += 1
    return statistics


if __name__ == "__main__":
    try:
        user_count = int(input("Введите количество пользователей для генерации: "))
    except ValueError:
        print("Ошибка: введите целое число.")

    else:
        if user_count > 0:
            generated_users = []

            for _ in range(user_count):
                user = test_data.generate_user()
                generated_users.append(user)

            show_users(generated_users)
            show_user_status_statistics(generated_users)
        else:
            print("Ошибка: количество пользователей должно быть больше нуля.")
