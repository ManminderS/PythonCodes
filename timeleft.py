
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.



# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = 90 * 365 - int(age) * 365
Weeks = 90 * 52 - int(age) * 52
months = 90 * 12 - int(age) * 12
print(f"You have {days} days, {Weeks} weeks, {months} months left")



# or 

yrs_remaining = 90 - int(age)
days_remaining = yrs_remaining * 365
weeks_remaining = yrs_remaining * 52
month_remaining = yrs_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {month_remaining} months left.")
