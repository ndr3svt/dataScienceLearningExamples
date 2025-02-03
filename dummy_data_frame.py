import pandas as pd

# Create a dummy DataFrame with some sample data
data = {
    'ID': [101, 102, 103, 104, 105],
    'Category': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana'],
    'Score': [88, 92, 85, 90, 87]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Convert the 'Category' column to categorical type
df['Category'] = df['Category'].astype('category')

print("\nDataFrame Info After Converting 'Category' to Categorical:")
print(df.info())

# Practice Operations:
# 1. List the categories
print("\nCategories:", df['Category'].cat.categories)

# 2. Count the frequency of each category
print("\nCategory Counts:")
print(df['Category'].value_counts())

# 3. Filter DataFrame rows based on a categorical value (e.g., Banana)
banana_df = df[df['Category'] == 'Banana']
print("\nFiltered DataFrame (Category = 'Banana'):")
print(banana_df) 