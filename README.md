# Inventory Management System

A command-line application built in Python that allows users to manage a store or warehouse inventory stored in a dictionary.

## Features


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

