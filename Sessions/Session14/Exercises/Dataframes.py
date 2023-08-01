import pandas as pd

products = ['Apple', 'Banana', 'Carrot', 'Daikon']
products_series = pd.Series(products)
print(products_series)

prices_series = pd.Series([2, 1, 3, 4])
print(prices_series)

data = {"Products": products_series, "Prices": prices_series}
data_frame = pd.DataFrame(data)
print(data_frame)

data = [{"Products": "Apple", "Price": 2}, 
        {"Products": "Banana", "Price": 1}, 
        {"Products": "Carrot", "Price": 3},
        {"Products": "Daikon", "Price": 4}]
data_frame = pd.DataFrame(data)
print(data_frame)