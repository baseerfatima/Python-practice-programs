def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print(" ")
def pattern2(n):
    for i in range(n):
        for j in range(0,i+1):
            print('*', end="")
        print("")
def p3(n):
    for i in range(n+1):
        for j in range(n-i):
              print('*', end="")
        print("")
def p4(n):
    for i in range(n):
        for j in range(0,i+1):
            print(j+1," ",end="")
        print("")
def p5(n):
    for i in range(2*n):
        if i>n:
            c=2*n-i
        else:
            c=i
        for j in range(c):
            print("*",end='')
        print(" ")
def p6(n):
    for i in range(n):
        space=n-i
        print(" "*space, end="")
        for j in range(i):
            space=n-i
            print( "*", end="")
        print("")
p6(4)
    