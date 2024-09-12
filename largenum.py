



def largest_of_numbers(number):
    if number > 100 :
        return f"this is a large number"
    elif number > 200 :
        return f"this is a large number."
    elif number > 300 :
        return f"this is a large number."
    elif number > 400 :
        return f"this is a large number."
    else :
        return f"this is a small number "
    
number = float(input("enter a number : "))
result = largest_of_numbers(number)
print(result)
       