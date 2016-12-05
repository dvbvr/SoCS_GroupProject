'''
Created on 27.11.2016

@author: dori
'''
import numpy as np
import matplotlib.pyplot as plt
import Plot
import InitializationMethods

##################################
# Initialize terrain
##################################
fieldSizeWidth = 10
fieldSizeHeight = 10

terrain = InitializationMethods.Initialize.Fields(fieldSizeWidth,fieldSizeHeight)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##################################
# Add some sugar and agents for testing purpose
##################################         
# terrain[X][Y] = # [0 = NoAgent 1 = Agent,     AgentSate 0:foraging 1:ReturningHome,     foodAmount]


# IsThereAnAgent
terrain[4][2][0] = 0 #No       
terrain[4][4][0] = 1 #Yes  
terrain[4][3][0] = 1   
# state
terrain[4][2][1] = 0       
terrain[4][4][1] = 0   
terrain[4][3][1] = 1   
# foodAmount
terrain[4][2][2] = 5       
terrain[4][4][2] = 10       
terrain[4][3][2] = 6   

##################################
# Initialize terrain
##################################
PlotDelay = 0.005

for i in range(5):
    Plot.Environment.Grid(np.copy(terrain), fieldSizeWidth, fieldSizeHeight, PlotDelay)

plt.show()
