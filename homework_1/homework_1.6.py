import random

school = {}

for i in range(1, 11):
    school[str(i) + random.choice(["а", "б", "в", "г"])] = random.randint(20, 30)

print(school)
