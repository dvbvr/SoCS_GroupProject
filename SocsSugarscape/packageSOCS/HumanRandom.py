import numpy as np
from Agent import Agent
#human  that walkes randomly also eats all the sugar.
####################################################
class HumanRandom(Agent):
	def __init__(self, xPos, yPos, health):
		super().__init__(xPos, yPos, health)
		self.stateOfBeing = 0;
	#

	def Move(self, grid): 
        # change position 
		oldPosition = [self.xPos, self.yPos]
		newPosition = oldPosition
		modS = np.shape(grid)[0]
		xNew = (self.xPos + np.random.random_integers(-1,1))%modS
		yNew = (self.yPos + np.random.random_integers(-1,1))%modS
		if grid[xNew][yNew][1] == 0:
			self.xPos = xNew
			self.yPos = yNew
			newPosition = [xNew,yNew]
		self.health -= 0.5
		tmpReturn = [oldPosition, newPosition, self.health]
		return tmpReturn
	#
