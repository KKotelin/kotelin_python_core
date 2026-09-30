def get_test_statistics(results_list: list[str]) -> dict[str, int]:
    statistics = dict.fromkeys(("PASS", "FAIL", "SKIP"), 0)

    for result in results_list:
        if result not in statistics:
            raise ValueError(
                f"Неизвестный статус: {result!r}. "
                "Допустимые статусы: PASS, FAIL, SKIP."
            )
        statistics[result] += 1

    return statistics


def input_test_results() -> list[str]:
    return input("Введите результаты тестов, через пробел: ").upper().split()


def show_statistics(statistics: dict[str, int]) -> None:
    total = sum(statistics.values())

    if total == 0:
        print("Нет результатов тестов для подсчёта статистики.")
        return

    success_percent = statistics["PASS"] / total * 100

    print(f"Всего тестов: {total}")

    for status, count in statistics.items():
        print(f"{status}: {count}")

    print(f"Успешно: {success_percent:.1f}%")


if __name__ == "__main__":
    results = input_test_results()
    try:
        test_statistics = get_test_statistics(results)
    except ValueError as error:
        print(f"Ошибка: {error}")
    else:
        show_statistics(test_statistics)
