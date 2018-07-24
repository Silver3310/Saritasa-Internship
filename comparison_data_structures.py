from time import time
from sys import getsizeof
from collections import namedtuple, OrderedDict
from datetime import date
import random

# declaration of namedtuple
named_tuple = namedtuple('named_tuple', ['id', 'name', 'start_date', 'end_date', 'description'])

# sample data for each data structure
id = 3
name = 'Alex'
start_date = date(2016, 2, 18)
end_date = date(2018, 7, 30)
description = 'a good person'

# creating a list that contains all data structures with the same data
comparison = [named_tuple(id, name, start_date, end_date, description),
              (id, name, start_date, end_date, description),
              dict(id=id, name=name, start_date=start_date, end_date=end_date, description=description),
              [id, name, start_date, end_date, description],
              OrderedDict(id=id, name=name, start_date=start_date, end_date=end_date, description=description),
              {id, name, start_date, end_date, description}]

# comparison the data structures based on one instance
print("How much memory one instance takes:")
for each in comparison:
    print(each.__class__.__name__, ':', getsizeof(each))


# Let's create a lot of instances to check how fast it is to go throughout them

# random values to fill the fields
names_list = ['alex', 'john', 'maria', 'cate', 'jake', 'andrew', 'peter', 'mary', 'harry', 'susan']
desc_list = ['good', 'bad', 'attractive', 'good-looking', 'well-educated', 'beautiful', 'pretty', 'usual', 'cool',
             'lovely']


# a function that returns a random name
def name_r():
    return names_list[random.randint(0, 9)]


# a function that returns a random date
def date_r():
    return date(random.randint(1978, 2018), random.randint(1, 12), random.randint(1, 28))


# a function that returns a random description
def desc_r():
    return desc_list[random.randint(0,9)]


# a function that estimates how much time data structure needs to perform creating, searching and how much memory
# it needs
def time_estimating(func):

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
        while n < 100000:
            elements.append([n, name_r(), date_r(), date_r(), desc_r()])
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

    elif func.__name__ == 'dict':
        # a dictionary of dictionaries
        elements = {}
        # start stopwatch
        start_time = time()
        while n < 100000:
            elements[n] = func(id=n, name=name_r(), start_date=date_r(), end_date=date_r(), description=desc_r())
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
        # a list of tuples (because we can't create a tuple and then add some values to it)
        elements = []
        # start stopwatch
        start_time = time()
        while n < 99999:
            elements.append((n, name_r(), date_r(), date_r(), desc_r()))
            n += 1
        elements.append((n, search_name, date_r(), date_r(), desc_r()))
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
        # a set of tuples (because sets are not hashable, then we can't add them to another set)
        elements = func()
        # start stopwatch
        start_time = time()
        while n < 99999:
            elements.add((n, name_r(), date_r(), date_r(), desc_r()))
            n += 1
        elements.add((n, search_name, date_r(), date_r(), desc_r()))
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
        while n < 99999:
            elements.append(func(n, name_r(), date_r(), date_r(), desc_r()))
            n += 1
        elements.append(func(n, search_name, date_r(), date_r(), desc_r()))
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

    elif func.__name__ == 'OrderedDict':
        # an OrderedDict of OrderedDicts
        elements = OrderedDict()
        # start stopwatch
        start_time = time()
        while n < 100000:
            elements[n] = func(id=n, name=name_r(), start_date=date_r(), end_date=date_r(), description=desc_r())
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

    # output the results
    print('{0}: The process of creating took {1:.3} seconds and process of searching took {2:.3}, size: {3}'.format(
        func.__name__, end_time - start_time, end_time_s - start_time_s, size))


print()
print("How much memory and time 100000 instances take:")
time_estimating(named_tuple)
time_estimating(tuple)
time_estimating(dict)
time_estimating(list)
time_estimating(OrderedDict)
time_estimating(set)

print()
print("As we see, when we created one instance, 'set' took the most memory\nWhen we created 100000 instances, "
      "'OrderedDict' took the most memory\nSearching was quite fast for 'tuple' and 'list'")
