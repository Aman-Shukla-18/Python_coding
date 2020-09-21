'''
There is a room with n bulbs, numbered from 0 to n-1, arranged in a row from left to right. Initially all the bulbs are turned off.
Your task is to obtain the configuration represented by target where target[i] is '1' if the i-th bulb is turned on and is '0' if it is turned off.
You have a switch to flip the state of the bulb, a flip operation is defined as follows:
Choose any bulb (index i) of your current configuration.
Flip each bulb from index i to n-1.
When any bulb is flipped it means that if it is 0 it changes to 1 and if it is 1 it changes to 0.
Return the minimum number of flips required to form target.

Example 1:
Input: target = "10111"
Output: 3
Explanation: Initial configuration "00000".
flip from the third bulb:  "00000" -> "00111"
flip from the first bulb:  "00111" -> "11000"
flip from the second bulb:  "11000" -> "10111"
We need at least 3 flip operations to form target.
Example 2:
Input: target = "101"
Output: 3
Explanation: "000" -> "111" -> "100" -> "101".
Example 3:
Input: target = "00000"
Output: 0
Example 4:
Input: target = "001011101"
Output: 5
'''
target = list(map(int,list(input())))
ourstring = []
counting = 0
def flip(x):
    if(x == 0):
        return 1
    elif(x == 1):
        return 0
    else:
        print("Invalid Input")

for _ in range(len(target)):
    ourstring.append(0)
for i in range(len(target)):
    if(target[i] == ourstring[i]):
        continue
    else:
        counting += 1
        for j in range(len(target)-i):
            ourstring[i+j] = flip(ourstring[i+j])

print(counting)
