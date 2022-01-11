import numpy as np
import matplotlib.pyplot  as plt
import matplotlib.animation as animation

#loading the data from data directory



anti_ferromagnetic = np.load('./data/zoomed-anti-ferromagnetic.npy')

fig = plt.figure()
frames = []                                                             #empty list to put snaps of lattice in#

for i in range(int(anti_ferromagnetic.shape[0])):   
                   
    Snaps = anti_ferromagnetic[i]
    img = plt.imshow(Snaps, interpolation='none', animated=True)
    frames.append([img])                                                #puts the snaps in the list#
ani = animation.ArtistAnimation(fig, frames, interval=10, blit=True)


plt.show()
plt.close()