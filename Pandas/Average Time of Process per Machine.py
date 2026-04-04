import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # Get only start and ends into their own tables, then join to have a start and end column
    starts = activity[activity['activity_type'] == 'start']
    ends = activity[activity['activity_type'] == 'end']
    joined = starts.merge(ends, on=['machine_id', 'process_id'])

    # Calculate processing times for each process
    joined['processing_time'] = joined['timestamp_y'] - joined['timestamp_x']

    # Calculate average processing times for each machine (group by just machine and find averages for processing times)
    average_processing_times = joined.groupby('machine_id', as_index=False)['processing_time'].mean()
    
    # Round to 3
    average_processing_times['processing_time'] = average_processing_times['processing_time'].round(3)

    return average_processing_times
  
# Solved after watching https://youtu.be/LfFkSFcZlSw?t=3272
