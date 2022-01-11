import numpy as np
#defining the size of the lattice to be 10 particles. So a 10x10x10 cube.
size=30
#defining the amount of iterations to be processed.
iterations = size**2*100

def lattice(size):
    '''Make a array of length size'''
    array = np.random.choice([-1,1], size = (size, size), p = [0.5,0.5])
    return array
initial_lattice = lattice(size)




def FerroMonteProcess(x = initial_lattice, alpha=2.5):
    '''Monte Carlo Algorithm Process with the default value of alpha is 2.5
    x in the arguement is the initial lattice'''
    ferromagnetic = np.array([x])
    for k in range(iterations-1):
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



#For anti-ferromagnetic process

def AntiFerroMonteProcess(x=initial_lattice, alpha=2.5):
    '''Monte Carlo Algorithm Process with the default value of alpha is 2.5
    x in the arguement is the initial lattice'''
    anti_ferromagnetic = np.array([x])
    for k in range(iterations-1):
        a = np.random.randint(size)
        b = np.random.randint(size)
         # spin in the lattice is chosen at random.
        spin = x[a,b] 
       

        ###Finding the spins of neighbours of the chosen partice.
        up = x[(a-1)][b]
        down = x[(a+1) - size][b]
        lhs = x[a][b-1]
        rhs = x[a][(b+1)-size]
        neighbour_S = up + down + lhs + rhs

        grad_E = 2 * spin * neighbour_S

        #Probability to change the chosen particle's spin
        Probability = -grad_E / alpha

        if grad_E > 0:
            spin *= -1
            x[a,b] = spin
        elif np.random.rand() > np.exp(Probability):                        
            spin *= -1
            x[a,b] = spin
        anti_ferromagnetic = np.append(anti_ferromagnetic, [x], axis=0)
    return np.save('./data/anti-ferromagnetic', anti_ferromagnetic)


FerroMonteProcess()
AntiFerroMonteProcess()

