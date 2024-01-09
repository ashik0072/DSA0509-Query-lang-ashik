import pandas as pd
from io import StringIO

# Sample data
data = """Customer ID,Order Number,Purchase Amount,Order Date,Salesman ID
3002,70001.0,150.5,2012-10-05,5002.0
3001,,270.65,2012-09-10,5003.0
3001,70002.0,65.26,,5001.0
3003,70004.0,110.5,2012-08-17,
3002,,948.5,2012-09-10,5002.0
3001,70005.0,2400.6,2012-07-27,5001.0
3001,,5760.0,2012-09-10,5001.0
3004,70010.0,1983.43,2012-10-10,
3003,70003.0,2480.4,2012-10-10,5003.0
3002,70012.0,250.45,2012-06-27,5002.0
"""

# Create DataFrame from the sample data
df = pd.read_csv(StringIO(data))

# Detect missing values using isna() and display True or False
missing_values_isna = df.isna()
print(missing_values_isna)
