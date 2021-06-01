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