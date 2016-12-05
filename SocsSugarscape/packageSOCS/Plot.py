'''
Created on 21.11.2016

@author: dori
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from IPython.core.pylabtools import figsize

import mpl_toolkits.axes_grid1
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size


class Environment:

	def Grid(terrainInfo, fieldSize, PlotDelay):    
                                   
		AGENTSTATE = 0
		AGENTHEALTH = 1
		SUGARAMOUNT = 2
		#[agentState, agentHealth, sugarAmount]
		#[AgentSate 0:foraging 1:ReturningHome, agentHealth, foodAmount]
                
        # AgentForaging position and state        
		npaAgentForagingPosX = np.array([])
		npaAgentForagingPosY = np.array([])
		npaAgentStateFor = np.array([])
		npaAgentHealthFor = np.array([])

        # AgentRetHome position and state        
		npaAgentRetHomePosX = np.array([])
		npaAgentRetHomePosY = np.array([])
		npaAgentStateRet = np.array([])
		npaAgentHealthRetHome = np.array([])
                
        # Sugar position and amount
		npaFoodAmount_X = np.array([])
		npaFoodAmount_Y = np.array([])
		npaFoodAmount = np.array([])
		
        #=======================================================================
        # Get Information from terrainInfo,
        # so that it can be added to the scatterplot.
        # 
		# Get the amount of sugar from terrainInfo for the imshow plot)
        #=======================================================================
		for y in range(fieldSize):
			for x in range(fieldSize):
				# If HEALTH than there is a agent
				if terrainInfo[y,x,AGENTHEALTH] >= 1: 					
					# Recognise the foraging agent
					if terrainInfo[y,x,AGENTSTATE] == 0: 
						npaAgentForagingPosX = np.append(npaAgentForagingPosX, np.array([x]))
						npaAgentForagingPosY = np.append(npaAgentForagingPosY, np.array([y]))
						npaAgentStateFor = np.append(npaAgentStateFor, terrainInfo[x,y,AGENTSTATE])
                    # Recognise the retruning agent
					if terrainInfo[y,x,AGENTSTATE] == 1: 
						npaAgentRetHomePosX = np.append(npaAgentRetHomePosX, np.array([x]))
						npaAgentRetHomePosY = np.append(npaAgentRetHomePosY, np.array([y]))
						npaAgentStateRet = np.append(npaAgentStateRet, terrainInfo[x,y,AGENTSTATE])
                    #
                #
            #
        #
        # get sugar amounts from terrainInfo
		npaFoodAmount = np.zeros([fieldSize,fieldSize])        
		for y in range(fieldSize):
			for x in range(fieldSize):
				npaFoodAmount[x,y]=terrainInfo[y][x][SUGARAMOUNT]
			#
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        #=======================================================================
        # Define the COLORMAPS for the plots
        #=======================================================================
        # Health
		cmapHealth = plt.cm.get_cmap('cool')
		#Sugar		
		cmapSugar = plt.cm.get_cmap('YlOrRd')#('Blues')#('YlOrRd')
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       

        #=======================================================================
        # The Figure
        #======================================================================= 
		figname='terrain'
		figsizeX =18
		figSizeY = 9                
		figsize=(figsizeX,figSizeY)
		mainFigure = plt.figure(figname,figsize)

		plt.ion()        
		plt.clf()
		plt.draw()
        
		ax = mainFigure.add_subplot(111)        
		ax.set_aspect('equal')
		ax.set_title("Environment",fontsize=14)
		ax.set_xlabel("x",fontsize=12)
		ax.set_ylabel("y",fontsize=12)
		ax.grid(True,linestyle='-',color='0.75')
		ax.set_xlim(-0.5, fieldSize+0.5-1)
		ax.set_ylim(-0.5, fieldSize+0.5-1)        
                                
        # Scatterplott the AgentForaging
		fAgentTypeI = ax.scatter(
                        npaAgentForagingPosY, npaAgentForagingPosX,                      
                        s=80, 
                        c=npaAgentStateFor,
		                #vmin=0, vmax=10, # --> for min and max 
                        marker = 's',
                        edgecolor='black', 
                        cmap=cmapHealth,
                        label='Agent foraging')

        # Scatterplott the AgentRetHome
		fAgentTypeII = ax.scatter(
		                npaAgentRetHomePosY, npaAgentRetHomePosX,                      
		                s=80, 
		                c=npaAgentStateRet,
		                #vmin=0, vmax=10,
		                marker = 'o',
		                edgecolor='black', 
		                cmap=cmapHealth,
		                label='Agent returning to the nest')
        
		# The position of the scatterplot legend of the agents
		ax.legend(scatterpoints=1, bbox_to_anchor=(0,0,-0.05, 1))
		legend = ax.get_legend()
		legend.legendHandles[0].set_color('black')
		legend.legendHandles[1].set_color('black')
		
		# Adding the colorbar agent state
		cbarHealth = mainFigure.colorbar(fAgentTypeI, shrink = 0.5)
		cbarHealth.set_label('Health of Agent')
        
        # plot the sugar as squares in a raster         
		fSugar = ax.imshow(
                        npaFoodAmount, 
                        interpolation='none', 
                        cmap=cmapSugar)
        
        # Adding the colorbar
		cbarAmountSugar = mainFigure.colorbar(fSugar, shrink= 0.5) 
		cbarAmountSugar.set_label('Amount of food')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
		plt.draw()
		plt.pause(PlotDelay)
		plt.ioff()  

