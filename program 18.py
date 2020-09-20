
'''
Minions game

this is a game in which there will bw two players and they will be given a string
to make different strings using the letters of given string but there is a twist
player1 will be making words starting with consonant and
player2 will be making words starting with vowels

example
input:
        Dog
Output:
        player1 won
explanation
        dog =['D','g','o',  'go', 'gD', 'og', 'Do', 'Dg', 'oD','Dgo', 'goD', 'gDo', 'ogD', 'oDg', 'Dog']

player1 can make D g go gD Do Dg Dgo goD gDo Dog
player2 can make o og oD ogD oDg
'''


from itertools import permutations
mainString = input()
player1 = input("Enter the name of first player: ")
player2 = input("Enter the name of second player: ")
print("{} will be making words starting with consonant".format(player1))
print("{} will be making words starting with vowels".format(player2))
a = []
player1point = 0
player2point = 0
for i in range(1,len(mainString)+1):
    x = permutations(mainString,i)
    for i in x:
        a.append("".join(i))
a = list(set(a))
for i in a:
    if(i.isalpha()):
        if(i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u' or i[0] == 'A' or i[0] == 'E' or i[0] == 'I' or i[0] == 'O' or i[0] == 'U'):
            player2point += 1
        else:
            player1point += 1
print("{} scores {}".format(player1,player1point))
print("{} scores {}".format(player2,player2point))
if (player1point > player2point):
    print("{} Won".format(player1))
elif(player1point < player2point):
    print("{} Won".format(player2))
else:
    print("Its a draw")
print(a)
