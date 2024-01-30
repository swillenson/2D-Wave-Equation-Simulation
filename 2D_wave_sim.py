import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

size = 100 #grid size
t = 100 #time total
dt = 1 #time step
c = 1 #speed of wave

x = np.linspace(0, 1, size)
y = np.linspace(0, 1, size)
z = np.random.rand(size, size)
X, Y = np.meshgrid(x, y)


fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.plot_surface(x, y, z)
plt.show()