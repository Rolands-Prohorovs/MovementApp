import pandas as pd

# Example data
data = {
'Temperature': [22, 23, 21, 20, 19, 18, 17, 16, 15, 14],
'Movement': [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]
}

# Create DataFrame
df = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df)