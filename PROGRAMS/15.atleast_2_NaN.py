import pandas as pd
from io import StringIO

# Sample data
data = """Index,ord_no,purch_amt,ord_date,customer_id
0,NaN,NaN,NaN,NaN
1,NaN,270.65,2012-09-10,3001.0
2,70002.0,65.26,NaN,3001.0
3,NaN,NaN,NaN,NaN
4,NaN,948.50,2012-09-10,3002.0
5,70005.0,2400.60,2012-07-27,3001.0
6,NaN,5760.00,2012-09-10,3001.0
7,70010.0,1983.43,2012-10-10,3004.0
8,70003.0,2480.40,2012-10-10,3003.0
9,70012.0,250.45,2012-06-27,3002.0
10,NaN,75.29,2012-08-17,3001.0
11,NaN,NaN,NaN,NaN
"""

# Create DataFrame from the sample data
df = pd.read_csv(StringIO(data), index_col='Index')

# Keep rows with at least 2 NaN values
df_at_least_2_nan = df.dropna(thresh=2)

# Display the DataFrame after keeping the rows
print(df_at_least_2_nan)
