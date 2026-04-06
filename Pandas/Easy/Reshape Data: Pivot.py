import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    # weather.info()
    # columns=city  =>  take the different values in 'city' and turn them into columns
    # values=temperature  =>  the values for this column will come from the temperature values for each city
    # index=month  => I think it uses month values as the rows and makes it the index
    weather = pd.pivot_table(weather, index='month', columns='city', values='temperature') #, aggfunc='max')
    return weather
