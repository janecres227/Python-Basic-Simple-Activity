age = int(input("How old are you? "))
has_license = input("Do you have any driver's license?(Yes/No:) ")

#Compariason and logical
if age >= 18 and has_license.lower() =="yes":
    print(f"You {age} and has license, then you can drive")
    
elif age >= 18 and has_license.lower() =="no":
    print("You are old enough to get a driver's license!!")
else:
    print("You are a minor")
#Checking if the user is senior citizen
if age >= 60:
    print("You are a senior citizen..")
else:
    print("You are not a senior citizen..")
#Checking if the user can vote
if age >= 18:
    print("You can vote. And please vote wisely..")
else:
    print("You are not old enough to vote..")

        