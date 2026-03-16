"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")


# TODO: Define get_price(size)
def get_price(size):
    if size == "Small":
        return 2.00
    elif size == "Medium":
        return 3.00
    else:
        return 4.00


# TODO: Define blend(size, base, fruit, scoops)
def blend(size, base, fruit, scoops):
    print("\nBlending smoothie...")
    print(f"Size: {size}")
    print(f"Order: {base} with {scoops} scoops of {fruit}")


# TODO: Define main() to collect input and call your logic
def main():
    print("Welcome to Casper's Smoothies!")
    drink_size = input("Choose a size (Small/Medium/Large): ").title().strip()
    print("Bases:", BASES)
    drink_base = input("Choose a smoothie base: ")
    print("Fruits:", FRUITS)
    drink_fruit = input("Choose a fruit: ")
    try:
        drink_scoops = int(input("How many scoops of fruit?: "))
    except:
        print("Invalid entry, defaulting to 1 scoop.")
        drink_scoops = 1
    cost = get_price(drink_size)
    blend(drink_size, drink_base, drink_fruit, drink_scoops)
    print(f"Total Bill: ${cost:.2f}")


main()
