import random 
Anumber = random.randrange(1,101)
userInput = int(input("Enter a number: "))
if userInput>Anumber:
    print("Computer number is ",Anumber)
    print("Your guess number is too high")
elif Anumber>userInput:
    print("Computer number is ",Anumber)
    print("Your guess number is too low")
else:
    print("Computer number is ",Anumber)
    print("Your guess number is equal and correct")    