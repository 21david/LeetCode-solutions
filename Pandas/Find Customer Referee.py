import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer.loc[(customer['referee_id'] != 2) | (customer['referee_id'].isna()), 'name'].to_frame()


# Another approach
# Convert nulls to 0 then just check for != 2, and select a list of 1 column to get back a data frame, instead of converting later
def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer['referee_id'] = customer['referee_id'].fillna(0)
    return customer.loc[customer['referee_id'] != 2, ['name']]
