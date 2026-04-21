import pandas as pd
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
total_sales = S1 + S2
grand_total = total_sales.sum()
print("Total Sales per fruit:")
print(total_sales)
print("\nGrand Total Sales:", grand_total)