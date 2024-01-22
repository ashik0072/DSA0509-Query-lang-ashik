import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Creating multiple plots in a single figure
fig, axs = plt.subplots(3, 1, figsize=(8, 12))  # 3 rows, 1 column of subplots

# Plotting on the first subplot
axs[0].plot(x, y1, label='sin(x)', color='blue')
axs[0].set_title('Plot of sin(x)')
axs[0].legend()

# Plotting on the second subplot
axs[1].plot(x, y2, label='cos(x)', color='green')
axs[1].set_title('Plot of cos(x)')
axs[1].legend()

# Plotting on the third subplot
axs[2].plot(x, y3, label='tan(x)', color='red')
axs[2].set_title('Plot of tan(x)')
axs[2].legend()

# Adding labels, title, and layout adjustments
plt.xlabel('X-axis')
plt.tight_layout()

# Display the plots
plt.show()
