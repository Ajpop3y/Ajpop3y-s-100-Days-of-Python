print("Welcome to the Tip Calculator")
total_bill = float(input("What was the total bill?\n$"))
tip_amount = int(input("What amount of tip will you like to give? 12%?, 15%, 20%?\n"))
total_tipped_bill = ((100 + tip_amount) / 100) * total_bill
tip_ratio = int(input("How many people would you like to split the bill? 5? 7? 9?\n"))
each_pays = round(total_tipped_bill / tip_ratio, 2)
# The above function round() rounded the operation to 2dp by round(x/y, 2)
each_pays = "{:.2f}".format(each_pays)
#The above line forcefully formats the variable in to 2DP "{:.Xf}" where X is the number of decimal places
print(f"Each person pays {each_pays}")
#print(type(each_pays))
