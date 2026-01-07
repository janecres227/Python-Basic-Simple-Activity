num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Choices for operation
print("=" * 30)
print("CHOOSE AN OPERATION")
print("=" * 30)
print("- Addition")
print("- Subtraction")
print("- Multiplication")
print("- Division")
print("- Floor Division")
print("- Modulo")
print("- Exponentiation")

#Get user's choice for operation
choice = int(input("Enter your choice (1/2/3/4/5/6/7): "))

#Perform calculation
if choice == 1:
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif choice == 2:
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif choice == 3:
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif choice == 4:
    if num1 != 0 and num2 !=0:
     result = num1 / num2
     print(f"{num1} / {num2} = {result}")
    else:
     print("Error: Division by zero is not allowed.")   
elif choice == 5:
    if num1 != 0 and num2 != 0:
     result = num1 // num2
     print(f"{num1} // {num2} = {result}")
    else:
     print("Error: Division by zero is not allowed.")
elif choice == 6:
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
elif choice == 7:
    result = num1 ^ num2
    print(f"{num1} ^ {num2} = {result}")
else:
    print("Invalid choice!!!")
    
 
