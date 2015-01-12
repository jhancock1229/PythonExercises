import string
from random import randint
from random import choice

file_name = 'pg10.txt'


def random_string_generator(file_name):
    random_integer = randint(1, 11)
    s = ""
    for i in range(0, random_integer):
        x = choice(string.letters)
        s += x
    with open(file_name, 'a+') as f:
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





random_string_generator(file_name)
counter(file_name)

print counter(file_name)



