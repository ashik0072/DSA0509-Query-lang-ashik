import pandas as pd
from io import StringIO

# Sample data
data = """Year,WHO Region,Country,Beverage Types,Display Value
1986,Western Pacific,Viet Nam,Wine,0.00
1986,Americas,Uruguay,Other,0.50
1985,Africa,Côte d'Ivoire,Wine,1.62
1986,Americas,Colombia,Beer,4.27
1987,Americas,Saint Kitts and Nevis,Beer,1.98
"""

# Create DataFrame from the sample data
df = pd.read_csv(StringIO(data), sep=',')

# Define the substring to search for
substring_to_search = 'Nam'

# Find the index of rows where the substring is present in the 'Country' column
matching_indices = df[df['Country'].str.contains(substring_to_search)].index

# Display the indices
print(f"Indices where the substring '{substring_to_search}' is present in the 'Country' column: {matching_indices}")
