import pandas as pd

# Updated approach
# Better concatenation, and use loc[0, <column>] to get top value as just strings
def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # Find the name of the user who has rated the greatest number of movies.
    review_counts = movie_rating.groupby('user_id', as_index=False).size()  # Find review amounts
    review_counts = review_counts.merge(users)  # Add names column
    # In case of a tie, return the lexicographically smaller user name.
    review_counts = review_counts.sort_values(['size', 'name'], ascending=[False, True]).reset_index()
    first_ans = review_counts.loc[0, 'name']  # name of guy with most reviews

    # Find the movie name with the highest average rating in February 2020
    movie_rating = movie_rating[(movie_rating.created_at >= '2020-02-01') & (movie_rating.created_at <= '2020-02-29')]  # Filter for feb
    movie_ratings_feb = movie_rating.groupby('movie_id', as_index=False)['rating'].mean()  # Find averages
    movie_ratings_feb = movie_ratings_feb.merge(movies)  # Add names column
    #  In case of a tie, return the lexicographically smaller movie name.
    movie_ratings_feb = movie_ratings_feb.sort_values(['rating', 'title'], ascending=[False, True]).reset_index()
    second_ans = movie_ratings_feb.loc[0, 'title'] # name of movie with highest rating

    # Combine into one DF
    return pd.DataFrame({'results': [first_ans, second_ans]})


 # -------------------------------------------------------------------------------------------------------

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    # Find the name of the user who has rated the greatest number of movies.
    review_counts = movie_rating.groupby('user_id', as_index=False).size()  # Find review amounts
    review_counts = review_counts.merge(users)  # Add names column
    # In case of a tie, return the lexicographically smaller user name.
    review_counts = review_counts.sort_values(['size', 'name'], ascending=[False, True])
    first_ans = review_counts.head(1)['name']

    # Find the movie name with the highest average rating in February 2020
    movie_rating = movie_rating[(movie_rating.created_at >= '2020-02-01') & (movie_rating.created_at <= '2020-02-29')]  # Filter for feb
    movie_ratings_feb = movie_rating.groupby('movie_id', as_index=False)['rating'].mean()  # Find averages
    movie_ratings_feb = movie_ratings_feb.merge(movies)  # Add names column
    #  In case of a tie, return the lexicographically smaller movie name.
    movie_ratings_feb = movie_ratings_feb.sort_values(['rating', 'title'], ascending=[False, True])
    second_ans = movie_ratings_feb.head(1)['title']

    # Combine into one DF
    res = pd.concat([first_ans, second_ans]).to_frame().rename(columns={0: 'results'})

    return res
