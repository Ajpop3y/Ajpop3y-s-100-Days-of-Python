# Basically a roller coaster ride with the main determinant being either 120cm or above to be eligble for the ride
# A nested determinant; age is introduced. Different ticket prices are introduced using nested conditionals
# A mid-life crises age was also accounted for. ranges (0-11,12-18, 45-55)
# a photo option was also added
print("Welcome to the roller coaster ride!")
height = int(input("What is your height in centimeters?\n"))
bill = 0
if height >= 120:
    print("You are eligible for the ride!")
    age =int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child ticket is 5$")
    elif age <= 18:
        bill = 7
        print("Youth ticket is 7$")
    elif age >=45 and age <=55:
        print("You get a free ride, you don try")
    else:
        bill = 9
        print("Adult ticket is 9$")
        
    wants_photo = input("Do you want a photo taken? N or Y \n")
    if wants_photo == ("Y"):
      bill += 3
      print(f"Your total bill is ${bill}")
    else:
      print(f"Your total bill is ${bill}")
else:
    print("You need to eat more proteins and vegetables")
    
# The print statement on line 20 is dependent on line 18's if condition.
# While the print statement on 21 isn't. Line 20's print statement can be
# eliminated with no issues
