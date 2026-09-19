def print_report(test_cases_list: list[str], statuses_list: list[str]) -> None:
    for test_case, status in zip(test_cases_list, statuses_list):
        print(f"{test_case} — {status}")

    passed = statuses_list.count("PASS")
    failed = statuses_list.count("FAIL")
    skipped = statuses_list.count("SKIP")
    print(f"\nУспешных тестов: {passed}")
    print(f"Неуспешных тестов: {failed}")
    print(f"Пропущенных тестов: {skipped}")

    if failed > 0:
        print("Тестовый запуск неуспешен")
    else:
        print("Тестовый запуск успешен")


if __name__ == "__main__":
    test_cases = ["Login", "Registration", "Checkout", "Logout"]
    statuses = ["PASS", "FAIL", "PASS", "SKIP"]

    print_report(test_cases, statuses)
