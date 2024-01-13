import random as r
import Weighted_Distribution as wd

length = int(input("Enter Length of the maze: "))
breadth = int(input("Enter Breath of the maze: "))
mazespaces = []
for i in range(breadth):
    
    mazespaces.append(wd.calc(length))
    print(mazespaces[i])