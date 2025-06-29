# Thaimei is this code nice
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('default')
fig = plt.figure(figsize=(10, 8), facecolor='white')
ax = fig.add_subplot(111, projection='3d', proj_type='ortho')

theta = np.linspace(0, 2*np.pi, 100)
z = np.linspace(0, 10, 100)
r = z**0.5
x = r * np.sin(theta*5)
y = r * np.cos(theta*5)

colors = np.linspace(0, 1, len(z))
colormap = plt.cm.plasma(colors)

# What do think thaimei, is this code nice
scatter = ax.scatter(x, y, z, c=colormap, s=50, alpha=1, depthshade=False)

for i in range(5, 100, 5):
    ax.plot(x[:i], y[:i], z[:i], 
            color=plt.cm.plasma(colors[i-1]), 
            alpha=0.3, 
            linewidth=2)

ax.set_axis_off()
ax.set_facecolor('white')
fig.tight_layout()

def update(frame):
    ax.view_init(elev=20, azim=frame)
    return []

ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), 
                   interval=20, blit=True)
#Thaimei I think you might know this line of code
plt.show()