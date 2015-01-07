
def get_user_input(count):
    user_input = raw_input("Please enter the " + count + " integer: ")

    if not user_input.isdigit() or (user_input == "0" and count == "second"):
        print "Not correct. Please try again."
        return get_user_input(count)
    else:
        return int(user_input)

value_1 = get_user_input("first")
value_2 = get_user_input("second")

add = value_1 + value_2
subtract = value_1 - value_2
multiply = value_1 * value_2
division = value_1 / value_2
remainder = value_1 % value_2


print "The sum of %s and %s is %s" % (value_1, value_2, add)
print "The difference of %s and %s is %s" % (value_1, value_2, subtract)
print "The product of %s and %s is %s" % (value_1, value_2, multiply)
print "The quotient of %s and %s is %s with a remainder of %s" % (value_1, value_2, division, remainder)