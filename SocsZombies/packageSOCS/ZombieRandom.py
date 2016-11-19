import numpy as np
from Agent import Agent
#zombie that walkes randomly does not take in to consideration any obstacles for now
####################################################
class ZombieRandom(Agent):
	def __init__(self, xPos, yPos, health):
		super().__init__(xPos, yPos, health)
		self.stateOfBeing = 1;
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
            
    


