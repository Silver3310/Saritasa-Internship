# -*- coding: utf-8 -*-
"""Output a string with a custom format

This module lets a user to create their own template of how a string
should look like

Example:
    Currently, this module contains a built-in example of dict type that
    contains id, name, action and email fields, so if a user types sth like:
    >>> {name} has id {id} and {email} e-mail
    They'll get: Alice has id 1 and my_mail e-mail

"""

from string import Template, Formatter


def check_and_insert(input_, sample_record):
    """This function is responsible for finding keys and replace them with
    values

    This is the main function of the whole program, it's divided into
    three logical parts, firstly we declare a template, then check if
    everything is ok with braces and then check whether a template contains
    keys that are presented in our example

    Args:
        input_ (string): a string that a user has entered.
        sample_record (dict): key-value pairs to be inserted.

    Returns:
        Either a string with inserted values or a string with a error message.

    """
    # replace the braces to make it suitable for being a Template
    input_ = input_.replace('{', '${')
    # make our input and input_template
    input_template = Template(input_)
    # is our template invalid?
    invalid = False

    try:
        # parse all the keys from input_ like {name} => ['name']
        input_keys = [i[1] for i in Formatter().parse(input_)]
    # ValueError, it occurs in situations like {name{, }name} etc
    except ValueError as e:
        print(e)
        return 'Your template is invalid'

    sample_record_keys = sample_record.keys()

    # he we compare keys that a user has typed and are in our sample
    for key in input_keys:
        # 'if key' is needed as input_keys may contain None value when it
        # encounters some string at the end
        if key and key not in sample_record_keys:
            print(f"There is no '{key}' key")
            invalid = True

    if invalid:
        return 'Your template is invalid'
    else:
        return input_template.substitute(sample_record)


def main():
    # here's our example of context
    example = {
        'id': 1,
        'name': 'Alice',
        'action': 'Attack Bob',
        'email': 'my_mail'
    }
    # get the user format
    input_ = input()
    # a function that is responsible for checking the string and inserting
    # needed values
    output = check_and_insert(input_, example)
    # the result
    print(output)


if __name__ == '__main__':
    main()
