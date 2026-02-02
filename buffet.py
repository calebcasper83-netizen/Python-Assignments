"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator
DATE: 02/02/2026
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask user for their age (convert to int).
2. Use if/elif/else to determine price:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Print the final price formatted as currency (e.g., $16.95).
-----------------------------------------------------------------------
"""

# Asking user for their age
age = float(input("What is your age?: "))
# If the age is under 1 the buffet is free.
if age < 1:
    cost = float(0.00)
# If age is 1 to 11 it is $1 per year of age
elif age <= 11:
    cost = float(1.00 * age)
# If age is 12 to 64 it is the standard adult price
elif age <= 64:
    cost = float(16.95)
# Anyone 65 or older will receive a senior discount
else:
    cost = float(12.95)
# Final price
print(f"The cost of the buffet is: ${cost:.2f}")
