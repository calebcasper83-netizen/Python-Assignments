"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE LOCKED CALENDAR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. MONTHS is defined as a constant tuple ().
[ ] 3. Program uses a for loop to display each month.
[ ] 4. 'try' and 'except' blocks catch a TypeError.
[ ] 5. Comments explain why the modification failed.

-----------------------------------------------------------------------
"""

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
# Uses a for loop to display each month.
for months in MONTHS:
    print(months)

# Try and except blocks catch a TypeError
try:
    MONTHS[0] = 7
except TypeError:
    print("You cannot modify the months")
# TypeError occurs because tuples cannot be modified.
