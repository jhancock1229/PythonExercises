import string
from random import randint
from random import choice

file_name = 'project_5.dat'


def random_string_generator(file_name):
    random_integer = randint(5, 20)
    s = ""
    for i in range(0, random_integer):
        x = choice(string.letters)
        s += x
    with open(file_name, 'w+') as f:
        f.write(s)


def counter(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
        dictionary = {}
        for character in contents:
            if character in dictionary:
                dictionary[character] += 1
            else:
                dictionary[character] = 1
    return dictionary

for i in range(10):
    random_string_generator(file_name)
    print counter(file_name)

# random_string_generator(file_name)
# counter(file_name)


# print sorted(my_dict, values())  # Sorts a dictionary based upon Key
# print sorted(my_dict, key=my_dict.get)  # Sorts a dictionary based upon Value