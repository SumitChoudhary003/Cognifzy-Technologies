num1 = float(input("Enter a first number: "))
num2 = float(input("Enter a second number:  "))
print("Press 1 for addition\nPress 2 for subtraction\nPress 3 for multiply\nPress 4 for division\npress 5 for modulo")
choice = int(input("Enter choices between 1 to 5:"))
if choice == 1:
    print("Addition is: ",num1 + num2)
elif choice == 2:
    print("Subtraction is: ",num1 - num2)
elif choice == 3:
    print("Multiply is: ",num1 * num2)
elif choice == 4:
    print("Division is: ",num1 / num2) 
elif choice == 5:
    print("Modulus is: ",num1 % num2)
else:
    print("Invalid choice from user")           
