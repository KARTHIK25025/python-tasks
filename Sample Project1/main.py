import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv('railway_gauges.csv') 
print(df.head())

# Find which year had the maximum installations
max_year_data = df.iloc[[df['Total'].idxmax()]]
print(max_year_data)

# Plot data using bar chart
df = df.drop('Total', axis=1) 
ax = df.plot(x="Year", kind="bar")
plt.xticks(rotation=70)
plt.xlabel('Year')
plt.ylabel('Total')
plt.title('Gauges: Number of railway tracks installed per year')
plt.savefig('rail_gauges.png')
plt.show()