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
print "The sum of %s and %s is: %s" % (first_int, second_int, add)
print "The difference of %s and %s is: %s" % (first_int, second_int, subtract)
print "The product of %s and %s is: %s" % (first_int, second_int, multiply)
print "The quotient of %s and %s is: %s" % (first_int, second_int, division(first_int, second_int)), "with remainder: %s" % (remainder(first_int, second_int))
