import random
import math
with open("./graph.txt",'w') as f:
    n = 50
    size = 5
    angle = math.pi * 2 / n

    f.write(f"{n}\n")
    for i in range(n):
        # theta = random.normalvariate(angle*i,angle)
        theta = angle*i
        dis = random.normalvariate(size,1)
        x = math.cos(theta)*dis
        y = math.sin(theta)*dis
        f.write(f"{x}\n{y}\n")
        