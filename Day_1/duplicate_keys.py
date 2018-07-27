# -*- coding: utf-8 -*-
"""Merge two dictionaries

This module merges two dictionaries and warns when they have the same keys.
In the case when two dicts have the same keys, the module keeps values
from the first dict

Example:
    For the following two dictionaries, the warning is going to occur, since
    they both have the same key:

    dict1 = {'a': 'b', 'c': 'd'}
    dict2 = {'e': 'f', 'c': 'q'}

    The result will be:

    new_dict = {'a': 'b', 'c': 'd', 'e': 'f'}

"""

import warnings


def merge_dict(dict1, dict2):
    """The function for merging dict1 and dict2

    Returns:
        dict: new dictionary based on the first one.

    """
    dict1_keys = [x for x in dict1.keys()]

    for key in dict2:
        if key in dict1_keys:
            warnings.warn(
                "You have the duplicated key - {}, value from dict1"
                " remains".format(key)
            )
        else:
            dict1[key] = dict2[key]
    return dict1


def main():
    dict1 = dict(
        name='alex',
        surname='cool',
        birthday=6
    )
    dict2 = dict(
        brother=True,
        sister=False,
        birthday=5
    )
    new_dict = merge_dict(
        dict1,
        dict2
    )
    print(new_dict)


if __name__ == "__main__":
    main()
