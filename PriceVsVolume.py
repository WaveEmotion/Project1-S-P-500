import pandas as pd
import matplotlib.pyplot as plt

# read the csv
data = pd.read_csv('sp.csv')
df = pd.DataFrame(data)

# convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# create the plot, with price on the left
fig, ax1 = plt.subplots(figsize=(26, 14))
ax1.plot(df['Date'], df['Close'], color='blue', label='Close Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price (USD)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# the 2nd y axis for volume
ax2 = ax1.twinx()
ax2.plot(df['Date'], df['Volume'], color='red', label='Volume', linestyle='--', alpha = 0.75)
ax2.set_ylabel('Volume (10 billions)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
plt.title('Price and Volume of the S&P 500 From 1928-2021')



# vertical lines for special events

special_dates = {
    'Great Depression': '1929-10-29',
    'Dot-com Bubble Burst': '2000-03-10',
    'Financial Crisis': '2008-09-15',
    'COVID-19 Crash': '2020-03-16'
}


for event, date in special_dates.items():
    plt.axvline(pd.to_datetime(date), color='gray', linestyle='--', alpha=0.7)
    plt.annotate(event, (pd.to_datetime(date), df['Close'].min()), textcoords="offset points", xytext=(10,-10), ha='center', fontsize=9)

plt.show()
