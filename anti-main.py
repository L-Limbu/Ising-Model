import numpy as np
import time
#defining the size of the lattice. So it produces a size x size x size cube.
size=500
#defining the amount of iterations to be processed.
iterations = 1000

def lattice(size):
    '''Make a array of length size'''
    array = np.random.choice([-1,1], size = (size, size), p = [0.5,0.5])
    return array
initial_lattice = lattice(size)

#For anti-ferromagnetic process

def AntiFerroMonteProcess(x=initial_lattice, alpha=1):
    '''Monte Carlo Algorithm Process with the default value of alpha is 1
    x in the arguement is the initial lattice'''
    anti_ferromagnetic = np.array([x])
    for k in range(iterations):
        for p in range(size**2):
            a = np.random.randint(size)
            b = np.random.randint(size)
            # spin in the lattice is chosen at random.
            spin = x[a,b] 
        

            ###Finding the spins of neighbours of the chosen partice.
            up = x[(a-1)%size][b]
            down = x[(a+1)%size][b]
            lhs = x[a][(b-1%size)]
            rhs = x[a][(b+1)%size]
            neighbour_S = up + down + lhs + rhs

            grad_E = 2 * spin * neighbour_S

            #Probability to change the chosen particle's spin
            Probability = -grad_E / alpha

            if grad_E >= 0:
                spin *= -1
                x[a,b] = spin
            elif np.random.rand() >= np.exp(Probability):                        
                spin *= -1
                x[a,b] = spin
        anti_ferromagnetic = np.append(anti_ferromagnetic, [x], axis=0)
    return np.save('./data/anti-ferromagnetic', anti_ferromagnetic)


start = time.perf_counter()
AntiFerroMonteProcess()
end = time.perf_counter()
print(f'Simulation took {end-start:0.4f} seconds')
