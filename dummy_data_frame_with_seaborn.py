import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create the dummy DataFrame
data = {
    'ID': [101, 102, 103, 104, 105],
    'Category': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana'],
    'Score': [88, 92, 85, 90, 87]
}
df = pd.DataFrame(data)

# Convert the 'Category' column to a categorical type
df['Category'] = df['Category'].astype('category')

# Create a count plot to display the frequency distribution of the 'Category' variable
plt.figure(figsize=(8, 4))
sns.countplot(x='Category', data=df)
plt.title("Frequency Distribution of Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()