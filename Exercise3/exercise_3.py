user_input = raw_input("Please enter a speed in miles/hour: ")
#Below, conversion values are assigned to variables
meters_per_mile = 1609.34
feet_per_mile = 5280
hours_in_day = 24
days_in_week = 7
weeks_in_fortnight = 2
barleycorn_per_meter = 117.647
feet_to_yards = 3
furlong_to_yards = 220
yards_per_meter = 1.09361
speed_of_sound_feet_per_second = 1130
speed_of_light_meters_per_second = 299792458
seconds_per_hour = 3600
#Below, variables are combined to produce results
barleycorn_per_day = (meters_per_mile * barleycorn_per_meter) / hours_in_day
furlongs_per_fortnight = (meters_per_mile * yards_per_meter * furlong_to_yards) / (hours_in_day * days_in_week * weeks_in_fortnight)
mach_number = (speed_of_sound_feet_per_second * feet_per_mile) / (seconds_per_hour)
percent_speed_of_light = ((meters_per_mile / seconds_per_hour) / speed_of_light_meters_per_second) * 100
print "Original speed in mph is: %s" % user_input
print "Converted to barleycorn/day is: %s" % barleycorn_per_day
print "Converted to furlongs/fortnight is: %s" % furlongs_per_fortnight
print "converted to Mach number is: %s" % mach_number
print "Converted to the percentage of the speed of light is: %s" % percent_speed_of_light