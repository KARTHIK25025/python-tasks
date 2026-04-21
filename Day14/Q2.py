import pandas as pd
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
required_cities = ["Delhi", "Chennai", "Bangalore"]
series = pd.Series(cities, index=required_cities)
missing = series.isna()
print("City Population Series:")
print(series)
print("\nMissing Values (True = missing):")
print(missing)