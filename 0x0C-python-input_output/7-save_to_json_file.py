#!/usr/bin/python3
""" save object to file """


def save_to_json_file(my_obj, filename):
    """
    save object to file
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
