import GLOBAL_VARIABLES

####################################################
class Thing(object):
	""" Every physical object in the Environment is a thing. """
	
	def __init__(self, PositionXY = None):
		self.PositionXY= PositionXY 
		self.stateOfBeing = 2 	#0 for human, 1 for zombie, 2 Thing
	#

	# __repr__ --> when using print(myThing) the console will print 
	# the package name and the class name
	def __repr__(self):
		return '<%s %s>' % (self.__class__, self.__class__.__name__)
	#

	def GetState(self):
		"""Returns the current state of the being"""
		
		#Human
		if hasattr(self, 'stateOfBeing') and self.stateOfBeing == 0:
			return GLOBAL_VARIABLES.NAME_AGENTHUMAN
		#
		
		#Zombie
		if hasattr(self, 'stateOfBeing') and self.stateOfBeing == 1:
			return GLOBAL_VARIABLES.NAME_AGENTHUMAN
		#

		#Obstacle
		if hasattr(self, 'stateOfBeing') and self.stateOfBeing == 2:
			return GLOBAL_VARIABLES.NAME_OBSTACLE
		#

		#Not defined
		if hasattr(self, 'stateOfBeing') and self.stateOfBeing is not 0 or 1 or 2:
			return GLOBAL_VARIABLES.NAME_NOTDEFINED
		#			
	#	
	
	def GetPosition(self):
		return self.PositionXY
	#

####################################################
class Agent(Thing):
	
	def __init__(self, PositionXY ,health, stateOfBeing = 0):
		#overwrite the position
		self.PositionXY= PositionXY 		
		self.health = health
		self.stateOfBeing = stateOfBeing 	#0 for human 1 for zombie
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
	
	def GetHealth(self):
		return self.health
	#



		
		
		
		
		
		
		
		
		
	#