import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# Plotting lines with different widths and colors
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='green', linewidth=1.5)
plt.plot(x, y3, label='tan(x)', color='red', linewidth=2.5)

# Adding labels, title, and legend
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines with Legends')
plt.legend()

# Display the plot
plt.show()
