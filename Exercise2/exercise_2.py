user_input = int(raw_input("Please enter the number of gallons of gasoline: "))
liters = user_input * 3.7854
gas_barrel = user_input / 42
oil_barrel = gas_barrel / 19.5
lbs_COO = user_input * 20
BTU = user_input * 115000
cost = user_input * 4
ethanol_gallon = user_input * (115000 / 75700)
print "Original number of gallons is: %s" % (user_input)
print "%s gallons of gasoline requires %s liters" % (user_input, liters)
print "%s gallons of gasoline produces %s barrels of oil" % (user_input, oil_barrel)
print "%s gallons of gasoline produces %s pounds of CO2" % (user_input, lbs_COO)
print "%s gallons of gasoline is energy equivalent to %s gallons of ethanol" % (user_input, ethanol_gallon)
print "%s gallons of gasoline requires %s US dollars" % (user_input, cost)