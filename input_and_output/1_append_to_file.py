import os


def append_to_file(some_data, some_file_name):
    with open(some_file_name, 'a') as f:
        num_chars = f.write(some_data)
    return num_chars


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"
    data = "\nDon't Panic"
    print(f"Number of chars added: {append_to_file(data, file_name)}")
    data = "\nDon't Panic!!!"
    print(f"Number of chars added: {append_to_file(data, file_name)}")
