# -*- coding: utf-8 -*-
"""A module that counts the values in dictionary by keys

This module demonstrates a counter of values in dictionary by keys
based on the list of records which is created randomly

Example:
    As an input is static you'll always see the same output
    The first row is a list of records itself, the second row
    is a list of counters::

        [{'id': 0, 'success': False, 'name': 'Mary'}, {'id': 1, ...
        [{'key': 'success', 'value': True, 'count': 476}, {'key': ....

"""

from random import choice

names_list = ['Lucy', 'Alex', 'Anna', 'Kate', 'John', 'Jake', 'Peter', 'Mary']


def init_records(record_list):
    """This function fills the empty record list with random values

    Args:
        record_list (list): an empty list

    """
    for i in range(1000):
        record_list.append(dict(id=i,
                                success=choice([True, False]),
                                name=choice(names_list)))


def counter(records_list, key, value):
    """The function for counting values by keys

    This function takes the given value and key and starts
    counting records that have the key with a given value

    Returns:
        a counter dict, e.g.{'key': 'success', 'value': True, 'count': 476}

    """
    count = 0
    for each in records_list:
        if each[key] == value:
            count += 1
    return dict(key=key, value=value, count=count)


def counters_list(records_list):
    """This function applies counter function to all record_list items

    Returns:
        a list of counters

    """
    c_list = list()
    c_list.append(counter(records_list, 'success', True))
    c_list.append(counter(records_list, 'success', False))
    for name in names_list:
        c_list.append(counter(records_list, 'name', name))
    return c_list


def main():
    record_list = []
    init_records(record_list)
    print(record_list)

    print(counters_list(record_list))


if __name__ == "__main__":
    main()
