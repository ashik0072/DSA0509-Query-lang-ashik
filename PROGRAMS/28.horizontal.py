import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Creating a horizontal bar chart
plt.barh(languages, popularity, color=['blue', 'green', 'orange', 'yellow', 'purple', 'red'])

# Adding labels and title
plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages (Horizontal Bar Chart)')

# Display the horizontal bar chart
plt.show()
