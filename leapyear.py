
def check_the_year(number):
    if number % 4:
        return f"{number} this is a leap year."
    elif number % 100:
        return f"{number} this is a leap year."
    else :
        return f"{number} this is not a leap year."
    
number = float(input("Enter the year: "))
result = check_the_year(number)
print(result)


def check_the_year(number):
    if number % 400 == 0:
        return f"{number} this is a leap year."
    elif number % 100 == 0:
        return f"{number} this is a leap year."
    elif number % 4 == 0:
        return f"{number} this is a leap year."
    else :
        return f"{number} this is not a leap year."
    
number = float(input("Enter the year: "))
result = check_the_year(number)
print(result)
