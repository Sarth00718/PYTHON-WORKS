import matplotlib.pyplot as plt
import numpy as np

'''
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
#plt.barh(x.y)   --> horizontal bar chat
plt.show()'''

# color, width and height

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
#plt.bar(x, y, width = 0.1)
plt.barh(x, y, height = 0.1, color='pink')
plt.show()