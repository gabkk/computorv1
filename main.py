

import re
import sys
import string


def test(argv):
    lst = []
    left = []
    left1 = []
    left2 = []
    rigth = []
    rigth1 = []
    rigth2 = []
    argv[1] = argv[1].replace(" ", "") 
    lst = argv[1].split('=')
    pattern_num = r"([^\^][0-9][^X])"#get value in front of X

    pattern = r"([^\^][0-9]+)"
    pattern1 = r"(.[0-9]*X\^1)"
    pattern2 = r"(.[0-9]*X\^2)"
    #pattern = r"(.X\^.)"
    left = re.findall(pattern,lst[0])
    left1 = re.findall(pattern1,lst[0])
    left2 = re.findall(pattern2,lst[0])
    for x in left1:
        left1 = re.findall(pattern, x)
    for x in left2:
        left2 = re.findall(pattern, x)
    newleft = []
    for s in left:
        if not any([s in left1 for left1 in left if s != left1]):
            newleft.append(s)
 #   left = re.sub("X$", 
    right1 = re.findall(pattern1,lst[1])
    right2 = re.findall(pattern2,lst[1])
    print(lst)
    if left1:
        print("display left:")
        print(left)
        print(newleft)
        print(left1)
        print(left2)
    if right1:
        print("display right:")
        print(right1)
    

if __name__ == "__main__":
    test(sys.argv)
