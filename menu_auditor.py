"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""


def read_menu():
    menus = {}
    try:
        with open("menu.txt", "r") as file:
            for line in file:
                parts_of_line = line.strip().split(":")
                category = parts_of_line[0].strip()
                detail = parts_of_line[1].strip()
                menus[category] = detail
            return menus
    except FileNotFoundError as e:
        print(e)


def split_into_variables(menu_items):
    crust = menu_items.get("CRUST")
    size = menu_items.get("SIZE")
    toppings = menu_items.get("TOPPINGS")
    drinks = menu_items.get("DRINKS")
    return crust, size, toppings, drinks


def print_menu(crust, size, toppings, drinks):
    print("\n[][][][][][][][][][][][]")
    print("     Casper's Pizzeria    ")
    print("[][][][][][][][][][][][][]")
    print("\nCrust options:")
    for item in crust.split(" , "):
        print(f"\t{item.strip()}")
    print("\nSize options:")
    for item in size.split(" , "):
        print(f"\t{item.strip()}")
    print("\nToppings options:")
    for item in toppings.split(" , "):
        print(f"\t{item.strip()}")
        print("\nDrinks options:")
    for item in drinks.split(" , "):
        print(f"\t{item.strip()}")


def main():
    menu_items = read_menu()
    crust, size, toppings, drinks = split_into_variables(menu_items)
    print_menu(crust, size, toppings, drinks)


main()
