

def check_the_result(number):
    if number > 90:
        return f"{number} the grade is A."
    elif number > 80:
        return f"{number} the grade is B."
    elif number > 70:
        return f"{number} the grade is C."
    else :
        return f"{number} the grade is D."
    
number = float(input("Enter the mark: "))
result = check_the_result(number)
print(result)