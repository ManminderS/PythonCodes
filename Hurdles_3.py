"""

Solution to Reeborg's World Hurdles 3 listed on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

using while and If

"""

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
    if wall_in_front() == True:
        xem()        
        
        
