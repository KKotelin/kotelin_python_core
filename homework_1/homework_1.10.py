from typing import List

def get_unique_number(numbers: List[int]) -> int | None:
    for value in numbers:
        if numbers.count(value) == 1:
            return value
    return None

nums = [1, 5, 2, 9, 2, 9, 1]
result = get_unique_number(nums)
print(f"Число без пары: {result}")


