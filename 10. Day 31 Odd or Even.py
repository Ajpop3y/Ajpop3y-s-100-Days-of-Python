# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# therefore: 6 % 2 = 0
# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.
# therefore: 5 % 2 = 1

number = int(input("10"))
if number % 2 == 0:
  # % = modulo, if helps to find the remainder after 
  # a division. == (exactly equal to)
  print("This is an even number.")
else:
  print("This is an odd number.")
