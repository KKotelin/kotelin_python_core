import random
from random import choice

school = {}

for i in range(1, 11):
    school[str(i)+choice(["а", "б", "в", "г"])] = random.randint(20,30)

print(school)
