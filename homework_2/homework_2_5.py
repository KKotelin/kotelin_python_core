def analyze_test_results() -> None:
    test_count = int(input("Введите количество тестов: "))
    results = {"PASS": 0, "FAIL": 0, "SKIP": 0}

    for test_number in range(1, test_count + 1):
        status = input(f"Результат теста №{test_number}: ").strip().upper()

        if status not in results:
            continue

        results[status] += 1

    print("\nИтоговая статистика:")
    for status, count in results.items():
        print(f"{status}: {count}")

    if results["FAIL"] > 0:
        print("Есть упавшие тесты.")
    else:
        print("Выполненные тесты прошли успешно.")


analyze_test_results()
