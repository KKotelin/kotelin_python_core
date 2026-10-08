def create_time_checker(max_time):
    def check_time(actual_time):
        if actual_time > max_time:
            return f"Превышен лимит: {actual_time} сек. Установленный лимит: {max_time} сек."
        return f"Лимит не превышен: {actual_time} сек. Установленный лимит: {max_time} сек."

    return check_time


if __name__ == '__main__':
    pass_test_checker = create_time_checker(5)
    fail_test_checker = create_time_checker(10)

    print(pass_test_checker(7))
    print(fail_test_checker(7))
