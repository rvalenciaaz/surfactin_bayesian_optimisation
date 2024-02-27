import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from scipy.stats import qmc
import numpy as np

# Generate Sobol sequence points
sampler = qmc.Sobol(d=3, scramble=False)
sample = sampler.random_base2(m=8)  # 2^m points

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the Sobol points
ax.scatter(sample[:, 0], sample[:, 1], sample[:, 2], marker='o')

# Setting the labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Initialization function for the animation
def init():
    ax.scatter(sample[:, 0], sample[:, 1], sample[:, 2], marker='o')
    return fig,

# Animation function which updates the figure
def animate(i):
    ax.view_init(elev=10., azim=i)
    return fig,

# Creating the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)

# Save the animation as GIF
ani.save('sobol_3d_animation.gif', writer='imagemagick', fps=30)
