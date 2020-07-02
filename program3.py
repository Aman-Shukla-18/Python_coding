''' designing a door mate 

input: 5										

output:
------.|.------
---.|..|..|.---
----WELCOME----
---.|..|..|.---
------.|.------

input: 8
output:
----------.|.-----------
-------.|..|..|.--------
----.|..|..|..|..|.-----
-.|..|..|..|..|..|..|.--
--------WELCOME---------
-.|..|..|..|..|..|..|.--
----.|..|..|..|..|.-----
-------.|..|..|.--------
----------.|.-----------
'''




row = input()
row = int(row)
col = row*3
c = ".|."
for i in range(row//2):
    print(((c*i)+c+(c*i)).center(col,"-"))
print("WELCOME".center(col,"-"))
for i in range(row//2):
    print(((c*((row//2)-1-i))+c+(c*((row//2)-1-i))).center(col,"-"))
