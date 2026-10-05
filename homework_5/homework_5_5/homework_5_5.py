import json
from datetime import timedelta
from functools import reduce

from homework_5.util_functions import (
    count_statuses,
    get_test_names_by_status,
    parse_duration,
)


def count_tests(tests: list[dict]) -> int:
    return len(tests)


def count_tests_by_status(tests: list[dict]) -> dict[str, int]:
    return count_statuses(
        tests,
        get_status=lambda test: test["status"],
    )


def get_failed_test_names(tests: list[dict]) -> list[str]:
    return get_test_names_by_status(
        tests,
        "FAIL",
        get_status=lambda test: test["status"],
        get_name=lambda test: test["name"],
    )


def get_longest_test(tests: list[dict]) -> dict | None:
    return max(
        tests,
        key=lambda test: parse_duration(test["duration"]),
        default=None,
    )


def get_total_duration(tests: list[dict]) -> str:
    time_strings = [test["duration"] for test in tests]
    total_duration = reduce(
        lambda total, time_string: total + parse_duration(time_string),
        time_strings,
        timedelta(),
    )
    return str(total_duration)


def save_report(
        total_tests: int,
        status_counts: dict[str, int],
        failed_names: list[str],
        longest_test: dict | None,
        total_duration: str,
) -> None:
    report = {
        "total_tests": total_tests,
        "status_counts": status_counts,
        "failed_tests": failed_names,
        "longest_test": longest_test,
        "total_duration": total_duration,
    }

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    try:
        with open("test_results.json", "r", encoding="utf-8") as file:
            tests = json.load(file)

            if not isinstance(tests, list):
                raise TypeError("Ожидался список тестов")

            for test in tests:
                if not isinstance(test, dict):
                    raise TypeError("Каждый тест должен быть словарём")

                for field in ("name", "status", "duration"):
                    if not isinstance(test[field], str):
                        raise TypeError(f"Поле {field!r} должно быть строкой")

            total_tests = count_tests(tests)
            status_counts = count_tests_by_status(tests)
            failed_names = get_failed_test_names(tests)
            longest_test = get_longest_test(tests)
            total_duration = get_total_duration(tests)

            save_report(
                total_tests=total_tests,
                status_counts=status_counts,
                failed_names=failed_names,
                longest_test=longest_test,
                total_duration=total_duration,
            )

    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")

    except json.JSONDecodeError as e:
        print(f"Некорректный JSON: {e}")

    except (KeyError, TypeError, ValueError) as e:
        print(f"Неправильная структура или значения тестовых данных: {e}")
