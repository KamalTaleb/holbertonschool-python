#!/usr/bin/python3
""" create object from json file """
def load_from_json_file(filename):
    """
    create object from json file
    """
    import json
    with open(filename, "r") as f:
        data = json.load(f)
    return data
