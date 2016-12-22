


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
		newPosition = [5,5]
		tmpReturn = [oldPosition, newPosition,5]
		#dropPheromones = [self.xPos, self.yPos] depending on state
		return tmpReturn
	#    

	def GetHealth(self):
		return self.health
	#

	def GetPos(self):
		return [self.xPos,self.yPos]
	#


