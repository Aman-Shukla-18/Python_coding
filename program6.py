'''
A game that prints the entered name using patternprinting .
for eg.:
input name is:: aman
outup:
 *** 
*   *
*   *
*****
*   *
*   *
*   *


**     **
* *   * *
*  * *  *
*   *   *
*       *
*       *
*       *


 *** 
*   *
*   *
*****
*   *
*   *
*   *


**      *
* *     *
*  *    *
*   *   *
*    *  *
*     * *
*      **

'''


def A():
    print(("*"*3).center(5," "))
    for _ in range(6):
        if(_ == 2):
            print(("*" * 5))
        else:
            print(("*")+("*").rjust(4," "))
    print("\n")
def B():
    for i in range(7):
        if i == 0 or i == 3 or i == 6 :
            print("*"*4)
        else:
            print(("*")+("*").rjust(4," "))
    print("\n")
def C():
    for i in range(7):
        if i == 0 or i ==6:
            print(("*"*4).rjust(5," "))
        else:
            print("*")
    print("\n")
def D():

    for i in range(7):
        if i == 0 or i == 6:
            print("*"*4)
        else:
            print(("*")+("*").rjust(4," "))
    print("\n")
def E():
    for i in range(7):
        if i == 0 or i == 3 or i == 6:
            print("*"*5)
        else:
            print("*")
    print("\n")
def F():
    for i in range(7):
        if i == 0 or i == 3:
            print("*" * 5)
        else:
            print("*")
    print("\n")
def G():
    for i in range(7):
        if i == 0 or i == 6:
            print(" "+"*"*4)
        elif i == 3:
            print("*"+("*"*3).rjust(4," "))
        elif i == 4 or i == 5:
            print("*"+("*").rjust(4," "))
        else:
            print("*")
    print("\n")
def H():
    for i in range(7):
        if i == 3:
            print("*"*5)
        else:
            print("*"+("*").rjust(4," "))
    print("\n")
def I():
    for i in range(7):
        if i == 0 or i == 6:
            print("*"*5)
        else:
            print(("*").center(5," "))
    print("\n")
def J():

    for i in range(7):
        if i == 0:
            print("*"*5)
        elif i == 6:
            print(("*").center(3," "))
        elif i == 5:
            print("*"+("*").center(3," "))
        else:
            print(("*").center(5," "))
    print("\n")
def K():

    x = 5
    for i in range(7):
        if i <= 3:
            x-=1
            print("*"+("*").rjust(x," "))
        else:
            x+=1
            print("*"+("*").rjust(x," "))
    print("\n")
def L():
    for i in range(7):

        if i == 6:
            print(("*"*3).rjust(5," "))
        else:
            print(("*").center(5," "))
    print("\n")
def M():

    x = 1
    y = 6
    for i in range(7):
        if i < 3:
            print("*" + ("*").rjust(x, " ")+("*").rjust(y," ")+("*").rjust(x," "))
            x+=1
            y-=2
        elif i == 3:
            print("*"+("*").center(7," ")+"*")
        else:
            print("*"+("*").rjust(8," "))
    print("\n")
def N():
    x = 1
    y = 7
    for i in range(7):
        print("*"+("*").rjust(x," ")+("*").rjust(y," "))
        x+=1
        y-=1
    print("\n")
def O():
    for i in range(7):
        if  i == 0 or i == 6:
            print(("*"*3).center(5," "))
        else:
            print("*"+("*").rjust(4," "))
    print("\n")
def P():
    for i in range(7):
        if i == 0 or i == 3:
            print("*"*4)
        elif i == 1 or i == 2:
            print("*"+("*").rjust(4," "))
        else:
            print("*")
    print("\n")
def Q():
    x = 2
    y = 2
    for i in range(7):
        if i == 0 or i == 5:
            print(("*"*3).center(5," "))
        elif i == 1 or i == 2:
            print("*"+("*").rjust(4," "))
        elif i == 3 or i == 4:
            print("*"+("*").rjust(x," ")+("*").rjust(y," "))
            x+=1
            y-=1
        else:
            print(("*").rjust(6," "))
    print("\n")
def R():
    x = 2
    for i in range(7):
        if i == 0 or i == 3:
            print("*" * 4)
        elif i == 1 or i == 2:
            print("*" + ("*").rjust(4, " "))
        else:
            print("*"+("*").rjust(x," "))
            x+=1
    print("\n")
def S():
    for i in range(7):
        if i == 0 or i == 3 or i == 6:
            print(("*"*3).center(5," "))
        elif i < 3 and i > 0:
            print("*")
        else:
            print(("*").rjust(5," "))
    print("\n")
def T():
    for i in range(7):
        if i == 0:
            print("*"*5)
        else:
            print(("*").center(5," "))
    print("\n")
def U():
    for i in range(7):
        if i == 6:
            print(("*"*3).center(5," " ))
        else:
            print("*"+("*").rjust(4," "))
    print("\n")
def V():

    x = 1
    y = 12
    for i in range(7):
        if i == 6:
            print(("*").rjust(7," "))
        else:
            print(("*").rjust(x," ")+("*").rjust(y," "))
            x+=1
            y-=2
    print("\n")
def W():

    x = 1
    for i in range(7):
        if i < 3:
            print("*"+("*").rjust(8," "))
        elif i == 3:
            print("*"+" "*3+"*"+" "*3+"*")
        else:
            print("*"+("*" + " "*x + "*").center(7," ")+"*")
            x+=2
    print("\n")
def X():

    x = 7
    for i in range(7):
        if i < 3:
            x -= 2
            print(("*" + " " * x + "*").center(7, " "))

        elif i == 3:
            print(("*").center(7," "))
        else:
            print(("*" + " " * x + "*").center(7, " "))
            x+=2
    print("\n")
def Y():
    x = 7
    for i in range(7):
        if i < 3:
            x -= 2
            print(("*" + " " * x + "*").center(7, " "))

        else:
            print(("*").center(7, " "))
    print("\n")
def Z():
    x = 5
    for i in range(7):
        if i == 0 or i == 6:
            print("*"*5)
        else:
            print(("*").rjust(x," "))
            x-=1
    print("\n")
name  = input("Enter your name here:-->")
name = name.upper()
name = list(name)
for i in name:
    if i == 'A':
        A()
    elif i == 'B':
        B()
    elif i == 'C':
        C()
    elif i == 'D':
        D()
    elif i == 'E':
        E()
    elif i == 'F':
        F()
    elif i == 'G':
        G()
    elif i == 'H':
        H()
    elif i == 'I':
        I()
    elif i == 'J':
        J()
    elif i == 'K':
        K()
    elif i == 'L':
        L()
    elif i == 'M':
        M()
    elif i == 'N':
        N()
    elif i == 'O':
        O()
    elif i == 'P':
        P()
    elif i == 'Q':
        Q()
    elif i == 'R':
        R()
    elif i == 'S':
        S()
    elif i == 'T':
        T()
    elif i == 'U':
        U()
    elif i == 'V':
        V()
    elif i == 'W':
        W()
    elif i == 'X':
        X()
    elif i == 'Y':
        Y()
    elif i == 'Z':
        Z()
    else:
        print("Invalid input")



