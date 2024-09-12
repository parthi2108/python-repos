def find_max(numbers)

if not (numbers)
return none 

max_number = numbers[0]

for number in numbers[1:]:
     if number > max_number:
          print ("This number is the max number")
     else :
          print ("This number is smaller")
     
return max_number
          

numbers = [10,20,45,98,200,333]
max_value = find_max(numbers)
print(f"The max value is: {max_value}")

def find_max(numbers):

    if not numbers:
        return None  


    max_number = numbers[0]


    for number in numbers[1:]:
        if number < max_number:
            print("This number is the max number") 
        else:
            print("This number is smaller")  
    return max_number


numbers = [10, 20, 45, 98, 200, 333]


max_value = find_max(numbers)


print(f"The max value is: {max_value}")


def find_max (numbers):
    if not numbers: 
       return None

    max_number = numbers[0]

    for number in numbers [1:]:
       if number >0 :
        print ("The number is bigger")
       else :
        print ("This number is smaller")
        
    return max_number    

numbers = [25, 35, 44, 100]
max_value = find_max(numbers)
print(f"the max val is: {max_value}")





    

