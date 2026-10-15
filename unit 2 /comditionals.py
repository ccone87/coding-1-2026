# conditional if/else logic- these are keywords that instruct your
# program to do specific instructions based on specific data
# or conditions 

# conditional syntax (how it is written)
bill_amount = int(input("please type in a bill tender (1,5,10,20)"))

if bill amount = 1:
    print("here are 4 quarters")
# elif allows us to indicate that there are more possible options
# you can have as many elif as you want

#else is always your last option.
# else:
   print("sorry amount entered is not correct") 


def college():
    grade= int(input("please type in your grade:"))
    if grade > 90:
        templeUapp()
    else:
        ccpApp()


def ccpApp():
    print("congrats please complete the templa u app with the following code")
    print("238293")

# using the calculator functions from the calculator.py file,
# create a main calculator function that uses if/else logic to 
# allow the user to select different arithmetic operators and
# then perform those operators by running their respective functions.

# Example: an input where if the user enter1, it will run the addition function.
# 1= addiction()
# 2= subtraction()
# 3= multiplication()
# 4= division()


def calculate_add():
    print("program has started: please type in 2 numbers to add ")
    num1 = int(input())
    num2 = int(input())
    print( num1 + num2)
    print("program has ended ")

    def calculate_muliply():
    print("program has started: please type in 2 numbers to add ")
    num1 = int(input())
    num2 = int(input())
    print( num1 + num2)
    print("program has ended ")

    def calculate_divide():
    print("program has started: please type in 2 numbers to add ")
    num1 = int(input())
    num2 = int(input())
    print( num1 + num2)
    print("program has ended ")

    def calculate_subtract():
    print("program has started: please type in 2 numbers to add ")
    num1 = int(input())
    num2 = int(input())
    print( num1 + num2)
    print("program has ended ")

choice = input("please a number: ")

if choice == '1':
    calculate_add()

if choice == '2':
    calculate_multiply()

if choice == '3':
    calculate_divide()

if choice == '4':
    calculate_subtract()
    

    def movieTicket():
        print("welcome to the movie theater. please type im your age: ") 
        age = input()
        if age <= 7:
            print("your ticket is $8.00.")
        elif age >= 8 and age <= 20    
            print('your ticket is $20.00')
        elif age >= 61:
            print("your ticket is free")    
        else:
            print("sorry there was an error in the program...")    

movieTicket()          















