'''
Created on 27.11.2016

@author: dori
'''
import numpy as np
import matplotlib.pyplot as plt
import Plot
import InitializationMethods

#===============================================================================
# Initialize terrain
#===============================================================================
fieldSize = 10
terrain = InitializationMethods.Initialize.Fields(fieldSize)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#===============================================================================
# Add some sugar and agents for testing purpose
#===============================================================================
# STATE
terrain[4][2][0] = 0 #Foraging       
terrain[4][4][0] = 1 #ReturningHome
terrain[4][3][0] = 1   
# HEALTH
terrain[4][2][1] = 12       
terrain[4][4][1] = 2   
terrain[4][3][1] = 4   
# foodAmount
terrain[4][2][2] = 2       
terrain[4][4][2] = 1       
terrain[4][5][2] = 21   
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#===============================================================================
# # Initialize terrain
#===============================================================================
PlotDelay = 0.005
for i in range(5):
    Plot.Environment.Grid(np.copy(terrain), fieldSize, PlotDelay)
plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

