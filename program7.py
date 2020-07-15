'''
this code will capitalize the first letter of first name, middle and last name.
input:
aman shukla

output:
Aman Shukla
'''
name = input().split()
for i in range(len(name)):
    name[i] = name[i].capitalize()
print(" ".join(name))
