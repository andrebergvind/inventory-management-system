"""
Inventory Management System

A command-line application that allows users to manage a store or
warehouse inventory stored in a dictionary.

The system enables the user to track items, update quantities,
calculate values, identify low-stock items, and perform data
operations through an interactive menu.
"""

inventory = {}


def add_item():
    """
    Prompts the user to add a new item to the inventory
    including name, quantity, and price per unit.
    Validates that the ID is unique and that quantities and
    prices are non-negative numbers.
    """
    print("\nAdding a new item")

    item_id = input("Enter item ID (unique integer): ").strip()
    if not item_id.isdigit():
        print("Please enter a valid integer for the item ID.")
        return

    item_id = int(item_id)
    if item_id in inventory:
        print("Error: Item ID already exists. Try a different ID.")
        return

    item_name = input("Enter item name: ").strip()
    if item_name == "":
        print("Item name cannot be empty.")
        return

    quantity = input("Enter quantity: ").strip()
    if not quantity.isdigit():
        print("Invalid input! Please enter a valid number for the quantity.")
        return

    quantity = int(quantity)
    if quantity < 0:
        print("Quantity cannot be negative.")
        return

    ppu = input("Enter price per unit: ").strip()
    try:
        ppu = float(ppu)
        if ppu < 0:
            print("Price cannot be negative")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number for the price.")
        return

    inventory[item_id] = {
        "name": item_name,
        "quantity": quantity,
        "price": ppu
    }

    print(f"\nItem '{item_name}' added successfully!")


def update_item():
    """
    Allows the user to update the name, quantity, and price of
    an item in the inventory.
    """
    print("\nUpdating Item Details")

    try:
        item_id = int(input("Enter item ID to update: "))
        if item_id not in inventory:
            print("Error: Item not found.")
            return
    except ValueError:
        print("Invalid input.")
        return

    print("Enter new values (press Enter to keep existing values):")

    new_name = input(f'Current name: {inventory[item_id]["name"]} | New Name: ').strip()
    if new_name != "":
        inventory[item_id]["name"] = new_name

    new_quantity = input(f'Current Quantity: {inventory[item_id]["quantity"]} | New Quantity: ').strip()
    if new_quantity != "":
        try:
            new_quantity = int(new_quantity)
            if new_quantity < 0:
                print("Quantity cannot be negative.")
                return
            inventory[item_id]["quantity"] = new_quantity
        except ValueError:
            print("Invalid input! Enter a valid integer for quantity.")
            return

    new_price = input(f'Current Price: {inventory[item_id]["price"]} | New Price: ').strip()
    if new_price != "":
        try:
            new_price = float(new_price)
            if new_price < 0:
                print("Price cannot be negative.")
                return
            inventory[item_id]["price"] = new_price
        except ValueError:
            print("Invalid input! Enter a valid number for price.")
            return

    print("\nItem updated successfully!")


def remove_item():
    """
    Prompts for an item ID and deletes the matching entry
    if it exists.
    """
    print("\nRemoving an Item")

    try:
        item_id = int(input("Enter the ID of the item to remove: ").strip())
        if item_id in inventory:
            del inventory[item_id]
            print("Item removed successfully!")
        else:
            print("Error: Item not found.")
    except ValueError:
        print("Invalid input! Please enter a valid integer ID.")
        return


def view_inventory():
    """
    Exhibits inventory item's ID, name, quantity, price, and total value.
    If no item is present, it prints "No items in inventory".
    """
    print("\nCurrent inventory:")
    if len(inventory) > 0:
        print("-" * 60)
        print(f'{"ID":<7}{"Name":<15}{"Quantity":>5}{"Price":>12}{"Total Value":>18}')
        print("-" * 60)

        for key, value in inventory.items():
            total_value = value["quantity"] * value["price"]
            print(f'{key:<7}{value["name"]:<15}{value["quantity"]:>2}{value["price"]:>19.2f}{total_value:>13.2f}')

        print("-" * 60)
    else:
        print("No items in inventory.")


def check_total_value():
    """
    Displays total value of inventory.
    """
    inventory_value = 0

    for value in inventory.values():
        inventory_value += value["quantity"] * value["price"]

    print(f'Total inventory value: {inventory_value:.2f}')


def find_low_stock():
    """
    Enables the user to identify items with low stock by choosing a threshold.
    """
    print("\nChecking for Low Stock Items")

    try:
        threshold = int(input("Enter the low stock threshold: ").strip())
        if threshold < 0:
            print("Threshold cannot be negative.")
            return

        low_stock_items = []

        for key, value in inventory.items():
            if value["quantity"] < threshold:
                low_stock_items.append(f'- Name: {value["name"]}, ID: {key}, Quantity: {value["quantity"]}')

        if len(low_stock_items) > 0:
            print("\nItems with Low Stock:")
            for item in low_stock_items:
                print(item)
        else:
            print("No items with low stock.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


def main():
    """
    Controls the main program loop by displaying the menu,
    validating user choices, and calling the requested functions.
    """
    while True:
        print("\n1. Add a new item")
        print("2. Update item details")
        print("3. Remove an item")
        print("4. View inventory")
        print("5. Check total inventory value")
        print("6. Find items with low stock")
        print("7. Exit")

        choice = input("\nMake a choice: ").strip()

        try:
            choice = int(choice)

            if choice == 1:
                add_item()
            elif choice == 2:
                update_item()
            elif choice == 3:
                remove_item()
            elif choice == 4:
                view_inventory()
            elif choice == 5:
                check_total_value()
            elif choice == 6:
                find_low_stock()
            elif choice == 7:
                print("Goodbye!")
                break
            else:
                print("Invalid option! Please choose a valid number.")

        except ValueError:
            print("Invalid option! Please choose a valid number.")


if __name__ == "__main__":
    main()
