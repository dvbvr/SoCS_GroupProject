'''
Created on 27.11.2016

@author: dori
'''

import numpy as np

      
class Initialize:        
    
    def Fields(fieldSizeWidth, fieldSizeHeight):
        
        fieldInfo = np.zeros((fieldSizeHeight, fieldSizeWidth), dtype=object)
        
        for y in range(fieldSizeHeight):
            for x in range(fieldSizeWidth):
                fieldInfo[y][x] = [0,0,0] # [AgentType, Health, SugarAmount]
            #    
        #
        return fieldInfo
    #