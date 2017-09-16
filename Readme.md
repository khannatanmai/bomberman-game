#Welcome to the Bomberman Game!
###	Made by Tanmai Khanna (As SSAD Assignment-1, Roll number 20161212)

##How to Install:

- Ensure that you have python3 installed. If not, run the following: `sudo apt-get install python3`
- Open the directory where you extracted it and run the following command : `pip3 install -r requirements.txt`
- Once this is done, from the terminal, run the file `play_game.py` by the following command: `python3 play_game.py`

##Controls:
- Move Up:	w
- Move Down: 	s
- Move Left: 	a
- Move Right: 	d
- Drop Bomb: 	b
- Quit Game:	q

##Representation:
- Bomberman
	BBBB
	BBBB

- Enemy
	EEEE
	EEEE

- Walls
	####
	####

- Bricks
	%%%%
	%%%%

- Bomb
	[33]
	[33]

##Important Things to Remember:

- The primary objective of the game is to kill the enemy.
- You can drop bombs to achieve this. Once you drop a bomb there will be a countdown to 0 and then it will explode.
- Walls are indestructible and bricks are destructible.
- You score 20 points for each brick you destroy and 100 points for killing the enemy.
- You have 3 lives per game. You will lose a life if you get caught in an explosion. The enemy however will die if caught in an explosion.
- You have 180 seconds to kill the enemy or you lose the game!
- Most Importantly, Enjoy the Game! ^_^

#TECHNICAL DETAILS:

##Object Oriented Programming Principles:

- **Objects** and **Classes** have been used extensively in this code. Every individual entity in the game has been assigned a class which holds the important data as variables and functions which act on this data as member functions.

- **Modularity** has been taken great care of, while writing this code. I have divided the functionality into as many files and functions as I could while maintaining understandability and an easy flow of control.

- While I haven't explicitly made class variables private and used getters and setters, but I read that in Python the reason private and public was removed (can still be done using _) is that programmers should be responsible and careful with their class variables. This can be implemented easily though.

- **Polymorphism** has already been implemented a lot in python functions such as len(), in, +, etc. which can be used for both numbers and strings.

- Throughout the code I didn't feel the need to inherit any classes. Tried making a superclass person for bomberman and enemy but didn't really feel there were commonalities in the two classes which needed to be defined in the person class. The commonality of valid moves existed but I felt it was easier to code the two separately. Hence, I did not force **inheritance** into my code. Would be more than willing to improve upon it for sure!

##Miscellaneous:

- The enemy always spawns in the bottom right corner.

##Formula for Calculation of True Position:
Excluding the outer walls, the board is a 17*17 board if we consider each 2*4 block as one position.

The true position formula is as follows:
- Input: (x,y) in which 0 <= x,y <= 16. These are representative positions on the board.
- Output: [(x1,y1),(x2,y2),...(x8,y8)]. These are actual positions of the 8 bytes on the board and these will contain the specific character of whichever object is at that key position.
