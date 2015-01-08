# Initial user input code
user_input = raw_input("Please enter a speed in miles/hour: ")
while True:
    try:
        user_input = float(user_input)
    except ValueError:
        user_input = (raw_input("MPH is a number, you dummy. Please enter an actual speed!: "))
        continue
    else:
        break

user_input_int = int(user_input)


# Below, conversion values are assigned to variables
meters_per_mile = 1609.34
hours_in_day = 24.0
barleycorn_per_meter = 117.647
barleycorn_per_mile = 378669.0/2.0
miles_furlongs = 8.0  # One mile is equal to 8 furlongs
speed_of_sound_mph = 761.207051
feet_per_mile = 5280.0
speed_of_light_mph = 670616629.0
seconds_per_hour = 3600.0
days_in_week = 7.0
weeks_in_fortnight = 2.0
hours_to_fortnight = hours_in_day * days_in_week * weeks_in_fortnight


# Below, variables are combined to produce results for the assignment
barleycorn_per_day = user_input_int * barleycorn_per_mile * hours_in_day
furlongs_per_fortnight = user_input_int * miles_furlongs * hours_to_fortnight
mach_number = user_input_int / speed_of_sound_mph
percent_speed_of_light = user_input_int / speed_of_light_mph


# Execution of program
print "Original speed in mph is: %s" % user_input
print "Converted to barleycorn/day is: %s" % barleycorn_per_day
print "Converted to furlongs/fortnight is: %s" % furlongs_per_fortnight
print "Converted to Mach number is: %s" % mach_number
print "Converted to the percentage of the speed of light is: %s" % percent_speed_of_light
