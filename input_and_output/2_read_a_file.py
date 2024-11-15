import os


def read_a_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        if len(lines) >= 3:
            print(lines[2].strip())
        else:
            print("File has less than 3 lines.")


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.txt"
    read_a_file(file_name)
