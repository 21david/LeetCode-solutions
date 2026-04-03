import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Join tables to see which ones have managers that left
    res = employees.merge(employees, left_on='manager_id', right_on='employee_id', how='left')

    # Select rows with low salaries and managers that left
    # (manager_id is not null, id of joined manager data is null, and salary is < 30,000)
    res2 = res[
        ~(res['manager_id_x'].isna())    \
        & (res['employee_id_y'].isna())  \
        & (res['salary_x'] < 30_000)
    ]

    # Rename column to LeetCode's requirement
    res2.rename(inplace=True, columns={'employee_id_x': 'employee_id'})

    # Order by employee ids
    ans = res2[['employee_id']].sort_values('employee_id')
    
    return ans
