import random as r
length = int(input("Enter Length of the maze: "))
breadth = int(input("Enter Breath of the maze: "))
mazespaces = []
for i in range(breadth):
    currentline=r.choices(range(breadth),list(range(breadth))[::-1])
    print(currentline)