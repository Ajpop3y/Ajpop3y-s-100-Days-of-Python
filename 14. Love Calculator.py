# You are going to write a program that tests the compatibility between two people. To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be: "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be: "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.: Your score is *z*."

print("This love calculator will calculate your score")
name_1 = input("What is your name?\n")
name_2 = input("What is their name?\n")
name_1_lower = name_1.lower()
name_2_lower = name_2.lower()
t_count = int((name_1_lower + name_2_lower).count("t"))
r_count = int((name_1_lower + name_2_lower).count("r"))
u_count = int((name_1_lower + name_2_lower).count("u"))
e_count = int((name_1_lower + name_2_lower).count("e"))
true_count = str(t_count + r_count + u_count + e_count)

l_count = int((name_1_lower + name_2_lower).count("l"))
o_count = int((name_1_lower + name_2_lower).count("o"))
v_count = int((name_1_lower + name_2_lower).count("v"))
e2_count = int((name_1_lower + name_2_lower).count("e"))
love_count = str(l_count + o_count + v_count + e2_count)

love_score = (true_count + love_count)
love_score_1 = int(love_score)
if love_score_1 < 10 or love_score_1 > 90:
    print(f"Your score is {love_score_1}, you go together like coke and mentos.")
elif love_score_1 >= 40 and love_score_1 <= 50:
    print(f"Your score is {love_score_1}, you are alright together.")
else:
    print(f"Your score is {love_score_1}")
