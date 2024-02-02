# Instructions. Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small pizza (S): $15. Medium pizza (M): $20. Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2. Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1

print("Thank you for choosing Python Pizza Deliveries!")
size = input("S, M, L?\n")
add_pepperoni = input("Pepperoni? Y or N?\n")
extra_cheese = input("Extra Cheese? Y or N?\n")
bill = 0
if size =="S": #an if, elif and else statement could have been used here
    bill +=15
if size =="M":
    bill +=20
if size =="L":
    bill +=25
if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3
if extra_cheese == "Y":
    bill +=1
print(f"Your final bill is ${bill}.")
