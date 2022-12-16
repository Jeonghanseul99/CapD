import numpy as np
import random
import matplotlib.pyplot as plt
import math

pi=np.pi
m=1
n=10
v_0=1
theta=np.linspace(0,2*pi,10000)
selected_theta=np.random.choice(theta, 10) #a는 0~2파이 까지 10000개의 난수, b는 a 중 10개 랜덤으로 뽑음
v_x=v_0*np.cos(selected_theta)
v_y=v_0*np.sin(selected_theta)

KE=[0.5*m*(v_x)**2+0.5*m*(v_y)**2]
v_x=[v_0*np.cos(selected_theta)]
v_y=[v_0*np.sin(selected_theta)]
mean_v=[]
Demon=[0.0]



for time in range(30):
    for idx in range(0,n):
        delta=random.uniform(-5.0,5.0)
        Theta=np.random.choice(theta,1)
        v_x[idx]+=delta*np.cos(Theta) 
        v_y[idx]+=delta*np.sin(Theta) 
        mean_v=math.sqrt((np.average(v_x[idx]))**2 + (np.average(v_y[idx]))**2)
        KE_f=0.5*m*(v_x[idx])**2 + 0.5*m*(v_y[idx])**2
        dKE=KE_f[idx]-KE[idx]
        if dKE.all()<0:
            Demon[idx]-=dKE.all()
        else:
            if Demon[idx]>=dKE.all():
                Demon[idx]-=dKE.all()
            else:
                break
    KE.append(KE_f)
    Demon.append(Demon[idx])
print(KE, Demon)
average = 0
for i in range(len(KE)):
    sum = 0
    sum += KE[i]
    average = sum/len(KE) 
print(average)


            
                

