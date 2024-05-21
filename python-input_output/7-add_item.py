#!/usr/bin/python3

"""creates, adds to json file list of user args"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    filename = "add_item.json"
    f = []

    try:
        f = load_from_json_file(filename)
    except FileNotFoundError:
        pass

    for i in range(1, len(argv)):
        f.append(argv[i])

    save_to_json_file(f, filename)
