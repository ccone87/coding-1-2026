# loop - a loop is a coonstruct (special function) that repeats itself
# in programming, a loop allows to repeat code instructions.  

# there are two types of loop: For loop and while loop

# While loop - a type of loop where so long as a condidtion is equal
# to true it will keep running forever. 

# the keyword is while --> do while


# syntax
num = 4
while 2+2 == num: # condition --> operations
    # print(num == 4)
    print("the program is running...")
    num = (input()


# while loops will always run unless you change the condition!
# we can do this by writing instructions to manually change it. 

def guessingGame():
    correctanswer= 10
    userguess= int (input("please type in a number to geuss:"))

    while usergeuss != correctanswer:
        print("sorry that incorrect ")
        print("try again...")
        attempts +=1
        print("number of attempts:" + str(attempts))
        userGuess= int(input("please tyoe in a number to guess:"))

    print("congratulations! you guessed correctly! ")    
    print("do you want to try again")

     


def password():
  print("please type in your password")
  print("please try again")
  print("try again password incorrect")


  def passwordreset():
      correctpw = 123abc
      attempts= 4

    if attempts > 0:

      print("please log in with your password")
      userpwattempt = input()

      while userpwattempt != correctpw:
      print("sorry incorrect")
      print("please try again")
      attempts-=1
      print("number of attempts left: '+str(attempts))
      userPWAttempt = input()

  print("welcome you have access...")
elif attempts <=1:




passwordReset()  

            


