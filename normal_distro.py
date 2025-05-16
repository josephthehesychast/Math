import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def normalDistro(x,mu=0,sigma=1):
    density=(1/(sigma*np.sqrt(2*np.pi)))*np.exp(-0.5*((x-mu)/sigma)**2)
    return density

x_values=np.linspace(-5, 5, 1000)
pdf_values=normalDistro(x_values)

plt.style.use('dark_background')
plt.plot(x_values, pdf_values,color='red', label='Normal PDF (μ=0, σ=1)')
plt.title("Probability Density Function")
plt.xlabel("x")
plt.ylabel("PDF(x)")
plt.grid(True)
plt.legend()
plt.show()

#Gausian times a gausian 
def f(x,y):
    return np.exp(-(x**2 + y**2))


x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Set up dark theme
plt.style.use('dark_background')

# Create figure and 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Change the pane colors to dark
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.xaxis.pane.set_edgecolor('gray')
ax.yaxis.pane.set_edgecolor('gray')
ax.zaxis.pane.set_edgecolor('gray')

# Surface plot
surf = ax.plot_surface(X, Y, Z, cmap='inferno')  # 'inferno' works well on dark backgrounds

# Enhance grid visibility
ax.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0.2)
ax.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0.2)
ax.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0.2)

# Optional colorbar with white text
cbar = fig.colorbar(surf)
cbar.ax.yaxis.set_tick_params(color='white')
for text in cbar.ax.get_yticklabels():
    text.set_color('white')

# Titles and labels (with white text)
ax.set_title("z = e^(x² + y²)", color='white')
ax.set_xlabel("x", color='white')
ax.set_ylabel("y", color='white')
ax.set_zlabel("z", color='white')

# Set tick colors to white
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.tick_params(axis='z', colors='white')

plt.show()
