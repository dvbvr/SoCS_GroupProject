

####################################################
class AgentWithState(object):
    
    def __init__(self, nFieldNumber, xPos, yPos, 
                 nAgentNr,health, stateOfBeing):
        self.xPos = xPos
        self.yPos = yPos
        self.health = health
        self.nAgentNr = nAgentNr 
        self.stateOfBeing = stateOfBeing
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
    #
        
	def GetState(self)
		return self.stateOfBeing
	#
	
            
    



        