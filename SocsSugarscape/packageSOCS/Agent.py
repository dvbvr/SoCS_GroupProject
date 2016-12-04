

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
		return tmpReturn
	#    

	def ChangeHealth(self, amountHealthAlteration):
		self.health = self.health + amountHealthAlteration
		return self.health
	#
        
	def GetState(self):
		state = self.stateOfBeing
		return state
	#
	
            
    



        
