
"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 35.0
# Number of characters.
numChars = 8
# Color of characters.
color = "Gold"
# Type of wood.
woodType = "Oak"
# Write assignment and if statements here as appropriate.
if numChars <=5:
    charge += 0
if numChars >5:
    charge += (numChars-5) * 4
if color =="Gold":
    charge += 15
if woodType == "Oak":
    charge += 20
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
