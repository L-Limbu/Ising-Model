import numpy as np
import time
#defining the size of the lattice to be 10 particles. So a 10x10x10 cube.
size=100
#defining the amount of iterations to be processed.
iterations = 1000

def lattice(size):
    '''Make a array of length size'''
    array = np.random.choice([-1,1], size = (size, size), p = [0.5,0.5])
    return array
initial_lattice = lattice(size)




def FerroMonteProcess(x = initial_lattice, alpha=2.5):
    '''Monte Carlo Algorithm Process with the default value of alpha is 2.5
    x in the arguement is the initial lattice'''
    ferromagnetic = np.array([x])
    for k in range(iterations):
        #this second iteration is used to only save data space by only appending data after this loop.
        for p in range(size**2):
            a = np.random.randint(size)
            b = np.random.randint(size)
            spin = x[a,b] 
            # spin in the lattice is chosen at random.

            ###Finding the spins of neighbours of the chosen partice.
            up = x[(a-1)][b]
            down = x[(a+1) - size][b]
            lhs = x[a][b-1]
            rhs = x[a][(b+1)-size]
            neighbour_S = up + down + lhs + rhs

            grad_E = 2 * spin * neighbour_S

            #Probability to change the chosen particle's spin
            Probability = -grad_E / alpha

            
            if grad_E < 0:
                
        
                x[a,b] *= -1
                
            elif np.random.rand() < np.exp(Probability):                        
                
            
                x[a,b] *= -1

        ferromagnetic = np.append(ferromagnetic, [x], axis=0)
    return np.save('./data/ferromagnetic', ferromagnetic)




start = time.perf_counter()
FerroMonteProcess()

end = time.perf_counter()
print(f'Simulation took {end-start:0.4f} seconds')


