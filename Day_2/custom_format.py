def check_and_insert(_format, example):
    # We convert this into list to make remove method enabled
    keys = list(example.keys())
    # new string that is our future output
    new_string_list = []
    # a variable for iteration
    i = 0
    while i < len(_format):
        # add a symbol from the input string to the output one
        new_string_list.append(_format[i])
        # if we see that a user is about to define a word
        if _format[i] == '{':
            # we're gonna check all our example's keys
            for k in keys:
                # if there's such a key after {
                if _format[i + 1:len(k) + i + 1] == k:
                    # so there should be }
                    if _format[len(k) + 1 + i] == '}':
                        # if so, we no longer need '{' in our new string
                        new_string_list.pop()
                        # add the value of that key to our new string
                        new_string_list.append(str(example[k]))
                        # now we need to skip this key next, + 1 means '}'
                        i += len(k) + 1
                        # also we no longer need this key
                        keys.remove(k)
                    else:
                        # if a user missed '}' we need to make sure that
                        # there's no other entries
                        if "{{{}}}".format(k) not in _format[len(k) + i + 1:]:
                            # if no, so a user just mistyped a symbol
                            raise Exception('Seems you have missed the }}'
                                            ' symbol for {}'.format(k))
        i += 1
    # here we're gonna to build our string and return it
    return ''.join(new_string_list)


def main():
    # here's our example of context
    example = {
        'id': 1,
        'name': 'Alice',
        'action': 'Attack Bob',
        'email': 'my_mail'
    }
    # get the user format
    _format = input()
    # a function that is responsible for checking the string and inserting
    # needed values
    output = check_and_insert(_format, example)
    # the result
    print(output)


if __name__ == '__main__':
    main()
