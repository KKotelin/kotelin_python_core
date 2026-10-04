from functools import wraps

LOGIN = "Kirill"
PASSWORD = "Qwerty"
KEY = "123"


def retry(count):
    if count < 1:
        raise ValueError("Количество попыток должно быть не меньше 1")

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, count + 1):
                print(f"Попытка: {attempt}")
                result = func(*args, **kwargs)

                if result is True:
                    return result

            print(f"Попытки закончились: выполнено {count}")
            return result

        return wrapper

    return decorator


@retry(5)
def authorization():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if login != LOGIN or password != PASSWORD:
        return False
    print("Авторизация успешна")
    return True


@retry(2)
def authorization_with_key():
    key = input("Введите ключ: ")
    if key != KEY:
        return False
    print("Авторизация по ключу успешна")
    return True


if __name__ == '__main__':
    authorization()
    authorization_with_key()
