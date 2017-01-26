import re
import sys

def handle_error_sup(liste):
    #pattern_other = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^[^0-2]|[\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^[1-2][0-9])"
    #x_other = re.findall(pattern_other,liste)
  #  print liste
    cmpt = 0
    remove = []
    for x in liste:
        if x == 0 and cmpt > 3:
            remove.append(cmpt)
        else:
            cmpt += 1
    for x in remove:
        del liste[x]
    if len(liste) > 4:
        print "exponential greater than 2"
        sys.exit()

def remove_x(liste, num): 
    pattern = r"([\+|\-]?[0-9]*[\.]?[0-9]*)"
    value = []
    for x in liste:
        tmp = re.findall(pattern, x)
        if tmp[0]:
            value.append(tmp[0])
        if not len(value):
            value.append("1")
        elif (value[0] == '+' or value[0] == '-'):
            value[0] += "1"
            num.append(value[0])
    return value

def remove_x_in_num(num):
    for x in num:
        is_x = re.findall(r"X",x)
        if is_x:
            num.remove(x)
    return num

def clean_num(num):
    new_num = []
    for x in num:
        x = x.replace(" ", "") 
        new_num.append(x)
    return new_num

def remove_value_from_list(the_list, source):
    for val in source:
        if val in the_list:
            the_list.remove(val)

def modif_string_to_float(liste):
    new_value = 0
    tmp = []
    value = 0
    for x in liste:
        pos = get_sign(x)
        tmp = re.findall(r"([0-9]*[\.]?[0-9]*)", x)
        for x in tmp:
            if x:
                value = float(x)
        if (pos == '-'):
            value *= -1.
        new_value += value
    return new_value

def get_sign(stri):
    pos = re.findall(r"\-", stri)
    if pos:
        return ('-')
    else:
        return ('+')
