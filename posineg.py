
def check_the_number(number):
    if number > 0:
        return f"{number} is a positive number."
    elif number < 0:
        return f"{number} is a negative number."
    else :
        return f"{number} is zero."
    
number = float(input("Enter a number: "))
result = check_the_number(number)
print(result)
