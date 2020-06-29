''' You are given a three integer X,Y and Z representing the dimensions of a cuboid along with an integer N. You have to print a list of all possible coordinates given by(i,j,k)
on a 3D grid where the sum of i+j+k is not eqaul to N.


input: input of x,y,z and N all in sperate line

eg:   1
      1
      1
      2
output: [[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,1,1]]

'''

x = int(input())
y = int(input())
z = int(input())
n = int(input())
ar = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
           if((i+j+k) != n):
            ar.append([i,j,k])
print(ar)

