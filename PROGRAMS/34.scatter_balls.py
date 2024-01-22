import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(42)  # Setting a seed for reproducibility
num_points = 50
random_x = np.random.randn(num_points)
random_y = np.random.randn(num_points)

# Generate random sizes for the balls
sizes = np.random.randint(10, 100, num_points)

# Create a scatter plot with balls of different sizes
plt.scatter(random_x, random_y, s=sizes, alpha=0.7, c='blue', edgecolors='black', label='Random Data')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Balls of Different Sizes and Random Data')

# Adding legend
plt.legend()

# Display the scatter plot
plt.show()
