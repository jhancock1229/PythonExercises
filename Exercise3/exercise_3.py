# Initial user input code
user_input = raw_input("Please enter a speed in miles/hour: ")
while not user_input.isdigit():
    user_input = raw_input("That didn't work! Please try a different value: ")

user_input_int = int(user_input)
# Below, conversion values are assigned to variables
meters_per_mile = 1609.34
feet_per_mile = 5280.0
hours_in_day = 24.0
days_in_week = 7.0
weeks_in_fortnight = 2.0
barleycorn_per_meter = 117.647
yards_per_mile = 1760
furlong_to_yards = 220.0
yards_per_meter = 1.09361
speed_of_sound_miles_per_hour = 761.207051
speed_of_light_meters_per_second = 299792458.0
seconds_per_hour = 3600.0
convert_to_percent = 100.0
hours_to_fortnight = hours_in_day * days_in_week * weeks_in_fortnight


# Below, variables are combined to produce results for the assignment
barleycorn_per_day = user_input_int * meters_per_mile * barleycorn_per_meter * hours_in_day
furlongs_per_fortnight = (user_input_int * yards_per_mile * furlong_to_yards) / hours_to_fortnight
mach_number = user_input_int / speed_of_sound_miles_per_hour
percent_speed_of_light = (user_input_int * meters_per_mile / seconds_per_hour) / speed_of_light_meters_per_second


# Execution of program
print "Original speed in mph is: %s" % user_input
print "Converted to barleycorn/day is: %s" % barleycorn_per_day
print "Converted to furlongs/fortnight is: %s" % furlongs_per_fortnight
print "converted to Mach number is: %s" % mach_number
print "Converted to the percentage of the speed of light is: %s" % percent_speed_of_light