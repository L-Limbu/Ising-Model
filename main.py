import numpy as np
#defining the size of the lattice to be 10 particles. So a 10x10x10 cube.
size=10
#defining the amount of iterations to be processed.
iterations = 1000

def lattice(size):
    '''Make a array of length size'''
    array = np.random.choice([-1,1], size = (size, size), p = [0.5,0.5])
    return array
initial_lattice = lattice(size)




def FerroMonteProcess(x, alpha=1.8):
    '''Monte Carlo Algorithm Process with the default value of alpha is 1.8
    x in the arguement is the initial lattice'''
    ferromagnetic = []
    for k in range(iterations):
        a = np.random.randint(size)
        b = np.random.randint(size)
        spin = x[a,b] 
        # spin in the lattice is chosen at random.

        ###Finding the spins of neighbours of the chosen partice.
        up = x[b-1][a]
        down = x[(b+1) - size][a]
        lhs = x[b][a-1]
        rhs = x[b][(a+1)-size]
        neighbour_S = up + down + lhs + rhs

        grad_E = 2 * spin * neighbour_S

        #Probability to change the chosen particle's spin
        Probability = -grad_E / alpha

        if grad_E <= 0:
            spin *= -1
            x[a,b] = spin
        elif np.random.rand() <= np.exp(Probability):                        
            spin *= -1
            x[a,b] = spin
        ferromagnetic.append(x)
    return np.save('./data/ferromagnetic', x)



#For anti-ferromagnetic process

def AntiFerroMonteProcess(x, alpha=1.8):
    '''Monte Carlo Algorithm Process with the default value of alpha is 1.8
    x in the arguement is the initial lattice'''
    anti_ferromagnetic = []
    for k in range(iterations):
        a = np.random.randint(size)
        b = np.random.randint(size)
        spin = x[a,b] 
        # spin in the lattice is chosen at random.

        ###Finding the spins of neighbours of the chosen partice.
        up = x[b-1][a]
        down = x[(b+1) - size][a]
        lhs = x[b][a-1]
        rhs = x[b][(a+1)-size]
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
        anti_ferromagnetic.append(x)
    return np.save('./data/anti-ferromagnetic', anti_ferromagnetic)


FerroMonteProcess(initial_lattice)
AntiFerroMonteProcess(initial_lattice)