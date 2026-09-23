def replace_file_data(file_name_1, file_name_2):
    with open(file_name_1, 'rb') as file_1, open(file_name_2, 'rb') as file_2:
        file_1_data = file_1.read()
        file_2_data = file_2.read()

    with (open(file_name_1, 'wb') as update_file_1, open(file_name_2, 'wb') as update_file_2):
        update_file_1.write(file_2_data)
        update_file_2.write(file_1_data)


if __name__ == '__main__':
    replace_file_data("cat.png", "dog.png")
