import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    res = cinema[(cinema['id'] % 2) & (cinema['description'] != 'boring')]
    res.sort_values(by='rating', ascending=False, inplace=True)
    return res
