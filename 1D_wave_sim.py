import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

L = 1.0 #string length
t = 1.0 #time total
dt = 0.01 #time step
c = 1.0 #speed of wave
v0 = 1.0 #initial velocity

#make discrete
nx = 100
nt = int(t / dt)

dx = L / (nx - 1)
x = np.linspace(0, L, nx)

#initial conditions

u0 = np.sin(2 * np.pi * x) #wave shape
u1 = u0.copy() + v0 * dt

#plotting
fig, ax = plt.subplots()
line, = ax.plot(x, u1)
ax.set_title('1D Wave Eq')
ax.set_xlabel('Position')
ax.set_ylabel('Amplitude')

def time_step(frame):
    global u0, u1
    u2 = 2 * (1 - c**2 * dt**2 / dx**2) * u1[1:-1] - u0[1:-1] +\
        c**2 * dt**2 / dx**2 * (u1[:-2] + u1[2:])
    u0 = u1.copy()
    u1[1:-1] = u2
    line.set_ydata(u1)
    return line,

#animate
animation = FuncAnimation(fig, time_step, frames = range(nt), blit = True)
plt.show()