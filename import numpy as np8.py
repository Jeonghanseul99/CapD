import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return  np.sqrt(1-x**2)
start =0
stop = 1

x = np.arange(start,stop,0.0001)
b = min(f(x))
h = max(f(x))
markersize = 1
count = []
y = f(x)
yy = np.arange(b,h,0.0001)

plt.figure(figsize=(20,10)).patch.set_facecolor('w')
for i in range(10000):
  x_p = np.random.choice(x)
  y_p = np.random.choice(yy)


  if start<=x_p<=stop and (0<=y_p<=f(x_p)):
    count.append(1)
    plt.plot(x_p,y_p, "o", color = "red",ms=markersize)
  elif  start<=x_p<=stop and f(x_p)<=y_p<=0:
    count.append(-1)
    plt.plot(x_p,y_p, "o", color = "blue",ms=markersize)
  else:
    count.append(0)
    plt.plot(x_p,y_p, "o", color = "green",ms=markersize)

N_tot = len(count)
N = sum(count)

p =N/N_tot
a = (x[-1]-x[0])*(yy[-1]-yy[0])
A = p*a

print("percentage of point: ",p , "\ntotal area of domain: ",a,"\nIntegration value: ",A )

plt.plot(x,y)
plt.grid()
plt.show()