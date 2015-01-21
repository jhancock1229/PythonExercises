import conversions


city_temp = {
    "Boston": "0 C",
    "Boise": "48 F",
    "Phoenix": "85 F",
    "Miami": "40 C",
    "Riverside": "30 C",
    "Baltimore": "32 F"
}


def value_list(city_temp):
    new_list = []
    for c in city_temp:
        new_list.append([c, [city_temp[c].split()]])
    print new_list
    for i in new_list:
        if i[-1][-1][-1] == 'F':




def convert_to_integer(new_list):
    temp_as_int = int(value_list(new_list[0]))
    return temp_as_int


def unit_convert(new_list, temp_as_int):
    if new_list[-1] == "F":
        return conversions.f_to_c(temp_as_int)
    elif new_list[-1] == "C":
        return conversions.c_to_f(temp_as_int)


a = value_list(city_temp)
print a

def assignment():
    for temp in city_temp.values():
        c = unit_convert(temp)
        return c





# def convert_temp():
#     temp_unit = determine_temp_unit()
#     value_list = city_temp_value_list()
#     if temp_unit == "F":
#         conversions.f_to_c(value_list)

# def city_temp_converted(new_list, temp_init):
#     city_temp2 = {}
#     new_values = determine_temp_unit(new_list, temp_int)
#     for line in new_values:
#     return new_values


# def city_temp_value_list():
#     for city in city_temp:
#         new_list = city_temp[city].split()
#         temp_int = int(new_list[0])
#         determine_temp_unit(new_list, temp_int)



# def assignment(city_temp):
#     for city, temp in city_temp.items():
#         print "In %s it is %s," % (city, temp)
#         # print "which is equivalent to %s" % ()
#
# assignment(city_temp)











