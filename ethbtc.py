import pandas as pd

# Load your data

mean_low = df['low'].mean()
std_dev_low = df['low'].std()
df['z_score_low'] = (df['low'] - mean_low) / std_dev_low

# Print the result to check
print(df[['low', 'z_score_low']].head())