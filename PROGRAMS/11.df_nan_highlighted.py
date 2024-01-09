import pandas as pd
import numpy as np
from IPython.display import display  # Import display function

# Create a DataFrame with random values
np.random.seed(42)  # for reproducibility
data = np.random.randn(10, 4)  # 10 rows, 4 columns of random values
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

# Convert some values to NaN randomly
nan_indices = np.random.choice(range(10), size=(3, 2), replace=False)
for i, j in nan_indices:
    df.iloc[i, j] = np.nan

# Function to apply styles for highlighting NaN values
def highlight_nan(val):
    if pd.isna(val):
        return 'background-color: yellow'
    else:
        return ''

# Apply styles to the DataFrame
styled_df_nan = df.style.applymap(highlight_nan)

# Display the styled DataFrame with highlighted NaN values
display(styled_df_nan)
