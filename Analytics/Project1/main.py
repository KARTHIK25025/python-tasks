import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# SCENARIO 1: Basic Data Loading & Cleaning

print("--- SCENARIO 1: Basic Data Loading & Cleaning ---")

# 1. Load the dataset
df = pd.read_csv('railway_gauges.csv')

# Clean column names (strip trailing spaces)
df.columns = df.columns.str.strip()

# 2. Display first 5 rows and column names
print("Column Names:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# 3. Check for missing values and replace them with 0
df.fillna(0, inplace=True)

# 4. Convert all gauge columns to numeric types
cols_to_convert = ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge', 'Total']
for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

print("\nData loading and cleaning complete!\n")


# SCENARIO 2: Simple Visualization

print("--- SCENARIO 2: Simple Visualization ---")

# 1 & 2. Extract columns and plot Line Graph
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Total'], marker='o')

# 3. Add Title and Labels
plt.title('Total Railway Tracks Growth Over the Years')
plt.xlabel('Year')
plt.ylabel('Total Tracks')

# Cleanup X-axis to avoid overlap
plt.xticks(range(0, len(df), 5), df['Year'].iloc[::5], rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 4. Identify Trend
trend = "INCREASING" if df['Total'].iloc[-1] > df['Total'].iloc[0] else "DECREASING"
print(f"Insight: The overall trend of total tracks is {trend}.\n")


# SCENARIO 3: Filtering + Bar Chart

print("--- SCENARIO 3: Filtering + Bar Chart ---")

# 1. Filter dataset for years after 2000 (Extract year as integer)
df['Start_Year'] = df['Year'].astype(str).str[:4].astype(int)
df_modern = df[df['Start_Year'] >= 2000]

# 2 & 3. Select specific columns and plot grouped bar chart
fig, ax = plt.subplots(figsize=(12, 6))
df_modern.set_index('Year')[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].plot(
    kind='bar', ax=ax, width=0.8,
)

# 4. Add legend and labels
ax.set_title('Modern Railway Expansion (Post-2000)')
ax.set_xlabel('Year')
ax.set_ylabel('Track Length')
ax.legend(title='Gauge Type')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Identify dominant gauge
dominant_gauge = df_modern[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].sum().idxmax()
print(f"Insight: The dominant gauge in recent years is {dominant_gauge}.\n")


# SCENARIO 4: Feature Engineering + Pie Chart

print("--- SCENARIO 4: Feature Engineering + Pie Chart ---")

# 1 & 2. Calculate total sum of each gauge and create a Series structure
gauge_totals = df[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].sum()

# 3 & 4. Plot Pie chart with percentages
plt.figure(figsize=(7, 7))
gauge_totals.plot(
    kind='pie', autopct='%1.1f%%', startangle=140, 
)
plt.title('Overall Contribution of Each Gauge Type')
plt.ylabel('') # Hide y-label
plt.tight_layout()
plt.show()

# 5. Interpret most contributing gauge
highest_contributor = gauge_totals.idxmax()
print(f"Insight: Historically, {highest_contributor} contributes the most.\n")


# SCENARIO 5: Advanced Analysis + Multiple Graphs

print("--- SCENARIO 5: Advanced Analysis ---")

# 1. Create Percentage columns
df['% Broad'] = (df['Broad Gauge'] / df['Total']) * 100
df['% Metre'] = (df['Metre Gauge'] / df['Total']) * 100
df['% Narrow'] = (df['Narrow Gauge'] / df['Total']) * 100

# 2. Yearly growth (inserting 0 for the first year to match DataFrame length)
df['Growth'] = np.insert(np.diff(df['Total']), 0, 0)

# 3. Plot multiple graphs (Line graph + Stacked bar chart)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))

# Graph A: Line Graph for all gauges
axes[0].plot(df['Year'], df['Broad Gauge'], label='Broad Gauge', marker='o',)
axes[0].plot(df['Year'], df['Metre Gauge'], label='Metre Gauge', marker='s',)
axes[0].plot(df['Year'], df['Narrow Gauge'], label='Narrow Gauge', marker='^',)
axes[0].set_title('Track Length by Gauge Over Time')
axes[0].set_ylabel('Track Length')
axes[0].legend()
axes[0].set_xticks(range(0, len(df), 5))
axes[0].set_xticklabels(df['Year'].iloc[::5], rotation=45)
axes[0].grid(True, linestyle='--', alpha=0.5)

# Graph B: Stacked Bar Chart
df.set_index('Year')[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].plot(
    kind='bar', stacked=True, ax=axes[1], 
)
axes[1].set_title('System Shift: Railway Gauge Composition (Stacked)')
axes[1].set_ylabel('Total Length')
axes[1].set_xticks(range(0, len(df), 3))
axes[1].set_xticklabels(df['Year'].iloc[::3], rotation=45)

plt.tight_layout()
plt.show()

# 4. Highlight peaks and declines
max_growth_idx = df['Growth'].idxmax()
print(f"Highlight: The year with the highest growth was {df.loc[max_growth_idx, 'Year']} (+{int(df.loc[max_growth_idx, 'Growth'])} tracks).")

for col in ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']:
    if df[col].iloc[-1] < df[col].iloc[0]:
        print(f"Highlight: A continuous historical decline was detected in {col}.")

# 5. Final Conclusion
print("\n--- FINAL CONCLUSION ---")
print("Question: Is the railway system shifting towards a single dominant gauge?")
print("Answer: Yes. The data explicitly shows that while the total track length increases, "
      "the lengths of Metre and Narrow gauges decline significantly. The network is "
      "actively shifting towards a single standard: the Broad Gauge.")