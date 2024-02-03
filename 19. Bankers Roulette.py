# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Line 1 splits the string names_string into individual names and puts them inside a List called names.
# For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

name_string = input("Give names separated by comma\n")
name_list = name_string.split(', ')
# name_string has changed from a string to a list thanks to line 2
name_indices_boundary = len(name_list)-1
#it is len(name_list)-1 because the number obatined is 1 higher than the elements indices number in
# a list. Why? Indices number start from zero
import random
random_name_int = random.randint(0,name_indices_boundary)
random_name = (name_list[random_name_int])
print(f"{random_name} is going to buy the meal today!")
print(random_name_int)
#print(random_name)
