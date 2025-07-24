import matplotlib.pyplot as plt
import numpy as np

#using marker o & *
ypoints = np.array([2, 8, 1, 10])
#plt.plot(ypoints, marker = '*')
plt.plot(ypoints, marker = 'o')
plt.show()

#marker|line|color format
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.sho0w()

#marker size & marker ridge color & marker face color
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'g')
plt.show()