import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    # Left join
    joined = pd.merge(employee, employee, left_on='managerId', right_on='id', how='inner')

    # Filter for employees earning more than manager
    res = joined.loc[joined['salary_x'] > joined['salary_y'], ['name_x']]

    # Rename column
    res.rename(columns={'name_x': 'Employee'}, inplace=True)
    
    return res
