#!/usr/bin/python3
"""ADD_ITEMS MODULE
"""

import sys
import json


save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file


def add_items_then_save(args):
    """A script that adds all arguments to a python list, then saves
    them to a file .JSON

    Args:
        args (any): items to add to list
    Returns:
        a list of all arguments passed to script
    """
    filename = 'add_item.json'
    try:
        # load existing items from the file
        existing_items = load_from_json(filename)
    except Exception:
        # if the file does not exist, create an empty list
        existing_items = []

    # add new items from the command line args
    existing_items.extend(args)

    # save the updated list to the file, next
    save_to_json(existing_items, filename)


if __name__ == '__main__':
    # skip the first arg, that is the script filename
    args = sys.argv[1:]
    # call the function we have created to add items and save to the file
    add_items_then_save(args)
