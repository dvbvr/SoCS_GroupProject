'''
Created on 21.11.2016

@author: dori
'''

import numpy as np
import matplotlib.pyplot as plt
import Agents as ag
from matplotlib import gridspec
from IPython.core.pylabtools import figsize
      
class InitializeFields(object):        
    
    def Fields(self, fieldSizeWidth, fieldSizeHeight):        
        
        fieldInfo = np.zeros((fieldSizeHeight, fieldSizeWidth), dtype=object)
        
        for y in range(fieldSizeHeight):
            for x in range(fieldSizeWidth):
                fieldInfo[y][x] = [0,0,0,0] # [nObstacles, nZombies, nHumans, Dead]
            #    
        #
        return fieldInfo
    #

class Plot(object):
    
    def AllFields(self, fieldInfo, fieldSizeWidth, fieldSizeHeight):
    
        lstHumansX = []
        lstHumansY = []
        lstZombiesX = []
        lstZombiesY = []
        lstThingsX = []
        lstThingsY =[]
        
        
        for index, x in np.ndenumerate(fieldInfo):
            if x[0] is not 0:
                lstHumansX.append(index[0])
                lstHumansY.append(index[1])
            if x[1] is not 0:
                lstZombiesX.append(index[0])
                lstZombiesY.append(index[1])
            if x[2] is not 0:
                lstThingsX.append(index[0])
                lstThingsY.append(index[1])        
                
        #print(lstHumansX + lstHumansY)
          
        fig, ax = plt.subplots()
        
        ax.set_title("Environment",fontsize=14)
        ax.set_xlabel("x",fontsize=12)
        ax.set_ylabel("y",fontsize=12)
        
        ax.grid(True,linestyle='-',color='0.75')
        
        ax.set_xlim(0, fieldSizeWidth)
        ax.set_ylim(0, fieldSizeHeight)
        
        ax.scatter(lstHumansX, lstHumansY, color='blue', s=100, edgecolor='none', label='Human')
        ax.scatter(lstZombiesX, lstZombiesY, color='red', s=100, edgecolor='none', label='Zombie') #color='tomato'
        ax.scatter(lstThingsX, lstThingsY, color='gray', s=100, edgecolor='none', label='Thing')
        
        ax.legend(numpoints=1,loc='lower left', bbox_to_anchor=(1.0, 0.5))
        
        plt.show()
    #
