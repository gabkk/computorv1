import sys

def squareroot(x):
    if x<0:
        return 0
    else:
        a = 1
        b = x
    while (abs(a-b)>0):
        a = (a+b)/2
        b = x/a
    return a

if __name__ == "__main__":
    print "test"
    print squareroot(int(sys.argv[1]))
