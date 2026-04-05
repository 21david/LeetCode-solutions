# https://leetcode.com/problems/drop-missing-data
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # help(students.dropna)
    students.dropna(subset='name', inplace=True)
    return students
