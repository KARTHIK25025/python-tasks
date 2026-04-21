import numpy as np

prices = [499, 299, 799, 199, 599]

prices_array = np.array(prices)

sorted_prices = np.sort(prices_array)

print("Sorted Prices (Ascending):", sorted_prices)