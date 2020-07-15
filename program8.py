'''
(HackerRank -question)
we are given N number of shoe with there sizes and there are X customers with certain shoe size demands
we have to write code to find the amount earned by shopkeeper.

input:
6               number of shoe
6 8 12 4 10 18   shoe sizes
4               number of customers
6 70
4 40             customers request of corespondinig shoe size abd there pricing
6 80
9 70

Output:
110
'''
from collections import Counter
n = int(input())
shoe_size = input().split()
for i in range(n):
    shoe_size[i] = int(shoe_size[i])
noc = int(input())
x = []
for i in range(noc):
    X = input().split()
    X[0] = int(X[0])
    X[1] = int(X[1])
    x.append(tuple(X))
shoe_size = Counter(shoe_size).items()
shoe_size = list(shoe_size)

for i in range(len(shoe_size)):
    shoe_size[i] = list(shoe_size[i])

earning = 0
for i in range(noc):
    for j in range(len(shoe_size)):
        if x[i][0] == shoe_size[j][0] and shoe_size[j][1] > 0:
            earning += x[i][1]
            shoe_size[j][1] -= 1
print(earning)

