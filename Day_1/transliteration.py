# -*- coding: utf-8 -*-
"""Transliteration

This module take a string and transliterates it from English to Russian or
vice versa (depends on the language a user typed in)

Examples:
    'Privet mir))' -> 'Привет мир))'
    'Здравствуйте!' -> 'Zdravstvujte!'
    'Я почти на русском, поэтому это будет in English' ->
    'YA pochti na rуsskom, poetomу eto bуdet in English'

"""

from itertools import chain

transl = {
    'j': 'й',
    'c': 'ц',
    'u': 'y',
    'k': 'к',
    'e': ['е', 'ё', 'э'],
    'n': 'н',
    'g': 'г',
    'sh': ['ш', 'щ'],
    'z': 'з',
    'h': 'х',
    'f': 'ф',
    'y': 'ы',
    'v': 'в',
    'w': 'в',
    'a': 'а',
    'p': 'п',
    'r': 'р',
    'o': 'о',
    'l': 'л',
    'd': 'д',
    'zh': 'ж',
    'ya': 'я',
    'ch': 'ч',
    's': 'с',
    'm': 'м',
    'i': 'и',
    't': 'т',
    'b': 'б',
    'yu': 'ю'
}


def is_rus(string):
    """Checking whether the language is Russian or not

    This function counts the amount of Russian and English letters in a
    user's string and decides what language to choose

    Args:
        string (str): a user's string.

    Returns:
        bool: True for Russian, False otherwise.

    """
    russian_letters = list(
        chain.from_iterable(
            transl.values()
        )
    )
    eng_letters_amount = len(
        [x for x in string if x.lower() in transl.keys()]
    )
    rus_letters_amount = len(
        [x for x in string if x.lower() in russian_letters]
    )
    from_rus = True if rus_letters_amount > eng_letters_amount else False
    return from_rus


def make_transl(string):
    """The main function for transliterating the string

    new transliterated string is presented a list, as we can add new
    values to a list without recreating it.
    Firstly, the function checks the features of Russian language and spaces,
    Secondly, it switches between Russian and English and starts
    transliterating using the declared dictionary. Then it turns a new list
    into a string and sends as a result

    Args:
        string (str): a user's string.

    Returns:
        str: the transliterated string

    """

    transl_string = []
    russian = is_rus(string)

    for char in string:
        # flag is needed for the case if a user type non-russian letter such
        # as )!?., etc
        flag = True
        # if it's empty
        if char == ' ':
            transl_string.append(' ')
            continue
        if char == 'ь' or char == 'ъ':
            transl_string.append('')
            continue
        if russian:
            # iterating over a sorted dictionary (as a dict is an unordered
            # sequence it can give us different values for the keys that
            # have more than one value
            for lng1, lng2 in sorted(
                    transl.items(),
                    key=lambda x: x[0]
            ):
                # for example: if е == е or Е.lower() == e or e in
                #  ['e', 'ё', 'э']
                if char.lower() == lng2 or char.lower() in lng2:
                    # if the letter is capital
                    if char.isupper():
                        # we use the capital too
                        transl_string.append(lng1.upper())
                    else:
                        transl_string.append(lng1)
                    flag = False
                    break
        else:
            for lng1, lng2 in sorted(
                    transl.items(),
                    key=lambda x: x[0]
            ):
                if char.lower() == lng1:
                    # if the letter is capital
                    if char.isupper():
                        # we use the capital too
                        transl_string.append(
                            lng2.upper() if isinstance(lng2, str)
                            else lng2[0].upper())
                    else:
                        transl_string.append(
                            lng2 if isinstance(lng2, str) else lng2[0])
                    flag = False
                    break

        # if flag is false then there wasn't a satisfied condition, then it's
        #  an unknown symbol, so we just add it
        if flag:
            transl_string.append(char)

    # return the result
    return ''.join(transl_string)


def main():
    print("Enter the phrase to transliterate:")
    # get a string from a user
    string = input()
    result = make_transl(string)
    print(result)


if __name__ == '__main__':
    main()
