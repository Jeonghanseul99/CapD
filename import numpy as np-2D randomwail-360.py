import numpy as np
import random
import matplotlib.pyplot as plt

x_move=[]
y_move=[]

for i in range(10000):
    prob=random.random()
    theta=2*np.pi*prob
    x_situation=np.cos(theta)
    y_situation=np.sin(theta)
    x_move.append(x_situation)
    y_move.append(y_situation)
    
x_positions=np.cumsum(x_move)
y_positions=np.cumsum(y_move)

print(x_positions)
print(y_positions)

plt.plot(x_positions, y_positions, alpha=0.5)
plt.scatter(x_positions[-1],y_positions[-1],color='red')
plt.xlabel('x_position')
plt.ylabel('y_position')
plt.grid()
plt.show()

