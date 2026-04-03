import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Group by customer_number and get the number of orders made by each one, sorted ascending
    # Note: This returns a series since its just one column
    order_amts = orders.groupby('customer_number')['order_number'].count().sort_values()

    # Get the customer with the most orders, still a series
    winner = order_amts.tail(1)
    
    # reset_index() turns it back into a dataframe with two columns (customer_number which is a group, and order_number for that group)
    # Using a list instead of just a column to index in gives a dataframe with just the winning customer's id
    final_ans = winner.reset_index()[['customer_number']]

    return final_ans
