# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# on every year that is divisible by 4 with no remainder
# except every year that is evenly divisible by 100 with no remainder
# unless the year is also divisible by 400 with no remainder

print("Hello, welcome to the leap year calculator")
year = int(input("What year do you want to check?\n"))
if year % 4 ==0:
    if year % 100 != 0:
        print("Leap year")
    elif year % 100 == 0 and year % 400 == 0:
        print("Leap year")
    elif year % 100 == 0 and year % 400 != 0:
        print ("Not leap year")
else:
    print("Not leap year")
    

#if there's a general conditon need to be met before testing many conditions, use the
#general if condition (for your general condition) first then use the nested if & elif to test specific conditions
    
    
    
    

    
    
    


    
    
#
