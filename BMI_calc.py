height = input("Enter your height!")
weight = input("Enter your weight!")

fheight = float(height)
fweight = float(weight)

bmi = round(fweight / fheight**2)
n_bmi = int(bmi)

print("Your BMI is: " , n_bmi)

if n_bmi <= 18.5 :
    print("You are underweight.")
elif n_bmi > 18.5 and n_bmi < 25 :
    print("You have a normal weight.")
elif n_bmi >= 25 and n_bmi < 30 :
    print("You are overweight")
elif n_bmi >= 30 and n_bmi < 35 :
    print("You are obese.")
else :
    print("You are clinically obese.")
