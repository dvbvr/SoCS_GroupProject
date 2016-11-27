import numpy as np
from Agent import Agent
#human  that walkes randomly does not take in to consideration any obstacles for now
####################################################
class HumanRandom(Agent):
	def __init__(self, xPos, yPos, health):
		super().__init__(xPos, yPos, health)
		self.stateOfBeing = 0;
	#

	def Move(self, grid): 
        # change position 
		oldPosition = [self.xPos, self.yPos]
		xNew = self.xPos + np.random.random_integers(-1,1)
		yNew = self.yPos + np.random.random_integers(-1,1)
		modS = np.shape(grid)[0]
		newPosition = [xNew%modS,yNew%modS]
		tmpReturn = [oldPosition, newPosition]
		return tmpReturn
	# 
            
    


