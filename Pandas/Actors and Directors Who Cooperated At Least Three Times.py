import pandas as pd
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    group_cts = actor_director.groupby(['actor_id', 'director_id'], as_index=False).size()
    return group_cts.loc[group_cts['size'] >= 3, ['actor_id', 'director_id']]

# OR

import pandas as pd
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    group_cts = actor_director.groupby(['actor_id', 'director_id'], as_index=False).size()
    return group_cts[group_cts['size'] >= 3][['actor_id', 'director_id']]

# OR

# Solution using regular Python
import pandas as pd
def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Make a dictionary to count times each actor-director pair worked together
    counts = defaultdict(int)
    for i, row in actor_director.iterrows():
        counts[(row['actor_id'], row['director_id'])] += 1

    # Filter out pairs where they worked together at least 3 times
    new_rows = {'actor_id': [],
                'director_id': []}
    for actor, director in counts:
        if counts[actor, director] >= 3:
            # This pair of actor and director has worked together 
            # at least 3 times, so add to the result dictionary
            new_rows['actor_id'].append(actor)
            new_rows['director_id'].append(director)

    # Put the actor-director pairs in a new dataframe
    res = pd.DataFrame(new_rows)

    return res
