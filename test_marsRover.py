import marsRover

def test_checkPlateau__size_isnotNull():
    assert marsRover.isPlateauValid((0,0)) == False
    assert marsRover.isPlateauValid((5,5)) == True

def test_checkRover_position_isWithinPlateau():
    assert marsRover.isRoverOnPlateau((5,5), {'x':6, 'y': 2, 'direction' : 'N'}) == False
    assert marsRover.isRoverOnPlateau((5,5), {'x':1, 'y': 2, 'direction' : 'N'}) == True

def test_checkRover__direction_isValid():
    assert marsRover.isDirectionValid({'x':6, 'y': 2, 'direction' : 'N'}) == True
    assert marsRover.isDirectionValid({'x':6, 'y': 2, 'direction' : 'E'}) == True
    assert marsRover.isDirectionValid({'x':6, 'y': 2, 'direction' : 'P'}) == False
    
def test_rover_direction_changeRight():
    assert marsRover.changeRoverDirection({'x':6, 'y': 2, 'direction' : 'N'}, 'R') == {'x':6, 'y': 2, 'direction' : 'E'}
    assert marsRover.changeRoverDirection({'x':6, 'y': 2, 'direction' : 'E'}, 'R') == {'x':6, 'y': 2, 'direction' : 'S'}

def test_rover_direction_changeLeft():
    assert marsRover.changeRoverDirection({'x':6, 'y': 2, 'direction' : 'N'}, 'L') == {'x':6, 'y': 2, 'direction' : 'W'}
    assert marsRover.changeRoverDirection({'x':6, 'y': 2, 'direction' : 'E'}, 'L') == {'x':6, 'y': 2, 'direction' : 'N'}

def test_rover_moveForward_newPosition():
    assert marsRover.moveRoverForward({'x':6, 'y': 2, 'direction' : 'N'}) == {'x':6, 'y': 3, 'direction' : 'N'}
    assert marsRover.moveRoverForward({'x':6, 'y': 2, 'direction' : 'S'}) == {'x':6, 'y': 1, 'direction' : 'S'} 
    assert marsRover.moveRoverForward({'x':6, 'y': 2, 'direction' : 'E'}) == {'x':7, 'y': 2, 'direction' : 'E'}
    assert marsRover.moveRoverForward({'x':6, 'y': 2, 'direction' : 'W'}) == {'x':5, 'y': 2, 'direction' : 'W'} 
 

def test_rover_seriesOfMoves_newPosition():
    #assert marsRover.marsRoverChallenge((5,5),{'x':1, 'y': 2, 'direction' : 'N'},"LMLMLMLMM"  ) == {'x':1, 'y': 3, 'direction' : 'N'}
    #assert marsRover.marsRoverChallenge((5,5),{'x':3, 'y': 3, 'direction' : 'E'},"MMRMMRMRRM"  ) == {'x':5, 'y': 1, 'direction' : 'E'}
    assert marsRover.marsRoverChallenge((5,5),[({'x':1, 'y': 2, 'direction' : 'N'},"LMLMLMLMM"), ({'x':3, 'y': 3, 'direction' : 'E'},"MMRMMRMRRM")]) == [{'x':1, 'y': 3, 'direction' : 'N'}, {'x':5, 'y': 1, 'direction' : 'E'}]