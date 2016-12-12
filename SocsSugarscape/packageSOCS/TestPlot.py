'''
Created on 27.11.2016

@author: dori
'''
import numpy as np
import matplotlib.pyplot as plt
from SocsSugarscape.packageSOCS.Plot import Environment
from SocsSugarscape.packageSOCS.InitializationMethods import Initialize

#===============================================================================
# Initialize terrain
#===============================================================================
fieldSize = 10
terrain = Initialize.Fields(fieldSize)
PlotDelay = 0.005
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
plot_Ants, AntsFigure = Environment.AntGridFigure(fieldSize)

for i in range(5):
    Environment.AntGridPlot(np.copy(terrain), fieldSize, PlotDelay, plot_Ants, AntsFigure)
plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

