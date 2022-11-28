'''

Using function to solve the problem on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json using function and for loop

Below is the solution, various function are called in order to make the robot reach its destination

'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def movement():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(1,7):
    movement()
