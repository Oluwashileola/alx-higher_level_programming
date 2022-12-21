#!/usr/bin/python3
def no_c(my_string):
    '''removes all characters c and C from a string'''
    # string_list = []
    # for i in my_string:
    #     if i != "c" and i != "C":
    #         string_list.append(i)
    # return ("".join(string_list))

    string_list = [i for i in my_string if i != "c" and i != "C"]
    return ("".join(string_list))
