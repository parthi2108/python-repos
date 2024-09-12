

# Function definition to check if a number is even or odd
def    check_odd_even(number)
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."  

Function definition to check if a number is even or odd
def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

# Get input from the user
number = int(input("Enter a number: "))

# Call the function and store the result
result = check_odd_even(number)

# Print the result
print(result)