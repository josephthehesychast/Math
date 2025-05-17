import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and 3D axis with dark background
plt.style.use('dark_background')
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Set equal aspect ratio
ax.set_box_aspect([1, 1, 1])

# Create a larger viewing box
axis_limit = 4
ax.set_xlim(-axis_limit, axis_limit)
ax.set_ylim(-axis_limit, axis_limit)
ax.set_zlim(-axis_limit, axis_limit)


# X-axis
ax.quiver(0, 0, 0, axis_limit, 0, 0, color='white', arrow_length_ratio=0.1, lw=2)
# Y-axis
ax.quiver(0, 0, 0, 0, axis_limit, 0, color='white', arrow_length_ratio=0.1, lw=2)
# Z-axis
ax.quiver(0, 0, 0, 0, 0, axis_limit, color='white', arrow_length_ratio=0.1, lw=2)

# Add axes labels at the end of each axis
ax.text(axis_limit+0.2, 0, 0, "X", color='white', fontsize=14)
ax.text(0, axis_limit+0.2, 0, "Y", color='white', fontsize=14)
ax.text(0, 0, axis_limit+0.2, "Z", color='white', fontsize=14)

# Add light grid for reference
ax.grid(True, alpha=0.15)

# Origin point
origin = np.array([0, 0, 0])

# Vector to plot
vector = np.array([1, 2, 3])  

# Second Vector to plot
vector2 = np.array([3, 3, 0])

# Plot the vector as a prominent arrow from origin (in red)
ax.quiver(origin[0], origin[1], origin[2], 
          vector[0], vector[1], vector[2],
          color='red', arrow_length_ratio=0.1, lw=3)

# Plot the second vector as a prominent arrow from origin (in red)
ax.quiver(origin[0], origin[1], origin[2], 
          vector2[0], vector2[1], vector2[2],
          color='red', arrow_length_ratio=0.1, lw=3)

# Add a label for the vector
ax.text(vector[0]*1.1, vector[1]*1.1, vector[2]*1.1, 
         f"v = [{vector[0]}, {vector[1]}, {vector[2]}]", 
         color='red', fontsize=12)

# Add a label for the vector
ax.text(vector2[0]*1.1, vector2[1]*1.1, vector2[2]*1.1, 
         f"v = [{vector2[0]}, {vector2[1]}, {vector2[2]}]", 
         color='red', fontsize=12)

# Adjust the viewing angle to a nice isometric view
ax.view_init(elev=30, azim=45)

# Make tick labels white
ax.tick_params(colors='white')
for label in ax.get_xticklabels() + ax.get_yticklabels() + ax.get_zticklabels():
    label.set_color('white')

# Ensure axis lines are dark to blend with background
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
ax.xaxis.pane.set_alpha(0.1)
ax.yaxis.pane.set_alpha(0.1)
ax.zaxis.pane.set_alpha(0.1)

# Add title (in white)
plt.title('3D Vector Plot (3Blue1Brown Style)', fontsize=16, color='white')

# Show the plot
plt.tight_layout()
plt.show()
