def validate_test_settings(retries: int, timeout: float) -> None:
    if not 0 <= retries <= 5:
        raise ValueError(
            "Количество повторных запусков должно быть от 0 до 5, "
            f"получено: {retries}"
        )

    if timeout <= 0:
        raise ValueError(
            "Таймаут должен быть положительным числом, "
            f"Полученный таймаут: {timeout}"
        )


if __name__ == "__main__":
    test_settings = {
        3: 23.2,
        4: -1.1,
        10: 8.6,
        0: 0,
    }

    for retries, timeout in test_settings.items():
        try:
            validate_test_settings(retries, timeout)
            print(f"Значения валидны: retries={retries}, timeout={timeout}")
        except ValueError as e:
            print(f"Ошибка настроек: {e}")
