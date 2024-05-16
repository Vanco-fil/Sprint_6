import random


def create_random_data():
    day = random.randint(1, 30)
    month = random.randint(6, 12)
    year = 2024
    date = f"{day}.{month}.{year}"
    return date