def add_grocery_items():
    print("Enter grocery items (type 'done' to stop):")
 
    with open("grocery.txt","w") as file:
        while True:
            item = input("Enter item: ")
 
            if item.lower() == "done":
                break
 
            file.write(item + "\n")
 
    print("Grocery list saved successfully!")
 
add_grocery_items()
