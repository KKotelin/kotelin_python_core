def get_pass_test_count(tests: list):
    if len(tests) == 0:
        return 0

    current = 1 if tests[0] == "PASS" else 0
    return current + get_pass_test_count(tests[1:])


if __name__ == '__main__':
    tests_result = [
        "PASS",
        "FAIL",
        "SKIP",
        "PASS",
        "FAIL",
    ]

    print(f"Количество успешных тестов: {get_pass_test_count(tests_result)}")
