# Inventory Management System

A command-line application built in Python that allows users to manage a store or warehouse inventory stored in a dictionary.

## Features
- **Add a new item:** Store items with a unique ID, name, quantity, and price per unit.
- **Update item details:** Modify an existing item's name, quantity, or price (or press Enter to keep current values).
- **Remove an item:** Delete an item from the inventory by its ID.
- **View inventory:** Display all items in a formatted table with calculated total values per item.
- **Check total inventory value:** Calculate the combined value of all stock.
- **Find low-stock items:** Search for items whose quantity falls below a chosen threshold.

## How to Run
1. Make sure you have Python 3 installed on your computer.
2. Download or clone this repository to your local machine.
3. Open your terminal in the project folder and run:
   ```bash
   python3 main.py

## Example Usage

**Main Menu & Adding an Item**
```
1. Add a new item
2. Update item details
3. Remove an item
4. View inventory
5. Check total inventory value
6. Find items with low stock
7. Exit

Enter choice: 1

Adding a new item

Enter item ID (unique integer): 101
Enter item name: Keyboard
Enter quantity: 15
Enter price per unit: 49.99

Item 'Keyboard' added successfully!
```
**Viewing the Inventory**
```
Enter your choice: 4

Current inventory:
------------------------------------------------------------
ID     Name           Quantity       Price       Total Value
------------------------------------------------------------
101    Keyboard       15              49.99           749.85
102    Mouse           4              25.50           102.00
------------------------------------------------------------
```
**Checking Total Value & Low-Stock Items**
```
Enter your choice: 5

Total inventory value: 851.85

-------------------------------

Enter your choice: 6

Checking for Low Stock Items
Enter the low stock threshold: 10

Items with Low Stock:
- Name: Mouse, ID: 102, Quantity: 4
```

