# Handles an input with a Value error or a Division by Zero error
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("The result is:",result)
except ValueError:
    print("You must enter a valid integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")

# Handles a Sort error by checking if the previous element is greater than the next
years = [1925, 1943, 1968, 1937, 1975, 1912, 1989, 1954, 1920, 1996]
years.sort()
print(years)
assert years[0] <= years[-1], "First element is greater than last element."
