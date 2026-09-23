if __name__ == '__main__':
    with open("homework_4_1.txt", 'r') as file:
        numbers = file.read().split()

        if len(numbers) < 3:
            print("Ошибка, недостаточно чисел в файле")
        else:
            print(numbers[0], numbers[1], numbers[-2], numbers[-1])
