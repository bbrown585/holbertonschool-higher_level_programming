#!/usr/bin/python3
def roman_to_int(roman_string):
    
    if type(roman_string) != str or not roman_string:
        return(0)
    values = {'I':1, 'V':5, 'X':10, 'L':50, 'L':100, 'D':500, 'M':1000}
    sum = 0
    last = 0

    for i in range(len(roman_string)):
        if last != 0 and last < values [roman_string[i]]:
            sum -= last
        else:
            sum += last
            last = values [roman_string[i]]
            sum += last
            return (sum)

