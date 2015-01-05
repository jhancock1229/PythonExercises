x = int(raw_input("Please enter the first integer: "))
y = int(raw_input("Please enter the second integer: "))
a = x + y
b = x - y
c = x * y
def d(x,y):
    if y == 0:
        return "You cannot divide by zero!"
    else:
        return x / y
def e(x,y):
    if y == 0:
        return "You cannot divide by zero!"
    else:
        return x % y
print "The sum of" ,x, "and" ,y, "is: " , a
print "The difference of" ,x, "and" ,y, "is: " , b
print "The product of" ,x, "and" ,y, "is: " , c
print "The quotient of" ,x, "and" ,y, "is: " , d(x,y) , "with remainder: " , e(x,y)
