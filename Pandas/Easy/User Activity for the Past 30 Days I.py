import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity

    # Filter for the 30 period day
    filtered = df[(df.activity_date >= '2019-06-28') & (df.activity_date <= '2019-07-27')]
    """
    # Another option to select that 30 day period:
    end_date = pd.to_datetime('2019-07-27')
    start_date = end_date - pd.Timedelta(days=29)
    filtered = df[(df.activity_date >= start_date) & (df.activity_date <= end_date)]
    """

    # Get unique user_ids for each different day:
    # Group by the day and then find the number of unique users for each day by applying 'nunique'
    uniques = (
        filtered
            .groupby('activity_date', as_index=False)
            .agg(active_users=('user_id', 'nunique'))
            .rename(columns={'activity_date': 'day'})
    )

    return uniques
