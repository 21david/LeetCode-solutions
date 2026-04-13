import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Filter out rows with a banned user or client
    banned = set(users[users.banned == 'Yes'].users_id)
    not_banned = trips[~(trips.client_id.isin(banned)) & ~(trips.driver_id.isin(banned))]

    # Add boolean 'cancelled' column
    not_banned['cancelled'] = not_banned.status.str[:9] == 'cancelled'

    # Group by and find total cancelled as well as total orders for each day
    grouped = not_banned.groupby('request_at', as_index=False).agg({'cancelled': 'sum', 'status': 'count'})

    # Calculate cancellation rate
    grouped['Cancellation Rate'] = (grouped.cancelled / grouped.status).round(2)

    # Rename column
    grouped.rename(inplace=True, columns={'request_at': 'Day'})

    # Only get the 3 requested days
    grouped = grouped[grouped.Day.isin(['2013-10-01', '2013-10-02', '2013-10-03'])]

    return grouped[['Day', 'Cancellation Rate']]
