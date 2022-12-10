'''
Program to Solve the problem mentioned at https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

using While and If/Elif/else


'''

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():  #this while loop is to move the reeborg to move to the nearest wall so that he doesnt get stuck in infinite loop where he has right side clear in all 4 direction(This happens when he is in the middle of the maze)
    move()
turn_left()
   
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
   
