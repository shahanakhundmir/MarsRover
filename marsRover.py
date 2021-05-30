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
    return