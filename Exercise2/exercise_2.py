# Initial user input
user_input = raw_input("Please enter the number of gallons of gasoline: ")


# Prompts user to enter numerical value if they failed to do so initially.
while not user_input.isdigit():
    user_input = raw_input("That wasn't a number! Please enter a number: ")


# Converts user input from a string to an integer
user_gallon = int(user_input)


# Variables which convert user_input into unit conversions
liters = user_gallon * 3.7854
oil_barrel = user_gallon / 19.5
lbs_COO = user_gallon * 20.0
BTU = user_gallon * 115000.0
cost = user_gallon * 4.0
gas_to_ethanol_ratio = 115000.0 / 75700.0
ethanol_gallon = user_gallon * gas_to_ethanol_ratio


# Execution of program
print "Original number of gallons is: %s" % user_input
print "%s gallons of gasoline requires %s liters" % (user_input, liters)
print "%s gallons of gasoline produces %s barrels of oil" % (user_input, oil_barrel)
print "%s gallons of gasoline produces %s pounds of CO2" % (user_input, lbs_COO)
print "%s gallons of gasoline is energy equivalent to %s gallons of ethanol" % (user_input, ethanol_gallon)
print "%s gallons of gasoline requires %s US dollars" % (user_input, cost)
print "Thanks for playing"