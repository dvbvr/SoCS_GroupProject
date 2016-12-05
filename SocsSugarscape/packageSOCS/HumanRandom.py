import numpy as np
from Agent import Agent
#human  that walkes randomly also eats all the sugar.
####################################################
class HumanRandom(Agent):
	def __init__(self, xPos, yPos, health):
		super().__init__(xPos, yPos, health)
		self.state = 0
		#self.direction = [1,1] #should be random
		#self.dirList = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
	#

	def Move(self, grid): 
		range = 3;
		#if (self.state == 0):
			#look for food pheromones
		#else
			#look for home pheromones
		
        # change position 
		newPosition = [self.xPos, self.yPos]
		modS = np.shape(grid)[0]
		xNew = (self.xPos + np.random.random_integers(-1,1))%modS
		yNew = (self.yPos + np.random.random_integers(-1,1))%modS
		#self.xPos = xNew
		#self.yPos = yNew
		newPosition = [xNew,yNew]
		self.health -= 1
		tmpReturn = [newPosition, self.health]
		return tmpReturn
	#
	def ChangeState(self, state):
		self.state = state
	#
