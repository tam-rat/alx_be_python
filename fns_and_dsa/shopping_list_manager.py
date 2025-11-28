# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print()  # Blank line for readability

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        # Add Item
        if choice == '1':
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the shopping list.\n")
            else:
                print("Item name cannot be empty.\n")

        # Remove Item
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.\n")
            else:
                print(f"'{item}' was not found in the shopping list.\n")

        # View List
        elif choice == '3':
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
                print()
            else:
                print("Your shopping list is currently empty.\n")

        # Exit
        elif choice == '4':
            print("Goodbye!")
            break

        # Invalid input
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
