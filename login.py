# import tkinter as tk 
# from tkinter import messagebox

# user_db = {
#     'user1' == 'abcd12345'
# }

# def login ():
#     username = entry_username.get()
#     password = entry_password.get()

#     if username in user_db and user_db[username] == password:
#         messagebox.showinfo("login","login succesful!")
#     else:
#         messagebox.showfinfo("login","User credentials invalid.")
        
# root = tk.Tk()
# root.title = ("loginform ")

# window_width, window_height : 300, 250
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight() 


# a= int(input())
# b= input()
# c= str (a)+b
# print (c)

# a= input("My name is: ")
# b= int(input("My age is: "))
# c= a+ str(b)
# print (c)

# name = input()
# age = input()
# print ("my name is :",name)
# print ("my age is:",age)

# a = int(input())
# b = int(input())
# c = int(input())
# d = a+b+c
# e = a*b*c
# f = d/e

# print (d,e,f)

# name = (input())
# score = int(input())
# print ("My name is :",name)
# print ("My score is:", score/10,"/10")


# fname = input("Enter your name:")
# lname = input("Enter your last name:")
# age = int(input("Enter your age:"))
# address = {"Parthi",23,"Red river street","Texas"}
# phone=[9363565443,9500565161]
# phone1 = {"name":"parthi", "contact":[9363565443,9500565161]}


# print (fname)
# print(lname)
# print(age)
# print(address)
# print(phone[0])

# Data types

# v1 = 24
# v2 = "Prasanna"
# v3 = 75.75
# v4 = ["Prasanna",24,75.5,"TUP"]
# v5 = {"name":"Prasanna","age":24,"weight":75.5,"city":"TUP"}
# v6 = {"name":"Prasanna", "mobiles":[7339351147,9514424430]}

# # print(v6['mobiles'][1])
# print (v5)


comp={
  "company": {
    "name": "Tech Solutions",
    "employees": [
      {
        "id": 1,
        "name": "Alice",
        "age": 30,
        "position": "Software Engineer",
        "skills": ["Python", "JavaScript", "Docker"],
        "salary": 80000
      },
      {
        "id": 2,
        "name": "Bob",
        "age": 28,
        "position": "DevOps Engineer",
        "skills": ["Kubernetes", "AWS", "Ansible"],
        "salary": 85000
      },
      {
        "id": 3,
        "name": "Charlie",
        "age": 32,
        "position": "Data Scientist",
        "skills": ["Python", "SQL", "Machine Learning"],
        "salary": 95000
      }
    ],
    "location": {
      "city": "New York",
      "address": "123 Tech Avenue"
    }
  },
  "projects": [
    {
      "name": "AI Development",
      "deadline": "2024-12-31",
      "team": ["Alice", "Charlie"]
    },
    {
      "name": "Cloud Infrastructure",
      "deadline": "2024-09-30",
      "team": ["Bob"]
    }
  ]
}
# print(comp["projects"][0]["deadline"])
# print(comp["company"]["employees"][2]["salary"])

print(comp["projects"][1]["name"],(comp["projects"][1]["team"]))

print(comp["company"]['employees'][2]['name'])