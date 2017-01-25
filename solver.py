import re
import sys
import string
from parse import parse_value

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

def squareroot(x):
    a = 1
    b = x
    while (abs(a-b)>0.0005):
        a = (a+b)/2
        b = x/a
    return a

def sum_lst_value(lst1, lst2):
    lst1[0] -= lst2[0]
    lst1[1] -= lst2[1]
    lst1[2] -= lst2[2]
    lst1[3] -= lst2[3]
    return lst1

def solve_first_degree(lst):
    b = -lst[1]
    a = lst[2]
    print b/a

def solve_one_solution(liste, discrim):
    print "value of discrim "+ str(discrim)
    x1= -liste[2] / (2 * liste[3])
    if x1 == "-0":
      x1 = 0
    print "Only one solution"
    print "x1= " + str(x1)

def solve_two_solution(liste, discrim):
    print "value of discrim "+ str(discrim)
    x1 = (-liste[2] + (squareroot(discrim)))/(2*liste[3])
    x2 = (-liste[2] - (squareroot(discrim)))/(2*liste[3])
    print "Two solutions"
    #round number
    if int(x1)-x1 < 0.0000001:
      x1 = int(x1)
    print "X= " + str(x1)
    if int(x2)-x2 < 0.0000001:
      x2 = int(x2)
    print "X1= " + str(x2)

def solve_complex_solution(lst, discrim):
    print "There are no real solutions. The values are complex numbers"
    print discrim
    discrim = discrim*-1
    x_before_i = (-lst[2])/(2.*lst[3])
    x_after_i = (squareroot(discrim))/(2.*lst[3])
    #round number
    if x_after_i < 0 and (int(x_after_i) + x_after_i < 0.0000001):
      x_after_i = int(x_after_i)
    elif (int(x_after_i) + x_after_i) < 0.0000001:
      x_after_i = int(x_after_i)
    #print
    if x_before_i != 0:
      sys.stdout.write(str(x_before_i))
    sys.stdout.write(" + i *")
    sys.stdout.write(str(x_after_i))
    sys.stdout.write("\n")
    if x_before_i != 0:
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
    try:
      error = lst[1][0]
    except IndexError:
      print "Parsing error you should enter a value after equal"
      return;
    try:
      error = lst[0][0]
    except IndexError:
      print "Parsing error you should enter a value before equal"
      return ;

    lst[0] = ' '+lst[0]
    lst[1] = ' '+lst[1]
    list_left = parse_value(lst[0])
    list_right = parse_value(lst[1])
    lst = sum_lst_value(list_left, list_right)
    print_reducted_form(lst)

    if (lst[0] == lst[1]) and not lst[2] and not lst[3]:
      print "The polynome have all the real numbers as solution"
      return;
    if not lst[1]:
        lst[1] = 0
    if not lst[0]:
        lst[0] = 0
    lst[1] += lst[0]
    if not lst[3] and lst[2]:
        print "Polynomial degree 1"
        solve_first_degree(lst)
        return
    elif lst[3] or lst[2]:
        discrim = (lst[2] * lst[2]) - (4 * lst[3] * lst[1])
        if discrim > 0:
            solve_two_solution(lst, discrim)
        elif discrim == 0:
            solve_one_solution(lst, discrim)
        else:
            solve_complex_solution(lst, discrim)
    else:
        print "We conclude that equation has no solutions"

if __name__ == "__main__":
    test(sys.argv)
