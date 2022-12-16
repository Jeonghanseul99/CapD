import numpy as np
import matplotlib.pyplot as plt

particles = []
v_0       = 1.0
N         = 10
demon     = 0


for i in range(100):
    def KE(particle):
        return (np.linalg.norm(particle,2))**2/2

    Demon=[]
####################################################################################
#	initial value
####################################################################################
    for i in range(N):
        angle    =   np.random.rand()*2*np.pi                       ####xy평면 파이
        theta    =   np.random.rand()*2*np.pi                       ####Z와 평면 사이의 값
        particle =   np.array([v_0*np.sin(theta)*np.cos(angle), v_0*np.sin(theta)*np.sin(angle), v_0*np.cos(theta)])
        particles.append(particle)



####################################################################################
#	change velocity
####################################################################################
    for particle in particles:
        KE_i    =   KE(particle)
        delta   =   np.random.rand()*10-5
        dVel    =   np.array([delta*np.sin(theta)*np.cos(angle), delta*np.sin(theta)*np.sin(angle), delta*np.cos(theta)])
        KE_f    =   KE(particle-dVel)

        temp    =   particle.copy()
        dKE     =   KE_f - KE_i

        if dKE  <= 0:
            particle +=  dVel
            demon    -=  dKE
        else:
            if demon - dKE  >= 0:
                particle  +=  dVel
                demon     -=  dKE


        Demon.append(demon)
    #print(f"{temp[0]:.4f} -> {particle[0]:.4f}|t{temp[1]:.4f} -> {particle[1]:.4f}|t{temp[2]:.4f} -> {particle[2]:.4f}|tdKE= {dKE:.2f}|tdemon = {demon:.2f}")
    #print(KE(particle))
    #print(demon)
print(Demon)
plt.hist(Demon)
plt.show()
