# Pizza calc

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S , M or L?")
add_pepperoni = input("Dou you want pepperoni?")
extra_cheese = input("Do you want extra cheese?")

bill = 0

if size == "S" :
    bill += 15
    if add_pepperoni == "Y" :
        bill += 2   
elif size == "M" :
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
else :
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
        
if extra_cheese == "Y" :
    bill += 1   
    
f_bill = f"Your final bill is: ${bill}"

print(f_bill)