'''
Created on 27.11.2016

@author: dori
'''

import numpy as np

      
class Initialize:        
    
    def Fields(fieldSize):
        # m=row
        #n=column
        
        terrainInfo = np.zeros((fieldSize, fieldSize,3))
        
        for m in range(fieldSize):
            for n in range(fieldSize):
                terrainInfo[m][n] = [0,0,0] # [0 = NoAgent 1 = Agent, AgentSate 0:foraging 1:ReturningHome, foodAmount]
            #    
        #
        return terrainInfo #np.array
    #