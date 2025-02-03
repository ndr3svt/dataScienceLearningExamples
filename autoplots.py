import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style and random seed for reproducibility
sns.set(style="whitegrid")
np.random.seed(1)

# Create a sample 'auto' DataFrame with 100 observations.
auto = pd.DataFrame({
    'disp': np.random.uniform(100, 300, 100),  # displacement values between 100 and 300
    'acc': np.random.uniform(10, 30, 100)       # acceleration values between 10 and 30
})

# Example 1: Pairplot using columns 'disp' and 'acc'
sns.pairplot(auto[['disp', 'acc']])
plt.suptitle("Pairplot: disp and acc", y=1.02)
plt.show()

#example 
sns.scatterplot(auto[['acc','disp']])


# Example 2: Scatterplot using columns 'acc' and 'disp'
plt.figure()  # Start a new figure
sns.scatterplot(data=auto[['acc', 'disp']], x='acc', y='disp')
plt.title("Scatterplot: acc vs disp")
plt.xlabel("Acceleration")
plt.ylabel("Displacement")
plt.show()



# Example 3: Histplot for both 'disp' and 'acc'
# Melt the DataFrame so that we have one column for the variable name and one for its value.
auto_melt = auto[['disp', 'acc']].melt(var_name='variable', value_name='value')

plt.figure()
sns.histplot(data=auto_melt, x='value', hue='variable', multiple='dodge', bins=20)
plt.title("Histogram for disp and acc")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Example 4: Pairplot using columns 'acc' and 'disp'
sns.pairplot(auto[['acc', 'disp']])
plt.suptitle("Pairplot: acc and disp", y=1.02)
plt.show()

