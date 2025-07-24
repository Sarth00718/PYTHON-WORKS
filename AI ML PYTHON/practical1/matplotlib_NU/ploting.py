import matplotlib.pyplot as plt
import numpy as np

# using line
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()       

# using point
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

#multiple plots
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

#take default x plot
ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()





