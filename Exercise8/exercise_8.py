# from time import clock
#
#
# def naive_fib(n):
#     if n == 0 or n == 1:
#         return n
#     else:
#         return naive_fib(n-1) + naive_fib(n-2)
#
#
# def fib_helper(n):
#     if n == 0:
#         return 0
#     else:
#         return fib_improved(n, 0, 1)
#
#
# def fib_improved(n, p0, p1):
#     if n == 1:
#         return p1
#     else:
#         return fib_improved(n-1, p1, p0+p1)
#
# start1 = clock()
# result1 = fib_improved(40, 0, 1)
# stop1 = clock()
# difference_improved = (stop1 - start1) * 1000
#
#
# start2 = clock()
# result2 = naive_fib(40)
# stop2 = clock()
# difference = (stop2 - start2) * 1000
#
# x = 40
# for i in range(x):
#     naive_fib(x)
#     print difference
#     fib_improved(x, 0, 1)
#     print difference_improved

l = []
def worldmap():
    with open('map.txt', 'r') as f:
        for line in f:
            l.append([])
            for character in line:
                if character != '\n':
                    l[-1].append(character)
        for row in l:
            print row

worldmap()
# my_map = [[], [], []]
#
# def replace_pixel(replacement_character, original_character, x, y):
#
#     if x == -1 or y == -1:
#         return
#
#     if x >= len(my_map[0]):
#         return
#
#     if y >= len(my_map):
#         return
#
#     if my_map[x][y] == original_character:
#         my_map[x][y] = replacement_character
#
#
#     replace_pixel(replacement_character, original_character, x-1, y)
#     replace_pixel(replacement_character, original_character, x+1, y)
#     replace_pixel(replacement_character, original_character, x, y-1)
#     replace_pixel(replacement_character, original_character, x, y+1)