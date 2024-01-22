import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Creating a bar chart with different colors for each bar
colors = ['blue', 'green', 'orange', 'yellow', 'purple', 'red']
plt.bar(languages, popularity, color=colors)

# Adding labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages (Colored Bar Chart)')

# Display the bar chart
plt.show()
