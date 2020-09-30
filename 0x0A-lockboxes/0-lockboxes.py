#!/usr/bin/python3
"""
    0-lockboxes.py
    Module that determines if all the boxes can be opened
    Returns: True or False
"""


def canUnlockAll(boxes):
    """Open all boxes"""
    length_boxes = len(boxes)
    if not length_boxes:
        return False

    def list_open_boxes(first_box_open, all_keys_gotten, length_boxes):
        """List all boxes"""
        all_keys_gotten.append(first_box_open)
        for key_box_gotten in all_keys_gotten:
            for key_in_box in boxes[key_box_gotten]:
                if (key_in_box not in all_keys_gotten and
                        key_in_box < length_boxes):
                    all_keys_gotten.append(key_in_box)
        return all_keys_gotten

    if len(list_open_boxes(0, [], length_boxes)) == length_boxes:
        return True
    return False
