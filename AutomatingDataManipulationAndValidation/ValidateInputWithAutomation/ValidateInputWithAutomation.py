import pyinputplus as pyip

# Request the number of shopping bags required from an int input
result = pyip.inputInt("Enter number of shopping bags you will need for your items:")
print("\nYou will use", result, "store bags.")

# Request the colour required from a menu input
result = pyip.inputMenu(["red","blue","green"], lettered=True, numbered=False)
print("\nYou have chosen a", result, "marker.")

# Request an email address from an email input
result = pyip.inputEmail("Enter your email address:")
print("\nThe email you entered:", result)