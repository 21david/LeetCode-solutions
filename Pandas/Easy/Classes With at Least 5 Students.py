import pandas as pd

# Using value_counts()
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # value_counts() to get number of students in each class
    class_counts = courses['class'].value_counts().reset_index()
    
    # Only keep classes with at least 5 students
    big_classes = class_counts[class_counts['count'] >= 5]

    # Return just the class column as a DF
    return big_classes[['class']]


# Using groupby() and size()
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by to get number of students in each class
    class_counts = courses.groupby(by='class', as_index=False).size()
    
    # Only keep classes with at least 5 students
    big_classes = class_counts[class_counts['size'] >= 5]

    # Return just the class column as a DF
    return big_classes[['class']]


# groupby() and count()
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by to get number of students in each class
    class_counts = courses.groupby(by='class', as_index=False)['student'].count()
    
    # Only keep classes with at least 5 students
    big_classes = class_counts[class_counts['student'] >= 5]

    # Return just the class column as a DF
    return big_classes[['class']]
