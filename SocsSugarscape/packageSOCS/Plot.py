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
    
    def Grid(terrainInfo, fieldSizeWidth, fieldSizeHeight, PlotDelay):    
                                   

        # terrainInfo[nestPheromone, foodPheromone, food]
        # [0 = NoAgent 1 = Agent,     AgentSate 0:foraging 1:ReturningHome,     foodAmount]
                
        # Plot agent state:
        # [AgentState, food]

        # AgentForaging position and state        
        npaAgentForagingPosX = np.array([])
        npaAgentForagingPosY = np.array([])
        npaAgentState = np.array([])

        # AgentForaging position and state        
        npaAgentRetHomePosX = np.array([])
        npaAgentRetHomePosY = np.array([])
        npaAgentState = np.array([])
                
        # Sugar position and amount
        npaFoodAmount_X = np.array([])
        npaFoodAmount_Y = np.array([])
        npaFoodAmount = np.array([])


        ##################################
        # Get Information from terrainInfo,
        # so that it can be added to the scatterplot.
        # AgentState, foodAmount
        ##################################
        for y in range(fieldSizeWidth):
            for x in range(fieldSizeWidth):
                # if Agent is 0, --> no agent at this position
                if terrainInfo[y,x,0] >= 1: 
                    if terrainInfo[y,x,1] == 0: #foraging 
                        npaAgentForagingPosX = np.append(npaAgentForagingPosX, np.array([x]))
                        npaAgentForagingPosY = np.append(npaAgentForagingPosY, np.array([y]))
                        npaAgentState = np.append(npaAgentState, terrainInfo[x,y,1])
                    #
                    if terrainInfo[y,x,1] == 1: 
                        npaAgentRetHomePosX = np.append(npaAgentRetHomePosX, np.array([x]))
                        npaAgentRetHomePosY = np.append(npaAgentRetHomePosY, np.array([y]))
                        npaAgentState = np.append(npaAgentState, terrainInfo[x,y,1])
                    #
                #
            #
        #
        
        
        
        ####################################################################
        # Get the amount of sugar from terrainInfo for the imshow plot)
        ####################################################################
        npaFoodAmount = np.zeros([fieldSizeWidth,fieldSizeHeight])        
        # get sugar amounts from terrainInfo
        for y in range(fieldSizeWidth):
            for x in range(fieldSizeHeight):
                npaFoodAmount[x,y]=terrainInfo[x][y][2]
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        
        
        ##################################
        # Define the COLORMAPS for the plots
        ##################################
        # sugar
        #=======================================================================
        # vmax=3
        # cmapSugar = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'white'),
        #                                                     (1 / vmax, 'yellow'),
        #                                                     (3 / vmax, 'orange')])
        # # Health
        # cmapHealth = plt.cm.get_cmap('cool')
        #=======================================================================
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       

        
        
        ##################################
        # The Figure
        ##################################
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
        ax.set_xlim(-0.5, fieldSizeWidth+0.5-1)
        ax.set_ylim(-0.5, fieldSizeHeight+0.5-1)        
                                
        # Scatterplott the AgentForaging
        fAgentTypeI = ax.scatter(
                        npaAgentForagingPosY, npaAgentForagingPosX,                      
                        s=80, 
                        #c=npaAgentState,
                        #vmin=0, vmax=10,
                        marker = 's',
                        edgecolor='black', 
                        #cmap=cmapHealth,
                        label='Agent foraging')

        # Scatterplott the AgentRetHome
        #=======================================================================
        # fAgentTypeII = ax.scatter(
        #                 npaAgentRetHomePosY, npaAgentRetHomePosX,                      
        #                 s=80, 
        #                 #c=npaAgentState,
        #                 #vmin=0, vmax=10,
        #                 marker = 's',
        #                 edgecolor='black', 
        #                 #cmap=cmapHealth,
        #                 label='Agent returning to the nest')
        #=======================================================================
        
        #=======================================================================
        # # The position of the scatterplot legend of the agents
        # ax.legend(scatterpoints=1, bbox_to_anchor=(0,0,-0.05, 1))
        # legend = ax.get_legend()
        # legend.legendHandles[0].set_color('black')
        # #legend.legendHandles[1].set_color('black')
        # 
        # # Adding the colorbar agent state
        # cbarHealth = mainFigure.colorbar(fAgentTypeI, shrink = 0.5)
        # cbarHealth.set_label('Sate of Agent')
        #=======================================================================
        
        # plot the sugar as squares in a raster         
        fSugar = ax.imshow(
                        npaFoodAmount, 
                        interpolation='none', 
                        #cmap=cmapSugar,
                        vmin=0,
                        vmax=10)
        
        # Adding the colorbar
        cbarAmountSugar = mainFigure.colorbar(fSugar, shrink= 0.5) 
        cbarAmountSugar.set_label('Amount of food')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        plt.draw()
        plt.pause(PlotDelay)
        plt.ioff()  


