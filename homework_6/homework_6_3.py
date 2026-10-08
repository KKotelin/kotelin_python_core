from functools import wraps


def log_test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Запуск функции:", func.__name__)
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} завершила работу.")
        print("Результат: ", result, "\n")
        return result

    return wrapper


@log_test
def get_name(name: str) -> str:
    return "Имя: " + name


@log_test
def get_full_name(first_name: str, middle_name: str, second_name: str) -> str:
    return f"Имя: {first_name}. Отчество: {middle_name}. Фамилия: {second_name}"


@log_test
def get_age(age: int) -> str:
    return "Возраст: " + str(age)


if __name__ == '__main__':
    test_name = get_name("Кирилл")
    test_full_name = get_full_name("Кирилл", "Владиславович", "Котелин")
    test_age = get_age(27)
