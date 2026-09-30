def split_numbers(file_name, even_file_name, odd_file_name):
    with open(file_name, 'r') as file:
        numbers = file.read().split()

    with (open(even_file_name, 'w') as even_file,
          open(odd_file_name, 'w') as odd_file):
        for num in numbers:
            if int(num) % 2 == 0:
                even_file.write(num + " ")
            else:
                odd_file.write(num + " ")


if __name__ == '__main__':
    split_numbers("homework_4_2.txt", "even_numbers.txt", "odd_numbers.txt")
