"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""


class PizzaOrder:
    def __init__(self, name, location, size, topping, style, drink):
        self.__name = name
        self.__location = location
        self.__size = size
        self.__topping = topping
        self.__style = style
        self.__drink = drink

    # Getters
    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_size(self):
        return self.__size

    def get_topping(self):
        return self.__topping

    def get_style(self):
        return self.__style

    def get_drink(self):
        return self.__drink

    # Setters
    def get_size(self, size):
        if size in ("Small", "Medium", "Large"):
            self.__size = size

    def set_topping(self, topping):
        self.__topping = topping

    def set_drink(self, drink):
        self.__drink = drink

    # Calculating total (for final project)
    def calculate_total(self):
        if self.__size == "Small":
            size_total = 3.00
        elif self.__size == "Medium":
            size_total = 5.00
        else:
            size_total = 6.00
        if self.__topping == "Bacon":
            topping_total = 2.00
        elif self.__topping == "Pepperoni" or self.__topping == "Sausage":
            topping_total = 1.00
        else:
            topping_total = 0
        if self.__drink == "Water":
            drink_total = 0
        else:
            drink_total = 2.00
        return size_total + topping_total + drink_total

    # Order Summary
    def order_summary(self):
        total = self.calculate_total()
        return (
            f"-Order Summary-\n"
            f"Customer name: {self.__name}\n"
            f"Location: {self.__location}\n"
            f"Size: {self.__size}\n"
            f"Topping: {self.__topping}\n"
            f"Order total: ${total:.2f}"
        )


# Two distinct objects.

order1 = PizzaOrder("Caleb", "Huntley", "Large", "Bacon", "Thin", "Coke")
order2 = PizzaOrder("Madeline", "Crystal Lake", "Medium", "Cheese", "Regular", "Water")

print(order1.order_summary())
print(order2.order_summary())
