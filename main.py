

import re
import sys
import string


def remove_x(liste): 
    pattern = r"([^\^][0-9]+)"
    value = []
    for x in liste:
        tmp = re.findall(pattern, x)
        if len(tmp):
            value.append(tmp[0])
        else:
            value.append("1")
    return value

def remove_value_from_list(the_list, source):
    for val in source:
        if val in the_list:
            the_list.remove(val)

def remove_value_and_add_zero(the_list, source):
    for val in source:
        if val in the_list:
            the_list.remove(val)
            the_list.append("0")

def get_sign(stri):
    pos = re.findall(r"\-", stri)
    if pos:
        return ('-')
    else:
        return ('+')

def modif_string_to_int(liste):
    new_value = 0
    tmp = ""
    value = 0
    for x in liste:
        print "value:"
        print value
        print "x:"
        print x
        pos = get_sign(x)
        print pos
        tmp = re.findall(r"[0-9]", x)
        print tmp
        for x in tmp:
            value = int(x)
        print value
        if (pos == '-'):
            value *= -1
        new_value += value
    return new_value

def set_list(liste):
    num = []
    x1 = []
    x2 = []
    x1_empty = []
    x_zero = []
    final_list = []
    pattern = r"([^\^][0-9]+)"
    pattern1 = r"(.[0-9]*X\^1)"
    pattern_zero = r"(.[0-9]*X\^0)"
    pattern1_empty = r"(.[0-9]*X[^\^])"
    pattern2 = r"(.[0-9]*X\^2)"
    num = re.findall(pattern,liste)
    x1 = re.findall(pattern1,liste)
    x_zero = re.findall(pattern_zero,liste)
    x1_empty = re.findall(pattern1_empty,liste)
    x2 = re.findall(pattern2,liste)
    x1 = remove_x(x1)
    x2 = remove_x(x2)
    x1_empty = remove_x(x1_empty)
    x_zero = remove_x(x_zero)
    x_1 = x1 + x1_empty
    remove_value_and_add_zero(num, x_zero)
    remove_value_from_list(num, x_1)
    remove_value_from_list(num, x2)
    final_list.append(modif_string_to_int(num))
    final_list.append(modif_string_to_int(x_1))
    final_list.append(modif_string_to_int(x2))
    return final_list

def test(argv):
    lst = []
    rigth = []
    rigth1 = []
    rigth2 = []
    argv[1] = argv[1].replace(" ", "") 
    lst = argv[1].split('=')
    lst[0] = ' '+lst[0]
    lst[1] = ' '+lst[1]

    list_left = []
    list_right = []
    list_left = set_list(lst[0]);
    list_right = set_list(lst[1]);


    print(lst)
    if list_left:
        print("display left:")
        print(list_left)
    if list_right:
        print("display right:")
        print(list_right)
    

if __name__ == "__main__":
    test(sys.argv)
