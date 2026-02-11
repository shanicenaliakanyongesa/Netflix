import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("netflix_titles.csv")

# Handle missing values
missing_strings = ['', ' ', 'nan', 'NaN', 'None', None]
cols = ['director','cast','country','rating','date_added','duration']
for col in cols:
    data[col] = data[col].apply(lambda x: 'Unknown' if str(x).strip() in missing_strings else x)

# Set style
sns.set_style("whitegrid")

# 1. Distribution of content type
plt.figure(figsize=(8,6))
data['type'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Content Type')
plt.xlabel('Type')
plt.ylabel('Count')
plt.savefig('content_type_distribution.png')
plt.close()

# 2. Top 10 countries with most content
plt.figure(figsize=(8,6))
data['country'].str.split(', ').explode().value_counts().head(10).plot(kind='barh', color='lightcoral')
plt.title('Top 10 Countries with Most Content')
plt.xlabel('Count')
plt.savefig('top_countries.png')
plt.close()

# 3. Rating distribution
plt.figure(figsize=(8,6))
data['rating'].value_counts().plot(kind='bar', color='lightgreen')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.savefig('rating_distribution.png')
plt.close()

# 4. Release year distribution
plt.figure(figsize=(8,6))
data['release_year'].value_counts().sort_index().plot(kind='line', color='purple')
plt.title('Content by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.savefig('release_year_trends.png')
plt.close()

# Additional: Duration distributions
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Movies duration
movies_duration = data[data['type'] == 'Movie']['duration'].str.extract('(\d+)').astype(float)
movies_duration.plot(kind='hist', bins=30, ax=axes[0], color='orange', edgecolor='black')
axes[0].set_title('Distribution of Movie Duration (minutes)')
axes[0].set_xlabel('Duration (minutes)')
axes[0].set_ylabel('Count')

# TV Shows seasons
tv_seasons = data[data['type'] == 'TV Show']['duration'].str.extract('(\d+)').astype(float)
tv_seasons.plot(kind='hist', bins=20, ax=axes[1], color='teal', edgecolor='black')
axes[1].set_title('Distribution of TV Show Seasons')
axes[1].set_xlabel('Number of Seasons')
axes[1].set_ylabel('Count')

plt.tight_layout()
plt.savefig('duration_distributions.png')
plt.close()

# Content age
data['content_age'] = 2023 - data['release_year']
data['content_age'].plot(kind='hist', bins=30, color='lightblue', edgecolor='black')
plt.title('Content Age Distribution')
plt.xlabel('Age (years)')
plt.ylabel('Count')
plt.savefig('content_age_distribution.png')
plt.close()

print("Images generated successfully!")
