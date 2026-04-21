cart = []
n = int(input("Enter number of items: "))
for i in range(n):
    item = input(f"Enter item {i+1} name: ")
    cart.append(item)
print("Cart Items:", cart)
unique_items = set(cart)
print("Unique Items:", unique_items)
total_cost = 0
print("\nEnter prices for each unique item:")
for item in unique_items:
    while True:
        try:
            price = float(input(f"Enter price for {item}: "))
            if price < 0:
                print("Price cannot be negative. Try again.")
                continue
            total_cost += price
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
print("\nTotal Cost:", total_cost)