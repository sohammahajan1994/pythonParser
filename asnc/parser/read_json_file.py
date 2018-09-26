import json


def read_json_file(filename):
    with open(filename) as f:
        data = json.load(f)

    return data