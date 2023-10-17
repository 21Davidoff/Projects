#Tip calculator 

print("Welcome to the tip calculator.")

bill = input("What was the total bill?")

tipp = input("What percentage tip would you like to give? 10 , 12, or 15?")

people = input("How many people to split the bill?")

fl_bill = float(bill)

fl_people = float(people)

p_tip = float(tipp) / 100

total_tip = (fl_bill / fl_people) * (p_tip + 1)

fl_total_tip = float(total_tip)

tip_person = round(fl_total_tip , 2)

message = f"Each person should pay: {tip_person}"

print(message)