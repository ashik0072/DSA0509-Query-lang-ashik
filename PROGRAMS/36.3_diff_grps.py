import matplotlib.pyplot as plt
import numpy as np

# Sample data for three groups
group1_heights = np.random.normal(170, 5, 30)
group1_weights = np.random.normal(65, 7, 30)

group2_heights = np.random.normal(160, 5, 30)
group2_weights = np.random.normal(55, 7, 30)

group3_heights = np.random.normal(180, 5, 30)
group3_weights = np.random.normal(75, 7, 30)

# Create a scatter plot for three different groups
plt.scatter(group1_heights, group1_weights, c='blue', marker='o', label='Group 1')
plt.scatter(group2_heights, group2_weights, c='green', marker='s', label='Group 2')
plt.scatter(group3_heights, group3_weights, c='orange', marker='^', label='Group 3')

# Adding labels and title
plt.xlabel('Heights (cm)')
plt.ylabel('Weights (kg)')
plt.title('Scatter Plot of Heights vs Weights for Three Groups')

# Adding legend
plt.legend()

# Display the scatter plot
plt.show()
