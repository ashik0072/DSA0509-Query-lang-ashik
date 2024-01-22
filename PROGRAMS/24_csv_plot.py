import pandas as pd
import matplotlib.pyplot as plt

# Read financial data from CSV file
file_path = 'fdata.csv'
df = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)

# Plotting line charts
plt.plot(df['Date'], df['Open'], label='Open', marker='o')
plt.plot(df['Date'], df['High'], label='High', marker='o')
plt.plot(df['Date'], df['Low'], label='Low', marker='o')
plt.plot(df['Date'], df['Close'], label='Close', marker='o')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.title('Financial Data of Alphabet Inc. (Oct 3, 2016 - Oct 7, 2016)')
plt.legend()

# Rotating x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()
