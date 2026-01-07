#Getting inputs from the user
name = input(" Enter your first name: ")
last_name = input(" Enter your last name: ")
birth_year = int(input(" Enter your birth year: "))
fav_num = int(input(" Enter your favorite number: "))

#Calculations and concatenation
full_name = name + " " + last_name
age = 2024 - birth_year
last_num = fav_num * 2

#Displaying outputs
print(f"\nMy name is: {full_name}")
print(f"I am {age} years old")
print(f"My number is: {last_num}")
