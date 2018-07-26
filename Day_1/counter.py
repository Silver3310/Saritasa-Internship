from random import randint, choice

names_list = ['Laura', 'Alex', 'Anna', 'Kate', 'John', 'Jake', 'Peter', 'Mary']


def init_records(record_list):
    for i in range(1000):
        record_list.append(dict(id=i,
                                success=True if randint(0, 1) == 0 else False,
                                name=choice(names_list)))


def counter(records_list, key, value):
    count = 0
    for each in records_list:
        if each[key] == value:
            count += 1
    return dict(key=key, value=value, count=count)


def counters_list(records_list):
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
