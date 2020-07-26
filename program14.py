''' Task: take some integer input obtain there binary in 32 bit format
reverse the bits and find out the decimal of that binary
input: 10 5 4 2
output: 1342177280,2684354560,536870912,1073741824
'''

def dec(string):
    lst = list(string)
    decimal = 0
    for i in range(len(lst)):
        if lst[len(lst)-i-1] == '1':
            decimal = decimal+(2**i)
    return decimal

decimals = list(map(int,input().split()))
output = []
for i in decimals:
    binary = bin(i)[2:]
    binary = '0'*(32-len(binary))+ binary
    binary = binary[::-1]
    output.append(dec(binary))
print(output)
