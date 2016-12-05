import numpy as np
from Agent import Agent
#human  that walkes randomly also eats all the sugar.
####################################################
class HumanRandom(Agent):
	def __init__(self, xPos, yPos, health):
		super().__init__(xPos, yPos, health)
		self.state = 0
		self.dirList = np.array([[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]])
		self.direction = np.random.random_integers(0,7) #should be random
	#

	def Move(self, grid):
		oldPosition = [self.xPos,self.yPos]
		modS = np.shape(grid)[0]
		pheroParameter = 0.01
		currPos = np.array([self.xPos, self.yPos])
		weights = np.array([5,10,20,10,5])
		# if see sugar go there
		if (self.state == 0):
			grid[self.xPos][self.yPos][1] += 1
			noSugar = True
			for i in self.dirList:
				[x,y] = currPos + self.dirList[i]
				print ([x,y])
				#checks for sugar and go there
				# WARNING!!
				# this next line doesn't work!!! but the rest should be ok...
				if grid[x,y][2] != 0:
					self.xPos = x
					self.yPos = y
					noSugar = False
					#[x,y] = sugar position			
			if noSugar:
				for i in range(5):
					[x,y] = currPos + dirList[(self.direction+i-2)%8]
					weights[i] += grid[x%modS][y%modS][0]*pheroParameter
				totWeight = np.sum(weights)	
				picked = np.random.random_integers(0,totWeight-1)
				for i in range(5):
					if picked < weights[i]:
						[x,y] = currPos + dirList[(self.direction+i-2)%8]
						self.xPos = x
						self.yPos = y
						break
					else:
						picked -= weights[i]			
				#look for food pheromones
		else:
			for i in range(5):
				[x,y] = currPos + dirList[(self.direction+i-2)%8]
				weights[i] += grid[x%modS][y%modS][1]*pheroParameter
			totWeight = np.sum(weights)	
			picked = np.random.random_integers(0,totWeight-1)
			for i in range(5):
				if picked < weights[i]:
					[x,y] = currPos + dirList[(self.direction+i-2)%8]
					grid[self.xPos][self.yPos][0] += 1
					self.xPos = x
					self.yPos = y
					break
				else:
					picked -= weights[i]
			#look for home pheromones
		
        # change position 
		
		newPosition = [self.xPos,self.yPos]
		self.health -= 1
		tmpReturn = [newPosition, oldPosition, self.health]
		return tmpReturn
	#
	def ChangeState(self, state):
		self.state = state
	#
	        
	def GetState(self):
		return self.state
	#
