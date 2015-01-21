__author__ = 'jhancock'
def f_to_c(temp_int):
    celsius = (temp_int - 32)*(5./9)
    return celsius

def c_to_f(temp_int):
    fahrenheit = (temp_int * (9./5) +32)
    return fahrenheit