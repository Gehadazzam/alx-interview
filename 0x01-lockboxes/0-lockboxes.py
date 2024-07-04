#!/usr/bin/python3
"""method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False"""
    # Initialize a set to keep track of visited boxes
    boxesVisited = set()

    def dfs(box):
        # Mark the current box as visited
        boxesVisited.add(box)

        # Iterate over each key in the current box
        for key in boxes[box]:
            # Check if the key corresponds to a valid box that hasn't been visited yet
            if 0 <= key < len(boxes) and key not in boxesVisited:
                # Recursively try to open the box corresponding to the key
                dfs(key)

    # Start DFS from the first box (which is always unlocked)
    dfs(0)

    # If there are any unvisited boxes left, return False; otherwise, return True
    return len(boxesVisited) == len(boxes)
