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
    



