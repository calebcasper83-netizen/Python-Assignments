"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with your name.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Caleb Casper
# Asking the user for two random integers
number_one = int(input("Pick a number:"))
number_two = int(input("Think of a second number:"))

# 6 Logical checks
# Determining if both inputs are greater than 0
if number_one > 0 and number_two > 0:
    print("Your numbers are both positive.")
# Determining if both inputs are greater than 100
if number_one > 100 and number_two > 100:
    print("Your numbers are both greater than 100.")
# Determining if either input is even
if number_one % 2 == 0 or number_two % 2 == 0:
    print("At least one of your numbers is even.")
# Determining if either input is less than 100
if number_one < 100 or number_two < 100:
    print("At least one of your numbers is less than 100.")
# Determining if inputs are not equal
if not (number_one == number_two):
    print("Your numbers are not equal.")
# Determining if inputs are not zero
if not (number_one == 0 or number_two == 0):
    print("Your numbers are both not zero.")

# Categorizing number_one into Positive/Negative/Zero using if/elif/else
if number_one == 0:
    result = "Zero"
elif number_one < 0:
    result = "Negative"
else:
    result = "Positive"

print(f"Your first number is {result}")
