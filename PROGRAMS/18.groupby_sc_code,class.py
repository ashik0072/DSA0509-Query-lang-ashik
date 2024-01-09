import pandas as pd
from io import StringIO

# Sample data
data = """Student ID,School,Class,Name,Date of Birth,Age,Height,Weight,Address
S1 s001,V,Alberto Franco,15/05/2002,12,173,35,street1
S2 s002,V,Gino Mcneill,17/05/2002,12,192,32,street2
S3 s003,VI,Ryan Parkes,16/02/1999,13,186,33,street3
S4 s001,VI,Eesha Hinton,25/09/1998,13,167,30,street1
S5 s002,V,Gino Mcneill,11/05/2002,14,151,31,street2
S6 s004,VI,David Parkes,15/09/1997,12,159,32,street4
"""

# Create DataFrame from the sample data
df = pd.read_csv(StringIO(data), sep=',')

# Group by School and Class
grouped_school_class = df.groupby(['School', 'Class'])

# Display the groups
for (school, class_), group in grouped_school_class:
    print(f"School: {school}, Class: {class_}")
    print(group)
    print("\n")
