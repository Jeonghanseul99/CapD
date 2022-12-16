import pylab
import numpy as np
import matplotlib.pyplot as plt

#######################################################################################
# Getting the Hamiltonian right
#######################################################################################
def energy_ising_1d(configuration, J, h):
    num_spins = len(configuration)
    energy = 0.0

    for i in range (num_spins):
        spini   = configuration[i]
        ip1     = (i+1)%num_spins
        spinip1 = configuration[ip1]
        energy  = energy - J*(spini*spinip1) - h*spini
    
    return energy

test_num_spins = 10
test_J         = 1
test_h         = 2

test_configuration_1 = -1*np.ones(test_num_spins)
test_configuration_2 = +1*np.ones(test_num_spins)
test_configuration_3 = +1*np.ones(test_num_spins)

test_configuration_3[::2] = -1

print("Test Config 1:", test_configuration_1)
print("Energy Config 1:", energy_ising_1d(test_configuration_1, test_J, test_h))
print("Expected Energy Config 1:", test_num_spins*(test_h - test_J))
print()
print("Test Config 2:", test_configuration_2)
print("Energy Config 2:", energy_ising_1d(test_configuration_2, test_J, test_h))
print("Expected Energy Config 2:", -test_num_spins*(test_h - test_J))
print()
print("Test Config 3:", test_configuration_3)
print("Energy Config 3:", energy_ising_1d(test_configuration_3, test_J, test_h))
print("Expected Energy Config 3:", test_num_spins*(test_h - test_J))


#######################################################################################################
#Simple (slow) Metropolis Monte Carlo
#######################################################################################################
random_seed=1
np.random.seed(random_seed)

def metropolis_mc_slow(n_steps, n_lattice_sites, beta, J, h, debug=False, save_freq=10):
    configuration = 2*np.random.randint(2, size=n_lattice_sites) -1
    average_spins = []

    if debug is True:
        print("Starting configuration:", configuration)
    
    current_energy = energy_ising_1d(configuration, J, h)

    for i in range(n_steps):
        spin_to_change = np.random.randint(n_lattice_sites)
        configuration[spin_to_change] *= -1
        energy_flip    = energy_ising_1d(configuration, J, h)
        r              = np.random.random()

        if r<min(1,np.exp(-beta*(energy_flip - current_energy))):
            current_energy *= -1
        
        else:
            configuration[spin_to_change] *= -1
        
        average_spin = configuration.mean()

        if 1%save_freq == 0:
            average_spins.append(average_spin)
        
        if debug and i%10 == 0:
            print("%i:"%i, configuration, "Energy:",current_energy, "Spin:", average_spin)
    
    return average_spins

print("High Temperature:")
average_spins = metropolis_mc_slow(n_steps = 100, n_lattice_sites = 10, beta = 0.1, J = 1, h = 2, debug=True)

print("Low Twmperature:")
average_spins = metropolis_mc_slow(n_steps= 200, n_lattice_sites=10, beta=1, J=1, h=2, debug=True)

#####################################################################################################################
# Faster Metropolis Monte Carlo
#####################################################################################################################
random_seed =1
np.random.seed(random_seed)

def energy_difference(J, h, si, sleft, sright):
    dE= 2*h*si+2*J*si*(sleft + sright)
    return dE

def metropolis_mc_fast(n_steps, n_lattice_sites, beta, J, h, debug=False, save_freq=10):
    configuration = 2*np.random.randint(2, size = n_lattice_sites) - 1
    average_spins = []

    if debug is True:
        print("Starting configuration:", configuration)

    current_energy = energy_ising_1d(configuration, J, h)
    for i in range(n_steps):
        spin_to_change= np.random.randint(n_lattice_sites)
        si            = configuration[spin_to_change]
        sright        = configuration[(spin_to_change +1)%n_lattice_sites]
        sleft         = configuration[(spin_to_change -1)%n_lattice_sites]

        dE            = energy_difference(J, h, si, sleft, sright)

        r = np.random.random()

        if r<min(1,np.exp(-beta*(dE))):
            configuration[spin_to_change] *= -1
            current_energy += dE
        else: 
            pass

        average_spin = configuration.mean()

        if i%save_freq ==0:
            average_spins.append(average_spin)
        
        if debug and i%10==0:
            print("%i: "%i, configuration, "Energy:", current_energy, "Spin:", average_spin)
    
    return average_spins

print("High temperature:")
average_spins = metropolis_mc_fast(n_steps=100, n_lattice_sites = 10, beta = 0.1, J=1, h=2, debug=True)

print("Low temperature:")
average_spins = metropolis_mc_fast(n_steps = 100, n_lattice_sites =10, beta=1, J=1, h=2, debug=True)


########################################################################################################################
#Testing for one case
########################################################################################################################
def bin_average(bins):
    return (bins[1:] + bins[:-1])/2

test_n_lattice_sites = 100
test_beta            = 0.2
test_J               = 1
test_h               = 0
test_n_steps         = test_n_lattice_sites*100

average_spins   =   metropolis_mc_fast(test_n_steps, test_n_lattice_sites, test_beta, test_J, test_h)

plt.plot(average_spins)
plt.ylabel("$m$")
plt.xlabel("MC Step")
plt.title("$||beta=%.2f,$J=%.2f,$h=%.2f$"%(test_beta, test_J, test_h))

spin_hist, spin_bins = np.histogram(average_spins[len(average_spins)//2:], bins=20)
plt.figure()
plt.plot(bin_average(spin_bins),spin_hist)
plt.xlabel('$m$')
plt.ylabel("$P(m)$")

plt.show()
