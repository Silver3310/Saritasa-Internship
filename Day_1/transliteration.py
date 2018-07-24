transl = dict(j='й',
              c='ц',
              u='у',
              k='к',
              e=['е', 'ё', 'э'],
              n='н',
              g='г',
              sh=['ш', 'щ'],
              z='з',
              kh='х',
              f='ф',
              y='ы',
              v='в',
              a='а',
              p='п',
              r='р',
              o='о',
              l='л',
              d='д',
              zh='ж',
              ya='я',
              ch='ч',
              s='с',
              m='м',
              i='и',
              t='т',
              b='б',
              yu='ю')

# get a string from a user
string = input()
transl_string = []
# flag is need for the case if a user type non-russian letter such as )!?., etc
flag = False

for char in string:
    flag = True
    # if it's empty
    if char == ' ':
        transl_string.append(' ')
        continue
    if char == 'ь' or char == 'ъ':
        continue
    # iterating over a dictionary
    for eng, rus in transl.items():
        # for example: if е == е or Е.lower() == e or e in ['e', 'ё', 'э']
        if char == rus or char.lower() == rus or char in rus:
            # if the letter is capital
            if char.isupper():
                # we use the capital too
                transl_string.append(eng.upper())
            else:
                transl_string.append(eng)
            flag = False
            continue
    # if flag is false then there wasn't a satisfied condition, then it's an unknown symbol, so we just add it
    if flag:
        transl_string.append(char)

# output the result
print(''.join(transl_string))
