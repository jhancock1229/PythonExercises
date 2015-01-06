# Conditions for first user input: the input has to be a number
first_int = raw_input("Please enter the first integer: ")
while not first_int.isdigit():
    first_int = raw_input("That is not an integer, please enter an integer: ")


# Conditions for second user input: the input has to be a number and cannot be 0
second_int = raw_input("Please enter the second integer: ")
while not second_int.isdigit() or second_int == "0":
    if second_int == "0":
        second_int = (raw_input("You cannot divide by zero! Pick a different value: "))
    else:
        second_int = (raw_input("That is not an integer, please enter an integer: "))


# Variables in which user string input is converted into integers for performing math operations
add = int(first_int) + int(second_int)
subtract = int(first_int) - int(second_int)
multiply = int(first_int) * int(second_int)
division = int(first_int) / int(second_int)
remainder = int(first_int) % int(second_int)


# Execution of the program
print "The sum of %s and %s is: %s" % (first_int, second_int, add)
print "The difference of %s and %s is: %s" % (first_int, second_int, subtract)
print "The product of %s and %s is: %s" % (first_int, second_int, multiply)
print "The quotient of %s and %s is: %s with remainder: %s" % (first_int, second_int, division, remainder)