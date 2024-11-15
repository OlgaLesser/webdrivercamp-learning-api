import json
import os


def to_json_file(data, filename):
    with open(filename, 'w') as f_h:
        json.dump(data, f_h)


if __name__ == "__main__":
    data_object = {"list": [1, 2, 3, 4, 5],
                   "tuple": (1, 2, 3, 4, 5),
                   "string": "Hello World!",
                   "bool": False,
                   "null": None,
                   "int": 123,
                   "float": 3.14,
                   "dict": {"abc": True, "Hello": "World", 10: [2, 3, 4]}}
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = f"{dir_path}/data.json"
    to_json_file(data_object, file_name)
    with open(file_name, "r") as f:
        print(f.read())
