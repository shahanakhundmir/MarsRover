## Strategy 👷‍♀️
⭐ Approached task using TDD

⭐ Separation of Concerns

    🟣 Validation of inputs and movements
  
    🟣 Moving the Rover
  
    🟣 Formatting the data for output in specified format
    
⭐ Dividing Areas of Concern into functions and writing a failing unit test for each function. Then coding the solution for that function
   
⭐ Building these functions into the main body of the challenge
 


## Mars Rover Challenge :oncoming_automobile:

### Cases to check ✔️
:star: Collision - if the current rover is at the same position that a previous rover mission ended at, then a collision has occured
  Print a message about the collision and abort the mission

:star: Before the rover starts its journey and after each move, check that the rover is still on the plateau
  If not then print an error message and abort the mission

:star: If initial plateau coordinates are (0,0) an error has occured and the mission cannot continue

:star: Check initital compass direction is N, S, E or W

:star: Check that move is L, R or M 



## Written using Python 🐍



## Testing 📑
:star: Tests have been carried out on isolated functions

:star: Thorough testing of edge cases, including collision, valid inputs and the rover remaining on the plateau

:star: Testing checks if missions are aborted and error messages returned

:star: If more than one rover is on a mission, a list of outputs is returned

:star: Output is a dictionary item for each rovers final position, with coordinates and compass direction

:star: Error messages are string with Mission aborted and reason why. 

:star: The Rover Missions dictionary format output is converted to String as per the specification and printed to screen





## To Run 🏃‍♂️
💻 Download and Install Python from https://www.python.org/downloads/

📂 GitHub - create a folder on your local computer and from the command line run 

git clone https://github.com/shahanakhundmir/MarsRover.git

📁 Open the created folder in VS Code

:star: Control + Shift + P - and select pytest as testing framework

🧪 From Left sidebar the test symbol should appear, click on this to see all tests

Run tests from this section : ✔️ means that tests are running



