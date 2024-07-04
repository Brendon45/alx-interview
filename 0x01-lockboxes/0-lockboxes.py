#!/usr/bin/python3
"""
Module 0-lockboxes
"""


def canUnlockAll(boxes):
    """
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1,
    and each box may contain keys to the other boxes.
    Determine if all the boxes can be opened.
    """

    # Start with the first box (index 0)
    position = 0
    # Dictionary to keep track of unlocked boxes
    unlocked = {}

    # Iterate through each box
    for box in boxes:
        # The first box is always unlocked, or if the box is empty
        if len(box) == 0 or position == 0:
            unlocked[position] = "always_unlocked"

        # Iterate through each key in the current box
        for key in box:
            # If the key is valid (within the range of boxes)
            if key < len(boxes) and key != position:
                unlocked[key] = key

        # If the number of unlocked boxes = the total num of boxes, return True
        if len(unlocked) == len(boxes):
            return True

        # Move to the next box
        position += 1

    # If not all boxes are unlocked, return False
    return False
