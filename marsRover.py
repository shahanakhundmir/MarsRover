def marsRoverChallenge(plateau, roverMovements ):
    arr = []
    for roverMovement in roverMovements:
        rover = roverMovement[0]
        movements = roverMovement[1]
    # refactor to list of rovers, 3
    # get the plateau
    #loop through the rovers
    #store endpoint of each rover journey in list 
    #with each rover move, check it hasn't collided with another rover

        if isPlateauValid(plateau) and isRoverOnPlateau(plateau, rover) and isDirectionValid(rover):
            for move in movements:
                if move == "R" or move == "L":
                    changeRoverDirection(rover, move)
                elif move == "M":
                    moveRoverForward(rover)
                    if isRoverOnPlateau(plateau, rover):
                        continue
                    else:
                      print("Rover is no longer on the plateau")
                else:
                 print("Error")

        # check rover hasn't collided  --- report collision
        arr.append(rover)
    return arr


def isPlateauValid(plateau):
    return plateau != (0,0)


def isRoverOnPlateau(plateau, rover):
    return plateau[0] >= rover.get('x') and rover.get('x') >= 0 and plateau[1] >= rover.get('y') and rover.get('y') >= 0
   

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