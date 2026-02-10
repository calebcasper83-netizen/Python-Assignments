"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Caleb Casper
# While loop
not_arrived = True
while not_arrived:
    print("Are we there yet?")
answer = input("Have you arrived?")
if answer == "yes":
    not_arrived = False
# For Loop (99 Bottles of Beer)
for number in range(99, 0, -1):
    print(f"{number} bottles of beer on the wall!")
