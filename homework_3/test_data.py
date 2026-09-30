import random

from faker.proxy import Faker

faker = Faker()


def generate_login() -> str:
    return faker.user_name()


def generate_age() -> int:
    return random.randint(18, 100)


def generate_status() -> str:
    return random.choice(["ACTIVE", "BLOCKED", "INACTIVE"])


def generate_user() -> dict:
    return {
        "user_login": generate_login(),
        "user_age": generate_age(),
        "user_status": generate_status(),
    }
