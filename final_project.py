"""
ASSIGNMENT 9B: SPRINT 2 - FUNCTIONAL STUBS
Project: Ghost's Pizzeria
Developer: Caleb Casper
"""

TOPPINGS = ("Pepperoni (+$1.00)", "Sausage (+$1.00)", "Bacon (+$2.00)", "Cheese")
STYLE = ("Thin", "Regular", "Deep dish")
DRINK = ("Water", "Coke (+$2.00)", "Tea (+$2.00)")


def get_customer_info():
    name = input("Please enter your name:")
    location = input("Please enter a location for your order:")
    return name, location


def take_order():
    print("--Welcome to Ghost's Pizzeria!--")
    size = (
        input("Please select a size for your pizza (Small/Medium/Large):")
        .title()
        .strip()
    )
    print("Toppings (Additional fees may apply.): ", TOPPINGS)
    toppings = input("Please select a topping for your pizza:").title().strip()
    print("Styles: ", STYLE)
    style = input("Please select a style: ").title().strip()
    print("Drinks (Additional fees may apply.): ", DRINK)
    drink = input("Please select a drink:").title().strip()
    delivery_choice = input("Please choose either pickup or delivery: ").title().strip()
    finalize_order = input(
        "Type 'C' to confirm your order (Or type E to edit, and X to cancel):"
    )
    return size, toppings, drink


def calculate_total(size, toppings, drink):
    if size == "Small":
        size_total = 3.00
    elif size == "Medium":
        size_total = 5.00
    else:
        size_total = 6.00

    if toppings == "Bacon":
        topping_total = 2.00
    elif toppings == "Pepperoni" or toppings == "Sausage":
        topping_total = 1.00
    else:
        topping_total = 0

    if drink == "Water":
        drink_total = 0
    else:
        drink_total = 2.00

    total = drink_total + topping_total + size_total
    return total


def order_summary(name, location, cost):
    print("--Order Summary--")
    print(f"Customer name: {name}")
    print(f"Location: {location})")
    print(f"Order total: ${cost:.2f}")


def main():
    name, location = get_customer_info()
    size, toppings, drink = take_order()
    total = calculate_total(size, toppings, drink)
    order_summary(name, location, total)


main()
