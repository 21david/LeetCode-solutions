import pandas as pd

# Approach: Create a function and use apply()
def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    parents = set(tree.p_id.unique().dropna())

    def get_type(row):
        if pd.isna(row.p_id):
            return 'Root'
        elif row.id in parents:
            return 'Inner'
        return 'Leaf'

    tree['type'] = tree.apply(get_type, axis=1)  # axis=1 sends each row instead of columns

    return tree[['id', 'type']]

# -----------------------------------------------------

# Approach: Using df.loc[ <condition aka mask>, <column> ] = <new value>
def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # Get unique set of parents
    parents = set(tree.p_id.unique().dropna())

    # Set all as Leaf. Parents and Root will be overwritten later.
    tree['type'] = 'Leaf'

    # Set nodes that are parents as inner nodes
    tree.loc[ tree['id'].isin(parents) , 'type'] = 'Inner'

    # Set the one root node (no parent) as root. This needs to be done last because
    # it is also just a parent, so the line above would overwrite this as 'Inner' if done after
    tree.loc[ tree['p_id'].isnull(), 'type'] = 'Root'

    return tree[['id', 'type']]

# -----------------------------------------------------

# Experiment using Python features, beats 91%+
def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # Uniques in p_id gives all parent nodes
    parents = set(tree.p_id.unique().dropna())
    all_nodes = set(tree.id.unique())

    # If only one node, just return that one as root
    if not parents:
        return pd.DataFrame({
            'id': list(all_nodes),
            'type': 'Root'
        })

    # Find all leaf nodes by subtracting sets
    leaves = all_nodes - parents

    # Find root node by finding the only one with null p_id, and separate it from the others
    root = tree[tree.p_id.isna()]
    root = root.id[0]
    parents.remove(root)

    # Now we have each type in its own group, create the final dataframe
    data = {
        'id': [root, *parents, *leaves],
        'type': ['Root']
    }
    data['type'].extend(['Inner'] * len(parents))
    data['type'].extend(['Leaf'] * len(leaves))

    return pd.DataFrame(data)
