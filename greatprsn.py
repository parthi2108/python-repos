def greatperson (name="user"):
    print (f"Hello,{name} ") 
    
greatperson ("Alice")
greatperson()
         
def prime_num (numbers):
     for num in numbers:
          if num %2 == 0 or num %3 == 0 or num %5 == 0:
               print(f"{num} is  prime Number")
          else:
               print(f"{num} Not a Prime number")
               
numbers = [23, 13, 15, 27, 233, 567, 244, 789, 567]
prime_num (numbers)

