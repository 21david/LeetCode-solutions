import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Remove non-February-2020 rows
    orders = orders[(orders.order_date >= '2020-02-1') & (orders.order_date <= '2020-02-29')]

    # Group by month and product it to aggregate total sales for each one
    product_totals = orders.groupby('product_id', as_index=False)['unit'].sum()

    # Filter out products with less than 100 sales that month
    product_totals = product_totals[product_totals.unit >= 100]

    # Join products table to get the names
    return product_totals.merge(products)[['product_name', 'unit']]
