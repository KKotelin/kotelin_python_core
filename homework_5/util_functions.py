from datetime import timedelta


def count_statuses(autotests, get_status) -> dict[str, int]:
    counts = {"PASS": 0, "FAIL": 0, "SKIP": 0}

    for autotest in autotests:
        status = get_status(autotest)
        counts[status] += 1

    return counts


def get_test_names_by_status(autotests, status, get_status, get_name):
    filtered_tests = filter_tests_by_status(autotests, status, get_status)
    return list(map(get_name, filtered_tests))


def filter_tests_by_status(autotests, status, get_status) -> list[list[str]]:
    status = status.upper()
    return list(filter(lambda test: get_status(test) == status, autotests))


def parse_duration(time_string) -> timedelta:
    hours, minutes, seconds = map(int, time_string.split(":"))

    if hours < 0 or minutes < 0 or seconds < 0:
        raise ValueError(
            f"Время выполнения не может быть отрицательным: {time_string!r}"
        )

    return timedelta(hours=hours, minutes=minutes, seconds=seconds)
