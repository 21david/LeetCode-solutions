import pandas as pd

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
