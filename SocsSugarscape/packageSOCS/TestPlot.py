'''
Created on 27.11.2016

@author: dori
'''
import numpy as np
import matplotlib.pyplot as plt
import Plot
import InitializationMethods

##################################
# Initialize fieldInfo
##################################
fieldSizeWidth = 16
fieldSizeHeight = 16 

fieldInfo = InitializationMethods.Initialize.Fields(fieldSizeWidth,fieldSizeHeight)


##################################
# Add some sugar and agents for testing purpose
##################################         

# fieldInfo[X][Y] = [AgentType ^= 0, Health^=1, SugarAmount^=2]

# sugar
fieldInfo[0][0][2] = 10       
fieldInfo[0][1][2] = 10       
fieldInfo[1][0][2] = 10       
fieldInfo[1][0][2] = 8       
fieldInfo[2][4][2] = 2       

# type
fieldInfo[4][2][0] = 0       
fieldInfo[4][4][0] = 0   
fieldInfo[4][3][0] = 1   

# health
fieldInfo[4][2][1] = 2       
fieldInfo[4][4][1] = 10       
fieldInfo[4][3][1] = 6   

##################################
# Initialize fieldInfo
##################################
PlotDelay = 0.005


for i in range(5):
    Plot.Environment.Grid(fieldInfo,fieldSizeWidth, fieldSizeHeight, PlotDelay)

plt.show()
