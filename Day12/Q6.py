data = [[1, 2, 3], [4, 5], [6]]
flattened = [num for sublist in data for num in sublist]
even_squares = [num**2 for num in flattened if num % 2 == 0]
print("Flattened list:", flattened)
print("Even squares:", even_squares)