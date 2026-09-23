def square_numbers(file_name):
    update_numbers = []

    with open(file_name, 'r') as file:
        for num in file.read().split():
            update_numbers.append(float(num) ** 2)

    with open(file_name, 'w') as file:
        for num in update_numbers:
            file.write(str(num) + "\n")


if __name__ == '__main__':
    square_numbers("homework_4_3.txt")
