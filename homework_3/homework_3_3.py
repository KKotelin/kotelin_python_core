import random


def generate_results(test_cases: list[str], count: int) -> dict[str, str]:
    selected_tests = random.sample(test_cases, count)

    result = {}
    for test in selected_tests:
        result[test] = random.choice(("PASS", "FAIL", "SKIP"))

    return result


def print_report(results: dict[str, str]) -> None:
    for test, status in results.items():
        print(f"{test} — {status}")


if __name__ == "__main__":
    tests = [
        "test_login",
        "test_logout",
        "test_registration",
        "test_profile",
        "test_payment",
        "test_search"
    ]

    try:
        test_count = int(input("Введите количество тестов для запуска: "))
    except ValueError:
        print("Ошибка: введите целое число.")
    else:
        if 1 <= test_count <= len(tests):
            test_result = generate_results(tests, test_count)
            print_report(test_result)
        else:
            print(f"Ошибка: введите количество от 1 до {len(tests)}.")
