import marsRover
import moveMarsRover
import validateMarsRover


def test_checkPlateau_size_isnotNull():
    assert validateMarsRover.isPlateauValid((0,0)) == False
    assert validateMarsRover.isPlateauValid((5,5)) == True

def test_rover_coordinates_areNotString():
    assert marsRover.marsRoverChallenge((5,5),[({'x':'4', 'y': 3, 'direction' : 'W'},"R")]) == [{'x':4, 'y': 3, 'direction' : 'N'}]
    assert marsRover.marsRoverChallenge((5,5),[({'x':1, 'y': '2', 'direction' : 'N'},"L")]) == [{'x':1, 'y': 2, 'direction' : 'W'}]

def test_checkRover_position_isWithinPlateau():
    assert validateMarsRover.isRoverOnPlateau((5,5), {'x':6, 'y': 2, 'direction' : 'N'}) == False
    assert validateMarsRover.isRoverOnPlateau((5,5), {'x':1, 'y': 2, 'direction' : 'N'}) == True

def test_checkRover__direction_isValid():
    assert validateMarsRover.isDirectionValid({'x':6, 'y': 2, 'direction' : 'N'}) == True
    assert validateMarsRover.isDirectionValid({'x':6, 'y': 2, 'direction' : 'E'}) == True
    assert validateMarsRover.isDirectionValid({'x':6, 'y': 2, 'direction' : 'P'}) == False
    
def test_rover_direction_changeRight():
    assert moveMarsRover.changeRoverDirection({'x':6, 'y': 2, 'direction' : 'N'}, 'R') == {'x':6, 'y': 2, 'direction' : 'E'}
    assert moveMarsRover.changeRoverDirection({'x':6, 'y': 2, 'direction' : 'E'}, 'R') == {'x':6, 'y': 2, 'direction' : 'S'}

def test_rover_direction_changeLeft():
    assert moveMarsRover.changeRoverDirection({'x':6, 'y': 2, 'direction' : 'N'}, 'L') == {'x':6, 'y': 2, 'direction' : 'W'}
    assert moveMarsRover.changeRoverDirection({'x':6, 'y': 2, 'direction' : 'E'}, 'L') == {'x':6, 'y': 2, 'direction' : 'N'}

def test_rover_moveForward_newPosition():
    assert moveMarsRover.moveRoverForward({'x':6, 'y': 2, 'direction' : 'N'}) == {'x':6, 'y': 3, 'direction' : 'N'}
    assert moveMarsRover.moveRoverForward({'x':6, 'y': 2, 'direction' : 'S'}) == {'x':6, 'y': 1, 'direction' : 'S'} 
    assert moveMarsRover.moveRoverForward({'x':6, 'y': 2, 'direction' : 'E'}) == {'x':7, 'y': 2, 'direction' : 'E'}
    assert moveMarsRover.moveRoverForward({'x':6, 'y': 2, 'direction' : 'W'}) == {'x':5, 'y': 2, 'direction' : 'W'} 

def test_rover_seriesOfMoves_newPosition():
    assert marsRover.marsRoverChallenge((5,5),[({'x':4, 'y': 3, 'direction' : 'W'},"RRMRM"),
     ({'x':2, 'y': 2, 'direction' : 'S'},"LMMLM")]) == [{'x':5, 'y': 2, 'direction' : 'S'}, {'x':4, 'y': 3, 'direction' : 'N'}]
    assert marsRover.marsRoverChallenge((5,5),[({'x':1, 'y': 2, 'direction' : 'N'},"LMLMLMLMM"),
     ({'x':3, 'y': 3, 'direction' : 'E'},"MMRMMRMRRM")]) == [{'x':1, 'y': 3, 'direction' : 'N'}, {'x':5, 'y': 1, 'direction' : 'E'}]

def test_rover_notOnPlateau_errorMessage():
    assert marsRover.marsRoverChallenge((5,5),[({'x':4, 'y': 3, 'direction' : 'W'},"RRMRM"),
     ({'x':4, 'y': 4, 'direction' : 'E'},"MMLM")]) == [{'x':5, 'y': 2, 'direction' : 'S'}, 'Mission Aborted - Rover is no longer on the plateau']

def test_rover_collision_errorMessage():
    assert marsRover.marsRoverChallenge((5,5),[({'x':4, 'y': 3, 'direction' : 'W'},"RRMRM"),
     ({'x':5, 'y': 1, 'direction' : 'E'},"LMM")]) == [{'x':5, 'y': 2, 'direction' : 'S'}, 'Mission Aborted - Collision has occured']

def test_rover_invalidMove_errorMessage():
    assert marsRover.marsRoverChallenge((5,5),[({'x':4, 'y': 3, 'direction' : 'W'},"RRWRM"),]) == ['Mission Aborted - Invalid move']

    