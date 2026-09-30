from exceptions import InvalidTestStatusError


def validate_test_status(status: str) -> None:
    if status not in ("PASS", "FAIL", "SKIP"):
        raise InvalidTestStatusError(
            f"Передан недопустимый статус: {status!r}. "
            "Допустимые статусы: PASS, FAIL, SKIP."
        )


if __name__ == "__main__":
    for status in ("PASS", "FAIL", "SKIP", "TIMEOUT", ""):
        try:
            validate_test_status(status)
            print(f"Допустимый статус: {status}")
        except InvalidTestStatusError as e:
            print(f"Ошибка: {e}")
