'''
edge cases : 
            


planning : 
            * first line defines plateau, after that several rovers can be 
            delopyed, so every 2 lines represents a rover
            * What type of error messages should be give
            * Each rover is a dictinary object
            * multiple rovers can be appended to a list which maintains the 
            position of each rover on the plateau, incase of collision

'''


def marsRoverChallenge(plateau, rover, movements):

    if isPlateauValid(plateau) and isRoverOnPlateau(plateau, rover) and isDirectionValid(rover):
        for move in movements:
            if move == "R" or move == "L":
                changeRoverDirection(rover, move)
            elif move == "M":
                moveRoverForward(rover)
            else:
                print("Error")
        # check rover is on plateu
        # check rover hasn't collided  
    return rover


def isPlateauValid(plateau):
    return plateau != (0,0)


def isRoverOnPlateau(plateau, rover):
    return plateau[0]>=rover.get('x') and plateau[1]>=rover.get('y')
   

def isDirectionValid(rover):
    return rover.get('direction') == 'N' or rover.get('direction') == 'E' or rover.get('direction') == 'S' or rover.get('direction') == 'W'


def changeRoverDirection(rover, newDirection):
    if newDirection == 'R':
        if rover.get('direction') == 'N': 
            rover['direction'] = 'E'
        elif rover.get('direction') == 'E': 
            rover['direction'] = 'S'
        elif rover.get('direction') == 'S': 
            rover['direction'] = 'W'
        elif rover.get('direction') == 'W': 
            rover['direction'] = 'N'

    elif newDirection == 'L':
        if rover.get('direction') == 'N': 
            rover['direction'] = 'W'
        elif rover.get('direction') == 'E': 
            rover['direction'] = 'N'
        elif rover.get('direction') == 'S': 
            rover['direction'] = 'E'
        elif rover.get('direction') == 'W': 
            rover['direction'] = 'S'
    return rover


def moveRoverForward(rover):
    if rover.get('direction') == 'N':
        rover['y'] = rover.get('y') + 1
    elif rover.get('direction') == 'S': 
        rover['y'] = rover.get('y') - 1
    elif rover.get('direction') == 'E': 
        rover['x'] = rover.get('x') + 1
    elif rover.get('direction') == 'W': 
        rover['x'] = rover.get('x') -1
    return rover