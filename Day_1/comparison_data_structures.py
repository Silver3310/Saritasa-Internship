# -*- coding: utf-8 -*-
"""Comparison of data structures

This module demonstrates how much memory does each data structure take to
store its data and how fast they are. This method doesn't require any input
data, all values are randomly created.

Firstly, we check how much memory does one instance take of each data
structure.

Secondly we take 3000 instances and check how long does it take to
search for an element in each data structure and create a data structure
itself and how much does it need to store its elements.
"""

from time import time
from sys import getsizeof
from collections import namedtuple, OrderedDict
from datetime import date
from faker import Faker

# declaration of namedtuple
named_tuple = namedtuple(
    'named_tuple',
    ['id', 'name', 'start_date', 'end_date', 'description']
)

# sample data for each data structure
fake = Faker()
_id = 3
name = 'Alex'
start_date = date(2016, 2, 18)
end_date = date(2018, 7, 30)
description = 'a good person'

# creating a list that contains all data structures with the same data
comparison = [
    named_tuple(id, name, start_date, end_date, description),
    (id, name, start_date, end_date, description),
    dict(
      id=id,
      name=name,
      start_date=start_date,
      end_date=end_date,
      description=description
    ),
    [id, name, start_date, end_date, description],
    OrderedDict(
      id=id,
      name=name,
      start_date=start_date,
      end_date=end_date,
      description=description
    ),
    {id, name, start_date, end_date, description}
]

# comparison the data structures based on one instance
print("How much memory one instance takes:")
for each in comparison:
    print(each.__class__.__name__, ':', getsizeof(each))


# a function that estimates how much time data structure needs to perform
# creating, searching and how much memory
# it needs
def time_estimating(func):
    """The function for estimating a period of time

    This function consists of several parts, each part is
    for a particular type of data structure (for dict and OrderedDict
    is the same)

    Inside these parts, we measure time it needs to create itself
    and time it needs to search for the last element (because only
    the last element has 'marty' name)

    Args:
         func - the function itself.

    """

    # default values
    n = 0
    # name that we are gonna search for
    search_name = 'marty'

    # values needed to calculate time and size that a data structure needs
    start_time = 0
    start_time_s = 0
    end_time = 0
    end_time_s = 0
    size = 0

    if func.__name__ == 'list':
        # a list of sample lists
        elements = []
        # start stopwatch
        start_time = time()
        # fill with random records
        while n < 3000:
            elements.append(
                [
                    n,
                    fake.name(),
                    fake.date(),
                    fake.date(),
                    fake.text()
                ]
            )
            n += 1
        # stop stopwatch
        end_time = time()

        # redefine the last record's name
        elements[n - 1][1] = search_name

        # perform searching
        start_time_s = time()
        for each in elements:
            if each[1] == search_name:
                end_time_s = time()

        # size of the whole data structure
        size = getsizeof(elements)

    elif func.__name__ == 'dict' or func.__name__ == 'OrderedDict':
        # a dictionary of dictionaries
        elements = dict() if func.__name__ == 'dict' else OrderedDict()
        # start stopwatch
        start_time = time()
        while n < 3000:
            elements[n] = func(
                id=n,
                name=fake.name(),
                start_date=fake.date(),
                end_date=fake.date(),
                description=fake.text()
            )
            n += 1
        # stop stopwatch
        end_time = time()

        # redefine the last record's name
        elements[n - 1]['name'] = search_name

        # perform searching
        start_time_s = time()
        for i in elements:
            if elements[i]['name'] == search_name:
                end_time_s = time()

        # size of the whole data structure
        size = getsizeof(elements)

    elif func.__name__ == 'tuple':
        # a list of tuples (because we can't create a tuple and then
        # add some values to it)
        elements = []
        # start stopwatch
        start_time = time()
        while n < 2999:
            elements.append(
                (
                    n,
                    fake.name(),
                    fake.date(),
                    fake.date(),
                    fake.text()
                )
            )
            n += 1
        elements.append(
            (
                n,
                search_name,
                fake.date(),
                fake.date(),
                fake.text()
            )
        )
        # turn a list into a tuple
        elements = tuple(elements)
        # stop stopwatch
        end_time = time()

        # perform searching
        start_time_s = time()
        for each in elements:
            if each[1] == search_name:
                end_time_s = time()

        # size of the whole data structure
        size = getsizeof(elements)

    elif func.__name__ == 'set':
        # a set of tuples (because sets are not hashable, then we
        # can't add them to another set)
        elements = func()
        # start stopwatch
        start_time = time()
        while n < 2999:
            elements.add(
                (
                    n,
                    fake.name(),
                    fake.date(),
                    fake.date(),
                    fake.text()
                )
            )
            n += 1
        elements.add(
            (
                n,
                search_name,
                fake.date(),
                fake.date(),
                fake.text()
            )
        )
        # stop stopwatch
        end_time = time()

        # perform searching
        start_time_s = time()
        for each in elements:
            if search_name in each:
                end_time_s = time()

        # size of the whole data structure
        size = getsizeof(elements)

    elif func.__name__ == 'named_tuple':
        # a list of named_tuples
        elements = []
        # start stopwatch
        start_time = time()
        while n < 2999:
            elements.append(
                func(
                    n,
                    fake.name(),
                    fake.date(),
                    fake.date(),
                    fake.text()
                )
            )
            n += 1
        elements.append(
            func(
                n,
                search_name,
                fake.date(),
                fake.date(),
                fake.text()
            )
        )
        elements = tuple(elements)
        # stop stopwatch
        end_time = time()

        # perform searching
        start_time_s = time()
        for each in elements:
            if each.name == search_name:
                end_time_s = time()

        # size of the whole data structure
        size = getsizeof(elements)

    # output the results
    print(
        '{0}: The process of creating took {1:.3} seconds and process'
        ' of searching took {2:.3}, size: {3}'.format(
            func.__name__,
            end_time - start_time,
            end_time_s - start_time_s,
            size)
    )


print()
print("How much memory and time 3000 instances take:")
time_estimating(named_tuple)
time_estimating(tuple)
time_estimating(dict)
time_estimating(list)
time_estimating(OrderedDict)
time_estimating(set)

print()
print(
    "As we see, when we created one instance, 'set' took the most memory\n"
    "When we created 3000 instances, 'OrderedDict' took the most memory\n"
    "Searching was quite fast for 'tuple' and 'list'"
)
