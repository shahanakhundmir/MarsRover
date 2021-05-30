'''
edge cases : 
            * collision
            * going beyound the plateau
            * plateau of 0,0 given - non existent
            * check start position is in plateau
            * check initital compass direction is N S E W
            * check that input is L R M 
            * What maximum number of rovers deployed at any one time


planning : 
            * first line defines plateau, after that several rovers can be 
            delopyed, so every 2 lines represents a rover
            * What type of error messages should be give
            * Each rover is a dictinary object
            * multiple rovers can be appended to a list which maintains the 
            position of each rover on the plateau, incase of collision

'''


def marsRoverChallenge():

    # take input from user or test file
    # first line will be plateau size
    # rover challenge will be in sets of 2 lines
    # first line is start point 
    # second line is movements    
    # check for next rover


    # hard code input for plateau
    p= (5,5)
    rover1 = {'x':1, 'y': 2, 'direction' : 'N'}

    # input for rover position
    # set the rovers position
    # check that this is within the plateau
    
    # get input of movements
    # apply movements to rover
    # return final position

    return

# if the defined plateau is 0,0 should throw an error
def isPlateauValid(plateau):
    return plateau != (0,0)


# if the rover starts from or moves to a position outside the plateau, error
def isRoverOnPlateau(plateau, rover):
    return plateau[0]>=rover.get('x') and plateau[1]>=rover.get('y')
   

# check if rover's initial direction is a valid compass value
def isDirectionValid(rover):
    return rover.get('direction') == 'N' or rover.get('direction') == 'E' or rover.get('direction') == 'S' or rover.get('direction') == 'W'


# change the rovers compass direction based upon an input
def changeRoverDirection(rover, newDirection):
    
    if newDirection == 'R':
        if rover.get('direction') == 'N': rover['direction'] = 'E'
        elif rover.get('direction') == 'E': rover['direction'] = 'S'
        elif rover.get('direction') == 'S': rover['direction'] = 'W'
        elif rover.get('direction') == 'W': rover['direction'] = 'N'

    elif newDirection == 'L':
        if rover.get('direction') == 'N': rover['direction'] = 'W'
        elif rover.get('direction') == 'E': rover['direction'] = 'N'
        elif rover.get('direction') == 'S': rover['direction'] = 'E'
        elif rover.get('direction') == 'W': rover['direction'] = 'S'

    return rover



def moveRoverForward(rover):
    return rover