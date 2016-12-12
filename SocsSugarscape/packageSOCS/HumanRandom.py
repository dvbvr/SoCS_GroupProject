import numpy as np
from Agent import Agent
#human  that walkes randomly also eats all the sugar.
####################################################
class HumanRandom(Agent):
	def __init__(self, xPos, yPos, health):
		super().__init__(xPos, yPos, health)
		self.maxHealth = health
		self.state = 0
		self.dirList = np.array([[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]])
		self.direction = np.random.random_integers(0,7) #should be random
	#

	def Move(self, grid):
		focusOnPheroParameter = 10
		oldPosition = [self.xPos,self.yPos]
		modS = np.shape(grid)[0]
		pheroParameter = 1
		currPos = np.array([self.xPos, self.yPos])
		weights = np.array([1,2,3,2,1])
		# if see sugar go there
		if (self.state == 0):
			if grid[self.xPos][self.yPos][1] < 100*((self.health/self.maxHealth)**5):
				grid[self.xPos][self.yPos][1] = 100*((self.health/self.maxHealth)**5)
			noSugar = True
			for i in range(8):
				[x,y] = currPos + self.dirList[i]
				#checks for sugar and go there
				# WARNING!!
				# this next line doesn't work!!! but the rest should be ok...
				if grid[x%modS][y%modS][2] > 0:
					self.xPos = x%modS
					self.yPos = y%modS
					noSugar = False
					#[x,y] = sugar position			
			if noSugar:
				bestPhero = 0
				bestI = 2
				for i in range(5):
					[x,y] = currPos + self.dirList[(self.direction+i-2)%8]
					if (grid[x%modS][y%modS][0] > bestPhero):
						bestI = i
						bestPhero = grid[x%modS][y%modS][0]
				weights[bestI] = focusOnPheroParameter
				totWeight = np.sum(weights)	
				picked = np.random.random_integers(0,totWeight-1)
				for i in range(5):
					if picked < weights[i]:
						[x,y] = currPos + self.dirList[(self.direction+i-2)%8]
						self.xPos = x%modS
						self.yPos = y%modS
						self.direction = self.direction+i-2
						break
					else:
						picked -= weights[i]			
				#look for food pheromones
		else:
			if (grid[self.xPos][self.yPos][0] < 3):
				grid[self.xPos][self.yPos][0] += 1
			bestPhero = 0
			bestI = 2
			for i in range(5):
				[x,y] = currPos + self.dirList[(self.direction+i-2)%8]
				if (grid[x%modS][y%modS][1] > bestPhero):
					bestI = i
					bestPhero = grid[x%modS][y%modS][1]
			weights[bestI] = focusOnPheroParameter
			totWeight = np.sum(weights)	
			picked = np.random.random_integers(0,totWeight-1)
			for i in range(5):
				if picked < weights[i]:
					[x,y] = currPos + self.dirList[(self.direction+i-2)%8]
					self.xPos = x%modS
					self.yPos = y%modS
					self.direction = self.direction+i-2
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
		self.direction = (self.direction+4)%8
		self.health = self.maxHealth
	#
	        
	def GetState(self):
		return self.state
	#
