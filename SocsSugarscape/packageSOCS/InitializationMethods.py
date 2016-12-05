'''
Created on 27.11.2016

@author: dori
'''

import numpy as np

      
class Initialize:        
    
    def Fields(width, height):
        # m=row
        #n=column
        
        terrainInfo = np.zeros((height, width,3))
        
        for m in range(height):
            for n in range(width):
                terrainInfo[m][n] = [0,0,0] # [0 = NoAgent 1 = Agent, AgentSate 0:foraging 1:ReturningHome, foodAmount]
            #    
        #
        return terrainInfo #np.array
    #