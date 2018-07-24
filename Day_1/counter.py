from random import randint

names_list = ['Laura', 'Alex', 'Anna', 'Kate', 'John', 'Harry', 'Peter', 'Mary']


def init_records(records_list):
    i = 0
    while i < 1000:
        records_list.append(dict(id=i, success=True if randint(0,1) == 0 else False, name=names_list[randint(0, 7)]))
        i += 1


def counter(records_list, key, value):
    count = 0
    for each in records_list:
        if each[key] == value:
            count += 1
    return dict(key=key, value=value, count=count)


def main():
    record_list = []
    init_records(record_list)
    print(record_list)

    count = counter(record_list, 'success', True)
    print(count)

    count = counter(record_list, 'name', 'Kate')
    print(count)


if __name__ == "__main__":
    main()
