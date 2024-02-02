#Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x weeks left.
#Where x is replaced with the actual calculated number of weeks the input age has left until age 90.


age = input("What is your age?\n")
#Weeks = (52 * 90) - (int(age) * 52)
#print((f"You have {Weeks} weeks left"))


year = 90 - int(age)
year *= 52
# note: "*=" is a subtle way of multiplying the variable year by 52. +=, /= also hold true.
print(f"You have {year} weeks left.")

fun
#DAYS, WEEK, MONTH, YEARS LEFT IF LIFE EXPECTANCY = 90
user_age = input("How old are you?\n")
years_left = 90 - int(user_age)
month_left = years_left * 12
week_left = years_left * 52
days_left = years_left * 365
message = f"You have {years_left} years, {month_left} months, {week_left} weeks, {days_left} days left to live (lol)"
print(message)
