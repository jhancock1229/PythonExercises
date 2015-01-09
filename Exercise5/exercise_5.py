import string
from random import choice
from random import randint

def random_string():
    random_integer = randint(0, 101)
    s = ''

    # print random_integer

    for i in range(0, random_integer):
        my_char = choice(string.letters)
        s += my_char

    print s
random_string()

# d = dict()
#
# for c in a_string:
#     d[c] = d.get(c,0) + 1
# print d


# if i in my_dict:
#         my_dict[i] += 1
#     else:
#         my_dict[i] = 1