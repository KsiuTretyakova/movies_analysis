import ast

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "movies_metadata.csv"
movies_df = pd.read_csv(url)

# print(movies_df.head())  # 5 lines

movies_df.info()

# print(movies_df.describe())

#homework:
        # pip freeze > requirements | pip freeze > requirements.txt


def extract_genres(genres_str):
    try:
        genres = ast.literal_eval(genres_str)
        return [genre['name'] for genre in genres]
    except ValueError:
        return []


movies_df['genres'] = movies_df['genres'].apply(extract_genres)
print(movies_df['genres'])


# -------------------------------
movies_df['budget'] = pd.to_numeric(movies_df['budget'], errors='coerce')
movies_df['revenue'] = pd.to_numeric(movies_df['revenue'], errors='coerce')

movies_df.dropna(subset=['budget', 'revenue'], inplace=True)
#
# # -------------------------------------
movies_df['release_year'] = pd.to_datetime(movies_df['release_date'], errors='coerce').dt.year
# print(movies_df['release_year'])


#---------------------------------------------------------------

genre_exploded = movies_df[['title','release_year', 'budget', 'revenue', 'genres']].explode('genres')
print(genre_exploded)

genre_counts = genre_exploded['genres'].value_counts()

plt.figure(figsize=(10,6))
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.title("Кількість фільмів за жанрами")
plt.xlabel("Жанр")
plt.ylabel("Кількість")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

