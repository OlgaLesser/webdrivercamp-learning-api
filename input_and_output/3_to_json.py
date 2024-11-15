import json


def to_json(some_data):
    return json.dumps(some_data)


if __name__ == "__main__":
    data_types = [[1, 2, 3, 4, 5],
                  (1, 2, 3, 4, 5),
                  "Hello World!",
                  False,
                  None,
                  123,
                  3.14,
                  {"abc": True, "Hello": "World", 10: [2, 3, 4]},
                  {"a", "b", "c"}]
    for data in data_types:
        try:
            json_data = to_json(data)
            print(f"{f'{data}:':17} {type(data).__name__:10} => {json_data}: {type(json_data).__name__}")
        except TypeError as e:
            print("ERROR:")
            print(f"\t{data}: {type(data).__name__} => {e}")
