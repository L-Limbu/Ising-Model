import numpy as np
import matplotlib.pyplot  as plt
import matplotlib.animation as animation

#loading the data from data directory


ferromagnetic = np.load('./data/ferromagnetic.npy')


fig = plt.figure()
frames = []                                                             #empty list to put snaps of lattice in#

for i in range(int(ferromagnetic.shape[0])):   
                   
    Snaps = ferromagnetic[i]
    img = plt.imshow(Snaps, interpolation='none', animated=True)
    frames.append([img])                                                #puts the snaps in the list#
ani = animation.ArtistAnimation(fig, frames, interval=1, blit=True)


plt.show()
plt.close()
