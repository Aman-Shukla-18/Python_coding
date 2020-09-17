#A program to find all the possible combination of stiring from a given string upto certain pair.(anagrams)
#       input:
#           abc
#       output:
#           a
#           b
#           c
#           ab
#           bc
#           ac
#           abc
from itertools import combinations

string = input()
for i in range(1,len(string)+1):
    x = combinations(string, i)
    for j in x:
        print("".join(j))

