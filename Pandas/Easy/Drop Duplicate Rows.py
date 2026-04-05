# https://leetcode.com/problems/drop-duplicate-rows

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # help(customers.drop_duplicates)
    customers.drop_duplicates(subset='email', keep='first', inplace=True)
    return customers
