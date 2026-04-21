products = {"Pen": 10, "Notebook": 50, "Pencil": 5} 
categories = {"Stationery", "Office Supplies"}  
cart = []

def calculate_total_recursive(cart_items):
    """Recursive function to compute the total price of all items in the cart."""
    if not cart_items:
        return 0
    
    try:
        return cart_items[0][2] + calculate_total_recursive(cart_items[1:])
    except TypeError:
        raise TypeError("Cart data type error.")

def display_products():
    """Function to display available products."""
    print("Available Products:")
    for name, price in products.items():
        print(f"{name} : {price}")

def add_to_cart():
    """Function to add items to the cart."""
    try:
        name = input("Enter product name: ")
        
        if name not in products:
            raise NameError("Product not found in store.")
            
        quantity_input = input("Enter quantity: ")
        quantity = int(quantity_input)
        
        item_total_price = products[name] * quantity
        item_details = (name, quantity, item_total_price)
        
        cart.append(item_details)
        print("Item added to cart successfully.")
        
    except ValueError:
        print("Invalid quantity! Please enter a number.")
    except NameError:
        print("Product not found in store.")

def view_bill():
    """Function to view cart items and calculate the total bill."""
    try:
        if not cart:
            print("Cart is empty.")
            return
            
        print("Items in Cart:")
        total_quantity = 0
        
        for item in cart:
            print(f"{item[0]} x {item[1]}")
            total_quantity += item[1]
            
        if total_quantity == 0:
            raise ZeroDivisionError("Calculation error: division by zero.")
            
        total_bill = calculate_total_recursive(cart)
        print(f"Total Bill: {total_bill}")
        
    except TypeError:
        print("Cart data type error.")
    except ZeroDivisionError:
        print("Calculation error: division by zero.")

def main():
    """Main menu-driven loop."""
    while True:
        print("1. Display Products")
        print("2. Add Item to Cart")
        print("3. View Total Bill")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            display_products()
        elif choice == '2':
            add_to_cart()
        elif choice == '3':
            view_bill()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
