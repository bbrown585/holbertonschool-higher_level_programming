#!/usr/bin/python3
def no_c(my_string):
    j = my_string
    return(j.translate({ord('c'): None, ord('C'): None}))
