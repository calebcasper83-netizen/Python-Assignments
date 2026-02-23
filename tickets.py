"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""

# Creating a list of 20 seats numbered (1-20)
seats = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
]

# Loop continues as long as there are seats available to be purchased.
while len(seats) > 0:
    print(f"Avaliable seats: {seats}")
    choice = int(input("Enter seat number to purchase (0 to quit): "))
    # Option to quit
    if choice == 0:
        print("See you next time!")
        break
    # Purchasing of the seat and removing it once sold
    if choice in seats:
        seats.remove(choice)
        print(f"Seat {choice} sold!")
    else:
        print(f"Sorry the seat you selected is not avaliable!")
        choice = int(input("Enter seat number to purchase (0 to quit): "))
# Determining if any seats are available in the list
if len(seats) == 0:
    print("Seats are all sold out")
