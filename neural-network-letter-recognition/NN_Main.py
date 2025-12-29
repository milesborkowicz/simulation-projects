from matplotlib import pyplot as plt
from math import *
from random import *
import numpy as np
from random import *
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

# Parameters
N = 20
J = 1.0
T = 1.0

# Calculate the energy of the lattice
def calculate_energy(lattice):
    energy = 0
    for i in range(N):
        for j in range(N):
            # Interaction with top neighbor
            energy += -J * lattice[i, j] * lattice[(i + 1) % N, j]
            # Interaction with bottom neighbor
            energy += -J * lattice[i, j] * lattice[(i - 1) % N, j]
            # Interaction with right neighbor
            energy += -J * lattice[i, j] * lattice[i, (j + 1) % N]
            # Interaction with left neighbor
            energy += -J * lattice[i, j] * lattice[i, (j - 1) % N]
            # Interaction with every other spin
            for k in range(N):
                for l in range(N):
                    if (k, l) != (i, j):
                        energy += -J * lattice[i, j] * lattice[k, l]
    return energy / 2  # Divide by 2 to avoid double counting
    
def letterA():
    return np.array([
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1],
        [-1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1],
        [-1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1],
        [-1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
        [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1]
    ])

# energyA = calculate_energy(letterA())

def letterB():
    return np.array([
        [-1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1,  1,  1, -1, -1, -1, -1, -1, -1, -1,  1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
        [-1,  1,  1, -1, -1, -1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
        [-1,  1,  1, -1, -1, -1, -1, -1, -1, -1, -1,  1,  1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]
    ])

# calculate_energy(letterB())

def letterC():
    return np.array([
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1]
    ])

# calculate_energy(letterC())

# Initialize a random letter with [prob] pixels out of place.
def initialize_lattice(N, prob):
    test = randint(1,3)
    if test == 1:
        lattice = letterA()
        let = 'A'
    if test == 2:
        lattice = letterB()
        let = 'B'
    if test == 3:
        lattice = letterC()
        let = 'C'
    print('Letter:',let)
    for i in range(0,19):
        for j in range(0,19):
            rand = uniform(0.0,1.0)
            if rand <= prob:
                lattice[i, j] *= -1
            j += 1
        rand = uniform(0.0,1.0)
        if rand <= prob:
            lattice[i, j] *= -1
    return lattice

# Calculate the Hamming distance
def hamming_dist(letter1,letter2):
    return np.sum(letter1 != letter2)

# Determine what letter it is
def nearest_letter(lattice):
    distA = hamming_dist(lattice,letterA())
    distB = hamming_dist(lattice,letterB())
    distC = hamming_dist(lattice,letterC())
    # print(distA,distB,distC)
    dists = [distA,distB,distC]
    mindist = min(dists)
    if mindist == distA:
        guess = 1
        # print('Guess: A')
        return letterA()
    if mindist == distB:
        guess = 2
        # print('Guess: B')
        return letterB()
    if mindist == distC:
        guess = 3
        # print('Guess: C')
        return letterC()

def monte_carlo_step(lattice, letter, temperature):
    i = randint(0,19)
    j = randint(0,19)
    
    new_lattice = lattice.copy()
    new_lattice[i, j] *= -1
    
    distold = hamming_dist(lattice,letter)
    distnew = hamming_dist(new_lattice,letter)
    
    if distnew < distold:
        return new_lattice
    else:
        return lattice
    
# Function to plot the lattice configuration
def plot_lattice(lattice):
    plt.figure()
    plt.imshow(lattice,cmap='binary',interpolation='none')
    # plt.colorbar()
    plt.show()
    
# Find the steps to resolve the lattice vs. randomization probability 
def steps_v_prob(prob):
    lattice = initialize_lattice(N, prob)
    # plot_lattice(lattice)
    letter = nearest_letter(lattice)
    
    count = 0
    
    # Monte Carlo Step
    while hamming_dist(lattice,letter) != 0:
        lattice = monte_carlo_step(lattice, letter, T)
        count += 1
        # if count % 500 == 0:
        #     plot_lattice(lattice)
    # plot_lattice(lattice)
    # print('Steps:',count)
    return count

# For plotting steps_v_prob
def steps_resolve_plot():
    prob = 0.005
    
    prob_ = []
    steps_ = []
    meansteps_ = []
    
    while prob <= 1:
        
        count = 0
        
        count = steps_v_prob(prob)
        prob_.append(prob)
        steps_.append(count)
        meansteps_.append(sum(steps_)/len(steps_))
        
        prob += 0.005
    
    plt.figure()
    plt.title('Steps to Resolve vs. Randomization Probability')
    plt.xlabel('Randomization Probability')
    plt.ylabel('Steps to Resolve')
    plt.plot(prob_,steps_,'k .',label='Steps')
    plt.plot(prob_,meansteps_,'b--',label='Moving Average')
    plt.legend()
    plt.show()
    
def hamming_v_step():
    prob = 0.1
    lattice = initialize_lattice(N, prob)
    plot_lattice(lattice)
    letter = nearest_letter(lattice)
    
    count = 0
    
    dist_ = []
    step_ = []
    
    # Monte Carlo Step
    while hamming_dist(lattice,letter) != 0:
        lattice = monte_carlo_step(lattice, letter, T)
        dist_.append(hamming_dist(lattice,letter))
        step_.append(count)
        count += 1
        # if count % 500 == 0:
        #     plot_lattice(lattice)
    plot_lattice(lattice)
    print('Steps:',count)
    
    plt.figure()
    plt.title('Hamming Distance vs. Monte Carlo Steps')
    plt.xlabel('Steps')
    plt.ylabel('Hamming Distance')
    plt.plot(step_,dist_)
    
def initial_letter(prob):
    test = randint(1,3)
    if test == 1:
        lattice = letterA()
        let = 1
    if test == 2:
        lattice = letterB()
        let = 2
    if test == 3:
        lattice = letterC()
        let = 3
    # print('Letter:',let)
    for i in range(0,19):
        for j in range(0,19):
            rand = uniform(0.0,1.0)
            if rand <= prob:
                lattice[i, j] *= -1
            j += 1
        rand = uniform(0.0,1.0)
        if rand <= prob:
            lattice[i, j] *= -1
    return lattice, let

def guess_(lattice):
    distA = hamming_dist(lattice,letterA())
    distB = hamming_dist(lattice,letterB())
    distC = hamming_dist(lattice,letterC())
    # print(distA,distB,distC)
    dists = [distA,distB,distC]
    mindist = min(dists)
    if mindist == distA:
        # guess = 1
        # print('Guess: A')
        return 1
    if mindist == distB:
        # guess = 2
        # print('Guess: B')
        return 2
    if mindist == distC:
        # guess = 3
        # print('Guess: C')
        return 3

def acc():
    prob = 0.01
    acc_ = []
    prob_ = []
    
    for i in range(0,100):
        acc = 0
        for j in range(0,1000):
            lattice, letter = initial_letter(prob)
            # print(letter)
            # plot_lattice(lattice)
            guess = guess_(lattice)
            if guess == letter:
                acc += 1
            j += 1
        acc_.append(acc)
        prob_.append(prob)
        prob += 0.01
        i += 1
    plt.figure()
    plt.title('Network Accuracy vs. Randomization Probability')
    plt.xlabel('Randomization Probability')
    plt.ylabel('Guesses right per 1000 trials')
    plt.plot(prob_,acc_,'k-')
    
def animate():
    prob = 0.5
    lattice = initialize_lattice(N, prob)
    letter = nearest_letter(lattice)
    
    fig, ax = plt.subplots(figsize=(10,10))
    
    im = ax.imshow(lattice, cmap='binary', interpolation='none')

    def update(frame):
        nonlocal lattice
        lattice = monte_carlo_step(lattice, letter, T)
        im.set_array(lattice)
        return im,

    ani = FuncAnimation(fig, update, frames=range(3500), interval=1, blit=True, repeat=False)
    
    plt.plot(ani)
    plt.draw()
    plt.show()
    
def energy_v_hamming():
    prob = 0.01
    
    energy_ = []
    hamming_ = []
    
    for i in range(1,100):
        lattice = letterA()
        for i in range(0,19):
            for j in range(0,19):
                rand = uniform(0.0,1.0)
                if rand <= prob:
                    lattice[i, j] *= -1
                j += 1
            rand = uniform(0.0,1.0)
            if rand <= prob:
                lattice[i, j] *= -1
        
        letter = letterA()
        
        energylattice = calculate_energy(lattice)
        energyletter = calculate_energy(letter)
        
        hamming_.append(hamming_dist(lattice,letter))
        energy_.append(abs(energylattice-energyletter))
        
        prob += 0.01
        i += 1
    
    plt.figure()
    plt.title('Energy vs. Hamming Distance: Letter A')
    plt.xlabel('Hamming Distance')
    plt.ylabel('Energy Difference')
    plt.plot(hamming_,energy_,'k o')
    
    prob = 0.01
    
    energy_ = []
    hamming_ = []
    
    for i in range(1,100):
        lattice = letterB()
        for i in range(0,19):
            for j in range(0,19):
                rand = uniform(0.0,1.0)
                if rand <= prob:
                    lattice[i, j] *= -1
                j += 1
            rand = uniform(0.0,1.0)
            if rand <= prob:
                lattice[i, j] *= -1
        
        letter = letterB()
        
        energylattice = calculate_energy(lattice)
        energyletter = calculate_energy(letter)
        
        hamming_.append(hamming_dist(lattice,letter))
        energy_.append(abs(energylattice-energyletter))
        
        prob += 0.01
        i += 1
    
    plt.figure()
    plt.title('Energy vs. Hamming Distance: Letter B')
    plt.xlabel('Hamming Distance')
    plt.ylabel('Energy Difference')
    plt.plot(hamming_,energy_,'k o')
    
    prob = 0.01
    
    energy_ = []
    hamming_ = []
    
    for i in range(1,100):
        lattice = letterC()
        for i in range(0,19):
            for j in range(0,19):
                rand = uniform(0.0,1.0)
                if rand <= prob:
                    lattice[i, j] *= -1
                j += 1
            rand = uniform(0.0,1.0)
            if rand <= prob:
                lattice[i, j] *= -1
        
        letter = letterC()
        
        energylattice = calculate_energy(lattice)
        energyletter = calculate_energy(letter)
        
        hamming_.append(hamming_dist(lattice,letter))
        energy_.append(abs(energylattice-energyletter))
        
        prob += 0.01
        i += 1
    
    plt.figure()
    plt.title('Energy vs. Hamming Distance: Letter C')
    plt.xlabel('Hamming Distance')
    plt.ylabel('Energy Difference')
    plt.plot(hamming_,energy_,'k o')
    
def hamming_to_energy(dist, letter):
    if letter == 1:
        return -0.35*(dist-200)**2 + 13500
    if letter == 2:
        return -0.35*(dist-200)**2 + 11500
    if letter == 3:
        return -0.85*(dist-200)**2 + 30000

def test():
    lattice = initialize_lattice(N,0.8)
    plot_lattice(lattice)
    
def energy_v_step():
    prob = 0.3
    lattice = initialize_lattice(N, prob)
    plot_lattice(lattice)
    letter = nearest_letter(lattice)
    guess = guess_(lattice)
    
    count = 0
    
    energy_ = []
    step_ = []
    
    # Monte Carlo Step
    while hamming_dist(lattice,letter) != 0:
        lattice = monte_carlo_step(lattice, letter, T)
        dist = hamming_dist(lattice,letter)
        energy_.append(hamming_to_energy(dist,guess))
        step_.append(count)
        count += 1
        # if count % 500 == 0:
        #     plot_lattice(lattice)
    plot_lattice(lattice)
    print('Steps:',count)
    
    plt.figure()
    plt.title('Energy vs. Monte Carlo Steps')
    plt.xlabel('Steps')
    plt.ylabel('Energy')
    plt.plot(step_,energy_,'k-')

# Main function to run the simulation
def main():
    # steps_resolve_plot()
    # hamming_v_step()
    # acc()
    # animate()
    # energy_v_hamming()
    # test()
    # energy_v_step()

main()