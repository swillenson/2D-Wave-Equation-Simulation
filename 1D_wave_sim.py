import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from numba import jit

L = 1.0 #string length
t = 1.0 #time total
dt = 0.005 #time step
c = 1.0 #speed of wave
v0 = 5.0 #initial velocity

#guitar string
plucked_x = 0.2
plucked_width = 0.1
damping_factor = 0.01

#make discrete
nx = 200
nt = int(t / dt)

dx = L / (nx - 1)
x = np.linspace(0, L, nx)

#initial conditions
#guitar sim
u0 = np.exp(-((x - plucked_x) / plucked_width)**2)  # Gaussian pluck
u1 = u0.copy() + 0.01 * np.sin(np.pi * x / L)  # Adding a sinusoidal initial velocity

#normal sim
# u0 = np.sin(np.pi * x) #wave shape
# # u0 = np.linspace(0,0,nx )
# u1 = u0.copy() + v0 * dt

#plotting
fig, ax = plt.subplots()
line, = ax.plot(x, u1)
ax.set_title('1D Wave Eq')
ax.set_xlabel('Position')
ax.set_ylabel('Amplitude')
y_lim = 4
ax.set_ylim(-y_lim,y_lim)

#create values to be animated, faster using numba
@jit(nopython = True)
def time_step(u0, u1, damping_factor, c, dt, dx):
    damping_term = damping_factor * (u1[1:-1] - 2 * u1[1:-1] + u1[:-2])
    u2 = 2 * (1 - c**2 * dt**2 / dx**2) * u1[1:-1] - u0[1:-1] +\
        c**2 * dt**2 / dx**2 * (u1[:-2] + u1[2:]) - damping_term
    u0 = u1.copy()
    u1[1:-1] = u2
    return u0, u1

def animate(frame):
    global u0, u1
    u0, u1 = time_step(u0, u1, damping_factor, c, dt, dx)
    line.set_ydata(u1)
    return line,

#animate
animation = FuncAnimation(fig, animate, frames = range(nt), blit = True)
plt.show()