import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions

    # Make a column for unique months
    df['temp_month'] = df['trans_date'].dt.month.astype(str)
    df['temp_month'] = df['temp_month'].apply(lambda x: f'{x:0>2}')
    df['year'] = df['trans_date'].dt.year.astype(str)
    df['month'] = df['year'] + '-' + df['temp_month']

    # Group by the unique months to get aggregated data
    # dropna=False so that 'null' countries still have their own group, as expected by LC (otherwise it drops those groups)
    gb = df.groupby(['country', 'month'], as_index=False, dropna=False).agg({'trans_date': 'count', 'amount':'sum'})
    print(gb)

    # Group by unique months but filter by approved to get the approved aggregated data
    gb_appr = df.groupby(['country', 'month', 'state'], as_index=False, dropna=False).agg({'trans_date': 'count', 'amount':'sum'})
    gb_appr = gb_appr[gb_appr['state'] == 'approved']

    # Merge all columns together and clean up
    final_df = gb.merge(gb_appr, on=['country', 'month'], how = 'left')
    final_df.rename(columns={
        'trans_date_x': 'trans_count', 
        'amount_x': 'trans_total_amount',
        'trans_date_y': 'approved_count',
        'amount_y': 'approved_total_amount'
    }, inplace=True)

    # Since some tables don't have approved rows, replace resulting nulls with 0s since that's what LC expects
    final_df[['approved_count', 'approved_total_amount']] = final_df[['approved_count', 'approved_total_amount']].fillna(0)

    return final_df[['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']]
