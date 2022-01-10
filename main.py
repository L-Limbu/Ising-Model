import numpy as np


def lattice(size):
    '''Make a array of length size'''
    array = np.random.choice([-1,1], size = (size, size), p = [0.5,0.5])
    return array

