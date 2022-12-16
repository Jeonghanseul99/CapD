import numpy as np
import matplotlib.pyplot as plt
import numpy.random as random

x_move=[]
y_move=[]
x_locations=[]
y_locations=[]
numbers=[1,2,3,4]

for j in range(1000):
    for i in range(1000):
        prob=random. choice(numbers,1,p=[0.25,0.25,0.25,0.25])
        if prob==1:
            x_move.append(1)
            y_move.append(0)
        elif prob==2:
            x_move.append(-1)
            y_move.append(0)
        elif prob==3:
            x_move.append(0)
            y_move.append(1)
        else:
            x_move.append(0)
            y_move.append(-1)
    x_positions=np.cumsum(x_move)
    y_positions=np.cumsum(y_move)
    x_last=x_positions[-1]
    y_last=y_positions[-1]
    x_locations.append(x_last)
    y_locations.append(y_last)

plt.hist(x_locations,bins=15,rwidth=0.8)
plt.xlabel('the positions which random walker stands on x-axis')
plt.ylabel('frquency')
plt.show()

plt.hist(y_locations,bins=15,rwidth=0.8)
plt.xlabel('the positions which random walker stands on y-axis')
plt.ylabel('frequency')
plt.show()