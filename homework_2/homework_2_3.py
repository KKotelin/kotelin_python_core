users = {}
for i in range(1, 21):
    users[i] = f"User-{i}"


def run_tests_for_users(data: dict[int, str]) -> None:
    for user_id, user_name in data.items():
        if user_id in (5, 10, 15):
            continue
        if user_id == 18:
            break

        print(user_name)


run_tests_for_users(users)
