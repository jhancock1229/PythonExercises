first_int = int(raw_input("Please enter the first integer: "))
second_int = int(raw_input("Please enter the second integer: "))
add = first_int + second_int
subtract = first_int - second_int
multiply = first_int * second_int
def division(x, y):
    if y == 0:
        return "You cannot divide by zero!"
    else:
        return first_int / second_int
def remainder(x, y):
    if y == 0:
        return "You cannot divide by zero!"
    else:
        return first_int % second_int
print "The sum of", first_int, "and", second_int, "is: ", add
print "The difference of", first_int, "and", second_int, "is: ", subtract
print "The product of", first_int, "and", second_int, "is: ", multiply
print "The quotient of", first_int, "and", second_int, "is: ", division(first_int, second_int), "with remainder: ", remainder(first_int, second_int)
