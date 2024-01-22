import pandas as pd

# Sample DataFrame
data = {'Name': ['John', 'Alice', 'Bob', 'Eve'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'San Francisco']}
df = pd.DataFrame(data)

# Specified character column to swap cases
column_to_swap = 'Name'

# Swapping cases using str.swapcase()
df[column_to_swap] = df[column_to_swap].str.swapcase()

# Display the updated DataFrame
print(df)
