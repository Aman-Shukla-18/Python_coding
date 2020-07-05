'''Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.


input:
5             --> no of participants(n)
2 3 6 6 5     --> n values seperated with space

output:
5
'''
n = int(input())
ar = input().split(" ")
for i in range(len(ar)):
    ar[i] = int(ar[i])
ar = sorted(ar,reverse = True)
for i in ar:
    if i == ar[0]:
        continue
    else:
        print(i)
        break
