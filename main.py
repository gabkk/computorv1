import re
import sys
import string



def convert_to_str(value, index):
    if (value >= 0 and index != 0):
        tmp = "+"+str(value)
    else:
        tmp = str(value)
    return tmp

def print_reducted_form(liste):
    index = 0
    sys.stdout.write("reducted form: ")
    if liste[0]:
        sys.stdout.write(convert_to_str(liste[0], index))
        sys.stdout.write(" ")
        index += 1
    if liste[1]:
        sys.stdout.write(convert_to_str(liste[1], index))
        sys.stdout.write("X^0 ")
        index += 1
    if liste[2]:
        sys.stdout.write(convert_to_str(liste[2], index))
        sys.stdout.write("X^1 ")
        index += 1
    if liste[3]:
        sys.stdout.write(convert_to_str(liste[3], index))
        sys.stdout.write("X^2 ")
        index += 1
    sys.stdout.write(" = 0\n")

def remove_x(liste): 
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
    return value

def remove_value_from_list(the_list, source):
    for val in source:
        if val in the_list:
            the_list.remove(val)

def get_sign(stri):
    pos = re.findall(r"\-", stri)
    if pos:
        return ('-')
    else:
        return ('+')

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

def squareroot(x):
    a = 1
    b = x
    while (abs(a-b)>0.0005):
        a = (a+b)/2
        b = x/a
    return a

def handle_error_sup(pattern_other,liste):
    x_other = re.findall(pattern_other,liste)
    for x in x_other:
      ret = re.findall(r"([0-9]$)", x)
      if ret:
        print "Exponential greater than 2"
      else:
        print "Parsing error"
      sys.exit()

def parse_value(liste):
    num = []
    x1 = []
    x2 = []
    x_other = []
    x1_empty = []
    x_zero = []
    final_list = []
    pattern = r"([^\^][0-9]+[\.]?[0-9]*)"
    pattern1 = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^1(?![0-9]))"
    pattern2 = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^2(?![0-9]))"
    pattern_zero = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^0(?![0-9]))"
    pattern_other = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^[^0-2]|[\+|\-]?[[0-9]*[\.]?[0-9]*]*X\^[1-2][0-9])"
    pattern1_empty = r"([\+|\-]?[[0-9]*[\.]?[0-9]*]*X[^\^])"
    
    liste += " "
    num = re.findall(pattern,liste)
    x1 = re.findall(pattern1,liste)
    x_zero = re.findall(pattern_zero,liste)
    x1_empty = re.findall(pattern1_empty,liste)
    x2 = re.findall(pattern2,liste)

    #if an exponential greater than 2 is find return
    handle_error_sup(pattern_other,liste)

    x1 = remove_x(x1)
    x2 = remove_x(x2)
    x1_empty = remove_x(x1_empty)
    x_zero = remove_x(x_zero)
    x_1 = x1 + x1_empty
    num = remove_x_in_num(num)
    num = clean_num(num)
    remove_value_from_list(num, x_zero)
    remove_value_from_list(num, x_1)
    remove_value_from_list(num, x2)
    final_list.append(modif_string_to_float(num))
    final_list.append(modif_string_to_float(x_zero))
    final_list.append(modif_string_to_float(x_1))
    final_list.append(modif_string_to_float(x2))
    return final_list

def sum_lst_value(lst1, lst2):
    lst1[0] -= lst2[0]
    lst1[1] -= lst2[1]
    lst1[2] -= lst2[2]
    lst1[3] -= lst2[3]
    return lst1

def solve_two_solution(liste, discrim):
    print "value of discrim "+ str(discrim)
    x1 = (-liste[2] + (squareroot(discrim)))/(2*liste[3])
    x2 = (-liste[2] - (squareroot(discrim)))/(2*liste[3])
    print "Two solutions"
    print x1
    print x2

def solve_one_solution(liste, discrim):
    print "value of discrim "+ str(discrim)
    x1= -liste[2] / (2 * liste[3])
    print "Only one solution"
    print x1

def solve_first_degree(lst):
    b = -lst[1]
    a = lst[2]
    print b/a

def solve_complex_solution(lst, discrim):
    discrim = discrim*-1
    x_before_i = (-lst[2])/(2.*lst[3])
    x_after_i = (squareroot(discrim))/(2.*lst[3])
    sys.stdout.write(str(x_before_i))
    sys.stdout.write(" + i *")
    sys.stdout.write(str(x_after_i))
    sys.stdout.write("\n")
    sys.stdout.write(str(x_before_i))
    sys.stdout.write(" - i *")
    sys.stdout.write(str(x_after_i))
    sys.stdout.write("\n")

def test(argv):
    lst = []
    discrim = 0
    argv[1] = argv[1].replace(" ", "").replace("*", "").replace("x", "X")
    if not re.findall(r"(\=)", argv[1]):
      print "Parsing error '=' sign missing"
      return ;
    lst = argv[1].split('=')
    lst[0] = ' '+lst[0]
    lst[1] = ' '+lst[1]

    list_left = parse_value(lst[0])
    list_right = parse_value(lst[1])

    lst = sum_lst_value(list_left, list_right)
    print_reducted_form(lst)

    if not lst[1]:
        lst[1] = 0
    if not lst[0]:
        lst[0] = 0
    lst[1] += lst[0]

    if not lst[3] and lst[2]:
        print "Polnomial degree 1"
        solve_first_degree(lst)
        return
    elif lst[3] or lst[2]:
        discrim = (lst[2] * lst[2]) - (4 * lst[3] * lst[1])
        if discrim > 0:
            solve_two_solution(lst, discrim)
        elif discrim == 0:
            solve_one_solution(lst, discrim)
        else:
            print "There are no real solutions. The values are complex numbers"
            solve_complex_solution(lst, discrim)
    else:
        print "We conclude that equation has no solutions"

if __name__ == "__main__":
    test(sys.argv)
