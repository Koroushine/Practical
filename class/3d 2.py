import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Optimized settings
plt.rcParams['animation.ffmpeg_path'] = 'ffmpeg'  # Ensure ffmpeg is installed if saving
plt.rcParams['animation.html'] = 'html5'  # For better display in notebooks
plt.style.use('dark_background')  # Better contrast and often performs better

# 1. Generate optimized 3D data
np.random.seed(42)
n_points = 80  # Reduced number of points for better performance
x = np.random.rand(n_points) * 10 - 5
y = np.random.rand(n_points) * 10 - 5
z = np.random.rand(n_points) * 10 - 5
colors = np.random.rand(n_points)
sizes = np.random.rand(n_points) * 50 + 20  # Reduced size variation

# 2. Set up the figure with optimized settings
fig = plt.figure(figsize=(8, 6), dpi=100, facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# Remove axis ticks and grids for better performance
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# 3. Create the optimized scatter plot
scatter = ax.scatter(
    x, y, z,
    c=colors,
    s=sizes,
    cmap='plasma',  # Lighter colormap performs better
    alpha=0.9,
    edgecolors='none',
    linewidths=0  # Ensure no edges
)

# Add minimal labels
ax.set_xlabel('X', color='white')
ax.set_ylabel('Y', color='white')
ax.set_zlabel('Z', color='white')
ax.set_title('Optimized 3D Rotation', color='white', pad=20)

# 4. Pre-compute view angles for smoother animation
frames = 360  # One full rotation
elev_angles = 20 + 10 * np.sin(np.linspace(0, 2*np.pi, frames))
azim_angles = np.linspace(0, 360, frames)

# 5. Optimized update function
def update(frame):
    ax.view_init(elev=elev_angles[frame], azim=azim_angles[frame])
    return scatter,

# 6. Create the animation with optimized parameters
ani = animation.FuncAnimation(
    fig,
    update,
    frames=frames,
    interval=16,  # ~60fps (1000ms/60 ≈ 16ms/frame)
    blit=False,
    repeat=True,
    cache_frame_data=False  # Important for memory optimization
)

# For Jupyter Notebook display
from IPython.display import HTML
plt.close()  # Prevent double display
HTML(ani.to_html5_video())

# Uncomment to save (recommended for smoothest playback)
# ani.save('3d_rotation.mp4', writer='ffmpeg', fps=60, dpi=100, 
#          bitrate=2000, extra_args=['-vcodec', 'libx264'])