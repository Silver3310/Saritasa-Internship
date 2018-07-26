import warnings


def merge_dict(dict1, dict2):
    dict1_keys = [x for x in dict1.keys()]
    dict2_keys = [x for x in dict2.keys()]
    print(dict1_keys, dict2_keys)
    for key in dict2:
        if key in dict1_keys:
            warnings.warn("You have the duplicated key - {}, value from dict1"
                          " remains".format(key))
        else:
            dict1[key] = dict2[key]
    return dict1


def main():
    dict1 = dict(name='alex', surname='cool', birthday=6)
    dict2 = dict(brother=True, sister=False, birthday=5)
    new_dict = merge_dict(dict1, dict2)
    print(new_dict)


if __name__ == "__main__":
    main()
