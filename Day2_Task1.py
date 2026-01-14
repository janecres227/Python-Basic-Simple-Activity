#Getting inputs from users
while True:
    try:
        age = int(input("Enter your age: "))

        if age < 0 or age >= 130:
            print("Invalid age. Please enter a valid age between 0 and 129.")
        else:
            break   # exit loop if age is valid

    except ValueError:
        print("Invalid input. Please enter numbers only.")

#Initiallization
has_license = ""

#Categories base on the users input
if age >= 0 and age <= 12:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teen")
elif age >= 20 and age <= 64:
    print("Adult")
elif age >= 65 and age < 130:
    print("Senior Citizen")
else:
    print("Invalid input")
    
#Asking users if they acquire a valid drivers license
#Actions they can do base on the user age and eligibility 
if age < 18:
    print("You are too young to drive")

else:
    while True:
        license_input = input("Do you have a driver's license? (yes/no): ").strip().lower()

        if license_input == "yes":
            has_license = True
            break
        elif license_input == "no":
            has_license = False
            break
        else:
            print("Invalid input. Please enter only 'yes' or 'no'.")
    print("You are qualified to vote")

    if has_license:
        print("You can drive")
    else:
        print("You need a valid drivers license to drive")

if age >= 21:
    print("You can drink liquior")

if age >= 65 and age < 130:
    print("You are eligible for senior citizen discount")

    