first_int = raw_input("Please enter the first integer: ")
while not first_int.isdigit():
    first_int = raw_input("That is not an integer, please enter an integer: ")
    print first_int
second_int = raw_input("Please enter the second integer: ")
while not second_int.isdigit() or second_int == "0":
    if int(second_int) == 0:
        second_int = (raw_input("You cannot divide by zero! Pick a different value: "))
        print "You cannot divide by zero! Pick a different value: "
    else:
        second_int = (raw_input("That is not an integer, please enter an integer: "))
        print second_int
add = int(first_int) + int(second_int)
subtract = int(first_int) - int(second_int)
multiply = int(first_int) * int(second_int)
division = int(first_int) / int(second_int)
remainder = int(first_int) % int(second_int)
print "The sum of %s and %s is: %s" % (first_int, second_int, add)
print "The difference of %s and %s is: %s" % (first_int, second_int, subtract)
print "The product of %s and %s is: %s" % (first_int, second_int, multiply)
print "The quotient of %s and %s is: %s" % (first_int, second_int, division), "with remainder: %s" % remainder
