''' A program to find the freqency of all number from 0 to 9

input:

        5 (number of inputs)
        1 2 5 4 5   (5 digits sepertaed by space)


output:
        Occurence of 0 is 0
        Occurence of 1 is 1
        Occurence of 2 is 1
        Occurence of 3 is 0
        Occurence of 4 is 1
        Occurence of 5 is 2
        Occurence of 6 is 0
        Occurence of 7 is 0
        Occurence of 8 is 0
        Occurence of 9 is 0
'''



n = int(input())
a = input().split(' ')
freq = [0,0,0,0,0,0,0,0,0]
for i in range(n):
    a[i] = int(a[i])
    
if len(a)==n:
    
    x = 0
    while x<=9:
    
        for i in a:
            if x == i:
                freq[x] = freq[x]+1
        x+=1
    y = 0    
    for i in freq:
        print('occurence of {}  is  {}  times'.format(y,i))
        y+=1
else:
    print("input format didnot match")
