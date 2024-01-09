import pandas as pd
import numpy as np
from IPython.display import display  # Import display function

# Create a DataFrame with random values
np.random.seed(42)  # for reproducibility
data = np.random.randn(10, 4)  # 10 rows, 4 columns of random values
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

# Function to apply styles
def highlight_numbers(val):
    color = 'red' if val < 0 else 'black'
    return f'color: {color}'

# Apply styles to the DataFrame
styled_df = df.style.apply(lambda x: x.map(highlight_numbers))

# Display the styled DataFrame
display(styled_df)
