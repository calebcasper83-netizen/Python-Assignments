"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

# Toppings Tuple
TOPPINGS = ("Bacon", "Cheese", "Sausage", "Pepperoni")


def make_pizza(customer, size, topping, is_delivery=False):
    print("--ORDER SUMMARY--")
    print(f"Customer: {customer}")
    print(f"Size: {size}")
    print(f"Topping: {topping}")

    if is_delivery:
        print("Delivery: Yes")
    else:
        print("Delivery: No")


def main():
    print("Avaliable toppings: Bacon, Cheese, Sausage, Pepperoni")
    name = input("Please enter your name:").title()
    size = input("Enter a pizza size (Small/Medium/Large): ")
    topping = input("Please select a topping: ")
    delivery_choice = input("Would you like to deliver? (Yes/No): ")
    if delivery_choice == "Yes":
        delivery = True
    else:
        delivery = False
    make_pizza(customer=name, size=size, topping=topping, is_delivery=delivery)


main()
