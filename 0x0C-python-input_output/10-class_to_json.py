#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """
    class to json
    """
    return dict(
        (key, value)
        for (key, value) in obj.__dict__.items())
