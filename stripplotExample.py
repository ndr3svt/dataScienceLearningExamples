import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Let's create a sample dataset similar to the auto dataset
data = {
    'wt': [2500 + i*10 for i in range(500)],  # weights from 2500-7500
    'cyl': [4]*200 + [6]*150 + [8]*100 + [3]*30 + [5]*20  # different cylinder counts
}
auto = pd.DataFrame(data)

# Create the stripplot
plt.figure(figsize=(12, 6))
sns.stripplot(x='wt', y='cyl', data=auto)

# Customize the plot
plt.title('Car Weight by Number of Cylinders')
plt.xlabel('Weight')
plt.ylabel('Number of Cylinders')

plt.show()