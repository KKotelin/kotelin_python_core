from datetime import timedelta
from functools import reduce

from homework_5.util_functions import get_test_names_by_status, parse_duration, count_statuses


def count_tests_by_status(autotests: list[list[str]]) -> dict[str, int]:
    return count_statuses(
        autotests,
        get_status=lambda test: test[1],
    )


def get_total_duration(autotests: list[list[str]]) -> str:
    time_strings = map(lambda autotest: autotest[2], autotests)
    result_duration = reduce(
        lambda total, time_string: total + parse_duration(time_string),
        time_strings,
        timedelta(),
    )
    return str(result_duration)


def get_failed_test_names(autotests: list[list[str]]) -> list[str]:
    return get_test_names_by_status(
        autotests,
        "FAIL",
        get_status=lambda test: test[1],
        get_name=lambda test: test[0],
    )


def get_passed_test_names(autotests: list[list[str]]) -> list[str]:
    return [
        test[0]
        for test in autotests
        if test[1] == "PASS"
    ]


if __name__ == '__main__':
    autotests_list = [
        ["auth_test", "PASS", "00:00:20"],
        ["logon_test", "FAIL", "00:00:40"],
        ["create_user_test", "SKIP", "00:01:20"],
        ["delete_user_test", "FAIL", "00:01:40"],
    ]

    status_counts = count_tests_by_status(autotests_list)
    failed_names = get_failed_test_names(autotests_list)
    passed_names = get_passed_test_names(autotests_list)
    total_duration = get_total_duration(autotests_list)

    print(f"Количество тестов по статусам: {status_counts}")
    print(f"Упавшие тесты: {failed_names}")
    print(f"Успешные тесты: {passed_names}")
    print(f"Общее время выполнения тестов: {total_duration}")
