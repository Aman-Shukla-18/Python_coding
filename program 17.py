'''
program to print the reversed wordes at there respective position(keeping the amount of spaces same between two words as input by user).
example:

Input:   WE        are developer's

Output:  EW        era s'repoleved

'''

n = list(input())
a = []
string = ''
prev = ''
def reverseWord(a):
    rstring = ''
    for i in range(1,len(a)+1):
        rstring += a[-i]
    return rstring
for i in range(len(n)):
    if(n[i].isalnum()):
        string += n[i]
        prev = n[i]
        if(i == len(n)-1):
            a.append(reverseWord(string))
    elif(n[i] == ' ' and prev.isalnum):
        a.append(reverseWord(string))
        a.append(" ")
        string = ''
        prev = n[i]
    elif(n[i] == ' '):
        a.append(" ")
        prev = [i]

print("".join(a))
