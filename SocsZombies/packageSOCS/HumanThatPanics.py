import numpy as np

####################################################
class HumanThatPanics(Agent):
    
    def __init__(self,  xPos, yPos, health):
		super().__init__(xPos, yPos, health)
        self.stateOfBeing = 0;
    #

    def Move(self, grid): # does not take in to consideration any obstacles for now
        # change position 
        oldPosition = [self.xPos, self.yPos]
		xStart = self.xPos
		yStart = self.yPos
		xNew = self.xPos + np.random.random_integers(0,1)
		yNew = self.yPos + np.random.random_integers(0,1)
		modS = np.shape(grid)[0]
		dist = 3
		find = False
		for x in range(0,dist)
			for y in range(0,(dist-x))
				xCurr = (xStart+x)%modS
				yCurr = (yStart+y)%modS
				if grid[xCurr][yCurr][0]>0:
					xNew = self.xPos - np.sign(x)
					yNew = self.yPos - np.sign(y)
					find = True
					break
				xCurr = (xStart+x)%modS
				yCurr = (yStart-y)%modS
				if grid[xCurr][yCurr][0]>0:
					xNew = self.xPos - np.sign(x)
					yNew = self.yPos - np.sign(-y)
					find = True
					break
				xCurr = (xStart-x)%modS
				yCurr = (yStart+y)%modS
				if grid[xCurr][yCurr][0]>0:
					xNew = self.xPos - np.sign(-x)
					yNew = self.yPos - np.sign(y)
					find = True
					break
				xCurr = (xStart-x)%modS
				yCurr = (yStart-y)%modS
				if grid[xCurr][yCurr][0]>0:
					xNew = self.xPos - np.sign(-x)
					yNew = self.yPos - np.sign(-y)
					find = True
					break
			if find: 
				break
        newPosition = [xNew,yNew]
        tmpReturn = [oldPosition, newPosition]
        return tmpReturn
    # 
            
    


