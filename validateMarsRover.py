def isPlateauValid(plateau):
    return plateau != (0,0)

def checkCoordinatedAreValid(rover):
    if type(rover.get('x')) == str:
        rover['x'] = int(rover.get('x'))
    if type(rover.get('y')) == str:
        rover['y'] = int(rover.get('y'))
    return rover

def isRoverOnPlateau(plateau, rover):
    return plateau[0] >= rover.get('x') and rover.get('x') >= 0 and plateau[1] >= rover.get('y') and rover.get('y') >= 0
   
def isDirectionValid(rover):
    return rover.get('direction') == 'N' or rover.get('direction') == 'E' or rover.get('direction') == 'S' or rover.get('direction') == 'W'

def collisionHasOccured(completedMissions, rover):
    for completedMission in completedMissions:
        if completedMission.get('x') == rover.get('x') and completedMission.get('y') == rover.get('y'):
            return True