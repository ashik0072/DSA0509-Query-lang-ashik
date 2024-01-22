import matplotlib.pyplot as plt

# Read data from the text file
file_path = 'test.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# Extract x and y values
x_values = [float(line.split()[0]) for line in lines]
y_values = [float(line.split()[1]) for line in lines]

# Plotting the line
plt.plot(x_values, y_values)

# Adding labels and title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot from Text File')

# Display the plot
plt.show()
