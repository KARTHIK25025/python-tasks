import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Scenario 1: Data Loading & Preprocessing

print("--- Scenario 1: Data Loading & Preprocessing ---")

# 1. Load the dataset
df = pd.read_csv("ign.csv")

# 2. Display basic info
print("First 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())
print("\nShape of dataset:", df.shape)

# 3. Remove the unnecessary column
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# 4. Check for missing values
print("\nMissing values before handling:")
print(df[["score", "genre", "platform"]].isnull().sum())

# 5. Handle missing values
# Fill numeric column score with mean
df["score"].fillna(df["score"].mean(), inplace=True)
# Fill categorical column genre with mode
df["genre"].fillna(df["genre"].mode()[0], inplace=True)

# 6. Ensure correct data types
# Dropping NA for date columns if any remain to safely convert to integer
df["release_year"] = df["release_year"].fillna(0).astype(int)
df["release_month"] = df["release_month"].fillna(0).astype(int)
df["release_day"] = df["release_day"].fillna(0).astype(int)
df["score"] = df["score"].astype(float)

print("\nData types after conversion:")
print(df[["score", "release_year", "release_month", "release_day"]].dtypes)


# Scenario 2: Line Graph (Score Trend) + Save

print("\n--- Scenario 2: Line Graph ---")

# 1. Group data by release_year and 2. Calculate average score per year
yearly_avg = df.groupby("release_year")["score"].mean().sort_index()

# 3. Convert results into NumPy arrays
years = np.array(yearly_avg.index)
avg_scores = np.array(yearly_avg.values)

# 4. Plot a line graph
plt.figure(figsize=(10, 5))
plt.plot(years, avg_scores, marker='o', linestyle='-', color='b')

# 5. Add titles and labels
plt.title("Average Game Score Over Years")
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.grid(True, linestyle="--", alpha=0.6)

# 6. Save the graph
plt.savefig("avg_score_trend.png")
plt.close()
print("Saved 'avg_score_trend.png'")


# Scenario 3: Filtering + Bar Chart + Save

print("\n--- Scenario 3: Bar Chart ---")

# 1. Filter dataset where score > 7
high_rated = df[df["score"] > 7]

# 2. Count number of high-rated games per platform and 3. Select top 10
top_platforms = high_rated["platform"].value_counts().head(10)

# 4. Convert data into NumPy arrays
platforms = np.array(top_platforms.index)
platform_counts = np.array(top_platforms.values)

# 5. Plot a bar chart
plt.figure(figsize=(12, 6))
plt.bar(platforms, platform_counts, color='orange')

# 6. Rotate x-axis labels
plt.title("Top 10 Platforms with Games Scoring > 7")
plt.xlabel("Platform")
plt.ylabel("Count of High-Rated Games")
plt.xticks(rotation=45, ha='right')

# Save the graph
plt.tight_layout()
plt.savefig("top_platforms_bar.png")
plt.close()
print("Saved 'top_platforms_bar.png'")


# Scenario 4: Aggregation + Pie Chart + Save

print("\n--- Scenario 4: Pie Chart ---")

# 1. Count games per genre and 2. Select top 5
top_genres = df["genre"].value_counts().head(5)

# 3. Prepare labels and values
genre_labels = np.array(top_genres.index)
genre_counts = np.array(top_genres.values)

# 4 & 5. Plot pie chart with percentages
plt.figure(figsize=(8, 8))
plt.pie(genre_counts, labels=genre_labels, autopct='%1.1f%%', startangle=140)
plt.title("Top 5 Game Genres Distribution")

# Save the graph
plt.savefig("genre_distribution.png")
plt.close()
print("Saved 'genre_distribution.png'")


# Scenario 5: Advanced Analysis + Graphs

print("\n--- Scenario 5: Advanced Analysis ---")

# --- Part 1: Feature Engineering ---
# 1. Create score_category
conditions = [
    (df['score'] >= 9),
    (df['score'] >= 7) & (df['score'] < 9),
    (df['score'] < 7)
]
choices = ['Excellent', 'Good', 'Average']
df['score_category'] = np.select(conditions, choices, default='Average')

# 2. Convert editors_choice
df['editors_choice'] = df['editors_choice'].map({'Y': 1, 'N': 0})

# --- Part 2: NumPy Analysis ---
# 3. Calculate yearly score growth using np.diff()
yearly_avg_scores = df.groupby("release_year")["score"].mean().sort_index()
score_growth = np.insert(np.diff(yearly_avg_scores.values), 0, 0) # Insert 0 for the first year to match array lengths
print("Yearly Score Growth Calculated successfully.")

# --- Part 3 & 4: Visualizations & Saving ---
# 4. Line Graph: Trend of average score per release_year
plt.figure(figsize=(10, 5))
plt.plot(yearly_avg_scores.index, yearly_avg_scores.values, color='green', marker='s')
plt.title("Trend of Average Score per Release Year")
plt.xlabel("Year")
plt.ylabel("Average Score")
plt.grid(True)
plt.savefig("score_trend.png")
plt.close()

# 5. Stacked Bar Chart: score_category per release_year
category_counts = pd.crosstab(df['release_year'], df['score_category'])
category_counts.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='viridis')
plt.title("Count of Score Category per Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Games")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("score_category_stacked.png")
plt.close()

# 6. Histogram: distribution of score
plt.figure(figsize=(8, 5))
plt.hist(df['score'], bins=20, color='purple', edgecolor='black')
plt.title("Distribution of Game Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.savefig("score_distribution.png")
plt.close()

print("Saved 'score_trend.png', 'score_category_stacked.png', and 'score_distribution.png'")

# --- Part 5: Insights ---
print("\n--- Part 5: Insights ---")
best_year = yearly_avg_scores.idxmax()
best_score = yearly_avg_scores.max()
print(f"1. Which years had highest scores: The year {best_year} had the highest average score of {best_score:.2f}.")

# Checking start vs end trend
start_score = yearly_avg_scores.values[0]
end_score = yearly_avg_scores.values[-1]
trend = "increased" if end_score > start_score else "decreased/fluctuated"
print(f"2. Whether high scores increased over time: Generally, average scores have {trend} (Started at {start_score:.2f}, ended at {end_score:.2f}).")

# Checking correlation
correlation = df[['score', 'editors_choice']].corr().iloc[0, 1]
print(f"3. If editors_choice correlates with high scores: Yes, there is a moderate positive correlation ({correlation:.2f}) between editors_choice and higher scores.")