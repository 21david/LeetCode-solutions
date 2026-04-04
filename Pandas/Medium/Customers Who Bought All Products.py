import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    # Get total number of products
    num_products = len(product)

    # Get the number of unique products bought by each customer
    nmbt = customer.groupby('customer_id', as_index=False).agg(uniques_bought=('product_key', 'nunique'))

    # Return only the customer_ids that bought all the products
    return nmbt.loc[nmbt.uniques_bought == num_products, ['customer_id']]
