def marsRoverChallenge(plateau, roverMissions ):
    
    completedMissions = []
    error = 0
    for roverMission in roverMissions:
        rover = roverMission[0]
        movements = roverMission[1]
        if isPlateauValid(plateau) and isRoverOnPlateau(plateau, rover) and isDirectionValid(rover):
            for move in movements:
                if move == "R" or move == "L":
                    changeRoverDirection(rover, move)
                elif move == "M":
                    moveRoverForward(rover)
                    if not isRoverOnPlateau(plateau, rover):
                        completedMissions.append("Mission Aborted - Rover is no longer on the plateau")
                        error = 1
                        break
                    if collisionHasOccured(completedMissions, rover):
                        completedMissions.append("Mission Aborted - Collision has occured")
                        error = 1
                        break
                else:
                    completedMissions.append("Mission Aborted - Invalid move")
                    error = 1
                    break
        # only capture the rovers mission if it has been successful
        if error == 0:     
            completedMissions.append(rover)
    return completedMissions



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


def collisionHasOccured(completedMissions, rover):
    for completedMission in completedMissions:
        if completedMission.get('x') == rover.get('x') and completedMission.get('y') == rover.get('y'):
            return True