'''
we are making a alphabatical rangoli in the followinig patter.
input:
3
output:
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

input:
5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
n = int(input("Enter the value to print the corresponding pattern:"))

def pattern(x):
    a = n + 97
    lst = []
    for i in range(x):
        if i < (x / 2):
            a = a - 1
            lst.append(chr(a))

        else:
            a = a + 1
            lst.append(chr(a))
    return  "-".join(lst)
y = -1
for i in range(2*n-1):

    if i < (2*n-1)/2:
        y+=2
        print(pattern(y).center(4*n-3, "-"))
    else:
        y-=2
        print(pattern(y).center(4*n-3,"-"))


