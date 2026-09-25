def analyze_number(number: int) -> None:
    if number % 15 == 0:
        print("BugTest")
    elif number % 5 == 0:
        print("Test")
    elif number % 3 == 0:
        print("Bug")
    else:
        print(number)


for i in range(1, 31):
    analyze_number(i)
