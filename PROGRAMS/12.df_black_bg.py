import pandas as pd
import numpy as np
from IPython.display import display  # Import display function

# Create a DataFrame with random values
np.random.seed(42)  # for reproducibility
data = np.random.randn(10, 4)  # 10 rows, 4 columns of random values
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])

# Function to apply styles for black background and yellow font color
def style_df_black_yellow(val):
    return 'background-color: black; color: yellow'

# Apply styles to the entire DataFrame
styled_df_black_yellow = df.style.applymap(style_df_black_yellow)

# Display the styled DataFrame with black background and yellow font color
display(styled_df_black_yellow)
