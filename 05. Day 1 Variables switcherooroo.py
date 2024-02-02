This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.

Write a program that switches the values stored in the variables a and b.

# There are two variables, a and b from input
a = input("29")
b = input("42")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)
#"a:" is just a string. c assumes the value of original value of a, a assumes a new value : b, b assumes a new value c
