#A program to find all the possible combination of stiring from a given string upto certain pair.
#       input:
#           abc 3
#       output:
#           a
#           b
#           c
#           ab
#           bc
#           ac
#           abc
from itertools import combinations

string, possibility = input().split()
possibility = int(possibility)
for i in range(1,possibility+1):
    x = combinations(string, i)
    for i in x:
        print("".join(i))
