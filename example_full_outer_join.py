import pandas as pd

# Define the first DataFrame
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'val1': [1, 2, 3]
})

# Define the second DataFrame
df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'val2': [4, 5, 6]
})

# Perform a full outer join on the 'key' column
df_full_outer = pd.merge(df1, df2, on='key', how='outer')
print("Full Outer Join Result:")
print(df_full_outer) 