import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    cross = students.merge(subjects, how='cross')

    test_counts = examinations.groupby(['student_id', 'subject_name'], as_index=False).size()

    total_counts = (
        cross
            .merge(test_counts, on=['student_id', 'subject_name'], how='left')
            .sort_values(by=['student_id', 'subject_name'])
            .rename(columns={'size': 'attended_exams'})
    )
    
    total_counts.attended_exams = total_counts.attended_exams.fillna(0)

    return total_counts
