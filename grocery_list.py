print("Welcome to the Grocery List Program")

# Get initial items
add_count = int(input("Number of items to add: "))
grocery_list = []
for _ in range(add_count):  
    item = input("Enter item to add: ").lower()  # Convert to lowercase for case-insensitive matching
    grocery_list.append(item)

grocery_list.sort()

# Display initial list
print("\nYour grocery list:")
for item in grocery_list:
    print(item)
print("List length:", len(grocery_list), "items")

# Remove items (improved loop)
while True:  # Keep asking until the user chooses to stop
    remove_request = input("\nRemove items? (Y/N): ").lower()

    if remove_request == "y":
        item_to_remove = input("Enter item to remove (or type 'done' to finish): ").lower()

        while item_to_remove != 'done':
            if item_to_remove in grocery_list:
                grocery_list.remove(item_to_remove)
                print(f"Removed '{item_to_remove}' successfully.")
            else:
                print(f"We couldn't find '{item_to_remove}' in your list.")

            item_to_remove = input("Enter item to remove (or type 'done' to finish): ").lower()

        break  # Exit the removal loop if the user enters 'done'

    elif remove_request == "n":
        break  # Exit the removal loop if the user doesn't want to remove items
    else:
        print("Invalid input. Please enter Y or N.")  # Handle invalid input

# Display final list
grocery_list.sort()
print("\nYour updated grocery list:")
if grocery_list:  # Check if the list is empty
    for item in grocery_list:
        print(item)
else:
    print("Your list is empty.")

print("List length:", len(grocery_list), "items")
