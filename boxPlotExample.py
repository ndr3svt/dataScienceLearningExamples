import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = {
    'yr': [70]*50 + [71]*50 + [72]*50 + [73]*50 + [74]*50 + [75]*50 + [76]*50 + [77]*50 + [78]*50 + [79]*50,
    'cyl': [4,6,8]*167  # Mix of different cylinder counts
}
auto = pd.DataFrame(data)

# Create the boxplot
plt.figure(figsize=(12, 6))
sns.boxplot(x='yr', y='cyl', data=auto)

# Customize the plot
plt.title('Distribution of Cylinders by Year')
plt.xlabel('Year')
plt.ylabel('Number of Cylinders')

plt.show()