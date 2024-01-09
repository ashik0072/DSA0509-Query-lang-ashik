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

# Display the dimensions or shape of the DataFrame
dimensions = df.shape
print(f"Dimensions of the DataFrame: {dimensions}")

# Extract the column names from the DataFrame
column_names = df.columns
print(f"Column names of the DataFrame: {column_names}")
