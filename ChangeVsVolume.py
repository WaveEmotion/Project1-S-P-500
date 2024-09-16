import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# read file
data = pd.read_csv('sp.csv')
df = pd.DataFrame(data)

# create daily return percentage
df['Daily Return'] = df['Close'].pct_change() * 100
df = df.dropna()

# filter out columns with 0 volume for clarity
df = df[df['Volume'] > 0]

# Create bins for the years of the data
df['Year'] = pd.to_datetime(df['Date']).dt.year
bins = [1928, 1950, 1975, 2000, 2021]
labels = ['1928-1950', '1950-1975', '1975-2000', '2000-2021']
df['Year Range'] = pd.cut(df['Year'], bins=bins, labels=labels, right=False)

# create the scatter plot, with different colors for each year bin
sns.set_theme(style='whitegrid')
plt.figure(figsize=(10, 5))
scatter = sns.scatterplot(x='Volume', y='Daily Return', data=df, edgecolor=None, hue='Year Range', palette='viridis')
plt.title('Volume vs. Daily Price Change of the S&P 500 Index 1928-2021')
plt.xlabel('Volume')
plt.ylabel('% Change')
plt.legend(title='Year Range')

plt.show()
