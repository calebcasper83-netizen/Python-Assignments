"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 4 inputs have 'while' loop validation.
[ ] 3. The Chaperone loop uses .upper() and correct Boolean logic.
[ ] 4. I have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
"""

# Input validation
# First & Last name
first_name = input("Enter your first name:")
while first_name == "":
    print("Error: Name cannot be blank.")
    first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
while last_name == "":
    print("Error: Last name cannot be blank.")
    last_name = input("Enter your last name:")
# Chaperone validation
chaperone = input("Are you willing to chaperone? (Y/N): ").upper()
while chaperone != "Y" and chaperone != "N":
    print("Error: You must only enter Y or N")
    chaperone = input("Are you willing to chaperone? (Y/N): ").upper()
# Phone Number Validation
phone_number = int(input("Enter your phone number:"))
while phone_number == "":
    print("Error: Phone number cannot be blank.")
    phone_number = int(input("Enter your phone number:"))
# Ticket count
tickets = 0
while True:
    try:
        tickets = int(input("How many tickets would you like?"))
        if tickets > 0:
            break
        print("Error: There must be at least one ticket")
    except ValueError:
        print("Error please enter a number")

print(f"Welcome {first_name} {last_name}.")
if chaperone == "Y":
    print("You are willing to chaperone!")
else:
    print("You are not willing to chaperone")
print(f"Your number of tickets is {tickets}")
