# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:        
    if year % 100 == 0:  
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a Leap year")
    else:
        print("Leap Year")      
else:
    Print("Not Leap")



#Logic for the Leap Year
# If a number is evenly divisble by 4, 100 and 400, its a Leap year
# If a year is evenly divisble by 4 and not evenly divisble by 100: Its a Leap Year
# If a year is evenly divisble by 4 and 100 but not with 400 : Its not a Leap Year
