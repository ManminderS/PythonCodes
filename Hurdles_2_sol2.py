'''
Alternate Solution to Problem listed on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

using while and if statement

'''

def xem():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
        
while not at_goal():
    if front_is_clear() == True:
        move()
    else:
        xem()  
