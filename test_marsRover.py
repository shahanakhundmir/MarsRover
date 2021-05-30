import marsRover

def test_checkPlateau_isnotNull():
    assert marsRover.isPlateauValid((0,0)) == False
    assert marsRover.isPlateauValid((5,5)) == True


    
