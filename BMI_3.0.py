print("Welcome to BMI Calculator")
def bmi(height, weight):
    calc = (weight / height ** 2)
    BMI = round(calc)
    if BMI < 18.5:
        print(f"Your BMI is {BMI}, you are underweight.")
    elif BMI < 25:
        print(f"Your BMI is {BMI}, you have a normal weight.")
    elif BMI < 30:
        print(f"Your BMI is {BMI}, you are slightly overweight.")
    elif BMI < 35:
        print(f"Your BMI is {BMI}, you are obese.")
    else:
        print(f"Your BMI is {BMI}, you are clinically obese.")

height = float(input("Your Height in m: "))
weight = float(input("Your Weight in kg: "))

bmi(height, weight)

