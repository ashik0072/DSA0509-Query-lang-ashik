import matplotlib.pyplot as plt
import numpy as np

# Sample data
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]

# Set the width of the bars
bar_width = 0.35

# Generate the x-axis positions for men and women
x_positions_men = np.arange(len(groups))
x_positions_women = x_positions_men + bar_width

# Creating a bar plot with multiple X values for men and women
plt.bar(x_positions_men, means_men, width=bar_width, label='Men', color='blue')
plt.bar(x_positions_women, means_women, width=bar_width, label='Women', color='pink')

# Adding labels and title
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x_positions_men + bar_width / 2, groups)  # Set x-axis ticks at the center of each group

# Adding legend
plt.legend()

# Display the bar plot
plt.show()
