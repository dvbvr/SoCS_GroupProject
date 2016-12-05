

####################################################
class Agent:
    
	def __init__(self, xPos, yPos ,health):
		self.xPos = xPos
		self.yPos = yPos
		self.health = health
	#
	
	def Move(self, grid):
        # change position
		oldPosition = [self.xPos, self.yPos]
		newPosition = []
		tmpReturn = [oldPosition, newPosition]
        #dropPheromones = [self.xPos, self.yPos] depending on state
		return tmpReturn
	#    
        
	def GetState(self):
		state = self.stateOfBeing
		return state
	#
    
    def GetHealth(self):
        return self.health
    #
	
            
    



        
