from colorama import Fore, Back, init, Style


from colorama import init
init(autoreset=True)

print("=" * 50)
print(Style.BRIGHT + Back.RED + "WELCOME TO USER INFO COLLECTOR")
print("=" * 50)

#Getting inputs from user
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")
phone_num = input("Enter your phone number: ")
city = input("Enter the city that you live in: ")
country = input("Enter your country: ")
occupation = input("Enter your occupation: ")
num_of_programming_language = int(input("Enter the number of programming language that you know: "))
fav_prog_lang = input("Enter your favorite programming language:  ")
years_of_coding_exp = int(input("Enter the number of your coding experience: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

#Calculation base on the inputs from the user
birth_year = 2024 - age
days_since_birth = age * 365.5
full_name = first_name + " " + last_name
average_language_per_year = num_of_programming_language / years_of_coding_exp
coding_exp = years_of_coding_exp / 1
status = "Yes" if is_student else "No"

#Check if the email contains "@" symbol
while "@" not in email:
    print("\nInvalid email address. Email should contain @ symbol. Please try again.")
    email = input("Enter your email: ")

#Validate the phone number if the phone number starts with 0 and 9, and has 11 digit (For Philippines phone number validation)
while not (phone_num.startswith("09") and len(phone_num) == 11 and phone_num.isdigit()):
    print("\nInvalid phone number. Philippine numbers must start with '09' and have 11 digits.")
    phone_num = input("Enter your phone number again: ")

#Calculate and determine coding level
if coding_exp == 0:
 experience_level = "No experience"
elif coding_exp == 1:
 experience_level = "Beginner"
elif coding_exp == 2:
 experience_level = "Intermediate"
else:
 experience_level = "Advance"
 
#Displaying all the information from the user
print()
print("=" * 50)
print(Back.RED + "USER INFORMATION SUMMARY")
print("=" * 50)
print(f"\nName: {full_name}")

#Checking if age is positive number
if age > 0:
 print(f"Age: {age} years old or {days_since_birth} days old since birth(in days)")
else:
 print(f"Age: Invalid age input")

print(f"Birth year: {birth_year}")
print(f"Email: {email}")
print(f"Phone Number: {phone_num}")
print(f"City: {city} Country: {country}")
print(f"Occupation: {occupation}")
print()
print("=" * 50 )
print(Back.RED + "PROGRAMMING EXPERIENCE:")
print("=" * 50 )
print(f"     Languages Known: {num_of_programming_language}")
print(f"     Favorite Languge: {fav_prog_lang}")
print(f"     Years of Experience: {years_of_coding_exp}")
print(f"     Experiece Level: {experience_level}")
print(f"     Avg Languages/Year: {average_language_per_year}")
print(f"     Student Status: {status}")
print(f"\nMessage: Keep up the good work!")

#Saving the collected information into a text file
with open("user_info.txt", "w") as file:
    file.write("USER INFORMATION SUMMARY\n")
    file.write("=" * 50 + "\n")
    file.write(f"Name: {full_name}\n")
    file.write(f"Age: {age} years old or {days_since_birth} days old since birth(in days)\n")
    file.write(f"Birth Year: {birth_year}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Phone Number: {phone_num}\n")
    file.write(f"City: {city} Country: {country}\n")
    file.write(f"Occupation: {occupation}\n\n")

    file.write("PROGRAMMING EXPERIENCE\n")
    file.write("=" * 50 + "\n")
    file.write(f"Languages Known: {num_of_programming_language}\n")
    file.write(f"Favorite Language: {fav_prog_lang}\n")
    file.write(f"Years of Experience: {years_of_coding_exp}\n")
    file.write(f"Experience Level: {experience_level}\n")
    file.write(f"Avg Languages/Year: {average_language_per_year:.2f}\n")
    file.write(f"Student Status: {status}\n")