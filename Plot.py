'''
Created on 21.11.2016

@author: dori
'''

import numpy as np
import matplotlib.pyplot as plt
import Agents as ag
from matplotlib import gridspec
from IPython.core.pylabtools import figsize

import mpl_toolkits.axes_grid1
from matplotlib.colors import LinearSegmentedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size


class Environment_Grid(object):
    
    def AllFields(self, fieldInfo, fieldSizeWidth, fieldSizeHeight):    
                                   
        ##################################
        # Get Information from fieldInfo 
        # So that it can be added to the scatterplot
        ##################################
        
        # AgentTypeI position and health
        lstAgentTypeI_X = []
        lstAgentTypeI_Y = []
        lstAgentHealth = []
        # AgentTypeII position and health
        lstAgentTypeII_X = []
        lstAgentTypeII_Y = []
        lstAgentHealthII = []
        # Sugar position and amount
        lstSugarAmount_X = []
        lstSugarAmount_Y =[]
        
        for index, x in np.ndenumerate(fielpython list integersdInfo):
            # if health is bigger than 0, --> ignore dead agents
            if x[1] is not 0:
                # recognize different agent types 
                if x[0] is 0:
                    lstAgentTypeI_X.append(index[0])
                    lstAgentTypeI_Y.append(index[1])
                    lstAgentHealth.append(x[1])
                if x[0] is 1:
                    lstAgentTypeII_X.append(index[0])
                    lstAgentTypeII_Y.append(index[1])
                    lstAgentHealthII.append(x[1])
            if x[2] is not 0:
                lstSugarAmount_X.append(index[0])
                lstSugarAmount_Y.append(index[1])                   
        # For debugging        
        #print(lstAgentTypeI_X , lstAgentTypeI_Y, lstAgentHealth)        
        
        ##################################
        # Initialization of amounts of sugar
        ##################################
        initialSugarAmounts = np.zeros([fieldSizeWidth,fieldSizeHeight])
        for x in range(fieldSizeWidth):
            for y in range(fieldSizeHeight):
                # Rescale the size of the grid into values in radians: [0,2*pi]
                radX = 2*np.pi*x/fieldSizeWidth
                radY = 2*np.pi*x/fieldSizeHeight
                # Fraction of sugar according to some function
                sugarFrac = abs(np.sin(radX)*np.sin(radY))
                # define sugar amount in (x,y) coordinate
                if radX < np.pi and radY < np.pi:
                    initialSugarAmounts[x,y] = 0
                elif radX > np.pi and radY > np.pi:
                    initialSugarAmounts[x,y] = 0
                else:
                    initialSugarAmounts[x,y] = round(sugarFrac*sugarMax)
                
                
        
        ##################################
        # Sugar (for the imshow() plot)
        ##################################
        amountOfSugarOnAllFields = np.zeros([fieldSizeWidth,fieldSizeHeight])
        
        # get sugar amounts from fieldInfo
        for x in range(fieldSizeWidth):
            for y in range(fieldSizeHeight):
                amountOfSugarOnAllFields[x,y]=fieldInfo[x][y][2]
        #print(amountOfSugarOnAllFields)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        
        ##################################
        # Define the COLORMAPS for the plots
        ##################################
        # sugar
        vmax=3
        cmapSugar = LinearSegmentedColormap.from_list('mycmap', [(0 / vmax, 'white'),
                                                            (1 / vmax, 'yellow'),
                                                            (3 / vmax, 'orange')])
        # Health
        cmapHealth = plt.cm.get_cmap('cool')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       

        
        ##################################
        # The Figure
        ##################################
        figsizeX =10
        figSizeY = 10
        plt.ion()   
        plt.clf()
        
        fig, ax = plt.subplots(figsize=(figsizeX,figSizeY))    # <--
        ax.set_title("Environment",fontsize=14)
        ax.set_xlabel("x",fontsize=12)
        ax.set_ylabel("y",fontsize=12)
        ax.grid(True,linestyle='-',color='0.75')
        ax.set_xlim(-0.5, fieldSizeWidth+0.5-1)
        ax.set_ylim(-0.5, fieldSizeHeight+0.5-1)        
                
        # Scatterplott the Agents Type I
        ax = plt.gca()
        fAgentTypeI = ax.scatter(lstAgentTypeI_X, lstAgentTypeI_Y,                        
                        s=100/figSizeY, #s=lstAgentHealth,
                        c=lstAgentHealth, #color='blue',
                        vmin=0, vmax=10,
                        marker = 's',
                        edgecolor='black', 
                        cmap=cmapHealth,
                        label='Agent TypeI')
        
        # Scatterplott the Agents Type II        
        fAgentTypeII = ax.scatter(lstAgentTypeII_X, lstAgentTypeII_Y,                        
                        s=100/figSizeY, #s=lstAgentHealthII,
                        c=lstAgentHealthII, #color='blue',
                        vmin=0, vmax=10,
                        edgecolor='black', 
                        cmap=cmapHealth,
                        label='Agent TypeII')
        
        # The position of the scatterplot legend of the agents
        ax.legend(scatterpoints=1, bbox_to_anchor=(0,0,-0.05, 1))#loc='lower right')#, bbox_to_anchor=(0,0,-0.05, 1))
        legend = ax.get_legend()
        legend.legendHandles[0].set_color('black')#plt.cm.Blues(.8))
        legend.legendHandles[1].set_color('black')#plt.cm.Greens(.8))
        
        # Adding the colorbar for health
        cbarHealth = plt.colorbar(fAgentTypeI, shrink = 0.5) #orientation='horizontal')
        cbarHealth.set_label('Health of Agent')
        
        # plot the sugar as squares in a raster         
        fSugar = plt.imshow(amountOfSugarOnAllFields, 
                        interpolation='none', 
                        cmap=cmapSugar,
                        vmin=0,
                        vmax=10)
        
        # Adding the colorbar
        cbarAmountSugar = plt.colorbar(fSugar, shrink= 0.5) #fraction=0.046, pad=0.04,#orientation='horizontal')
        cbarAmountSugar.set_label('Amount of sugar') #, rotation=270)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        
        plt.draw()
        plt.ioff()

