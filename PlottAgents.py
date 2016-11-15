'''
Created on 08.11.2016

@author: dori
'''
import numpy as np
import matplotlib.pyplot as plt
import Agents as ag
from matplotlib import gridspec

class PlotIntoScatter:
    def PlottAgents(self, AllFields, nRasterDimension, lst_nGeneration=None, lst_nIndSusceptibles=None, lst_nIndInfected=None, lst_nIndRecovered=None):


        #========================================
        # Plott the vlaues
        #========================================
        # initialize class
        myAgentGetter = ag.GetListOfAgents()

        plt.ion()
        plt.figure(1)
        plt.figaspect(21.9)
        #gs = gridspec.GridSpec(1, 2, width_ratios=[1, 1]) 
        plt.clf()
        plt.draw()
        plt.axis([0, nRasterDimension, 0, nRasterDimension])
        ax1 = plt.subplot(121)#gs[0])
        #ax1.gca()
        #ax1.set_aspect('equal')
        
        mySAgents = myAgentGetter.AllSusceptiblesSinglesCoordinates(AllFields)
        ## the data
        if mySAgents.size:
            x_S = mySAgents[:,0]
            y_S = mySAgents[:,1]
            plt.scatter(x_S,y_S, color='blue', s=100, edgecolor='none')    
        #

        myRAgents = myAgentGetter.AllRecoveredSinglesCoordinates(AllFields)
        ## the data
        if myRAgents.size:
            x_R = myRAgents[:,0]
            y_R = myRAgents[:,1]
            plt.scatter(x_R,y_R, color='green', s=100, edgecolor='none')
        #

        myIAgents = myAgentGetter.AllRecoveredInfectedCoordinates(AllFields)
        ## the data
        if myIAgents.size:
            x_I = myIAgents[:,0]
            y_I = myIAgents[:,1]
            plt.scatter(x_I,y_I, color='red', s=100, edgecolor='none')
        #
        plt.draw()
        #lt.pause(0.005)
        plt.ioff()
        
        
        
        if lst_nGeneration:  
            plt.ion()
#             plt.clf()
#             plt.draw()
            
            #x = np.linspace(0, 1, 10)
            #fig, ax = plt.subplots()
            ax = plt.subplot(122)#gs[1])#122)
            #ax.set(aspect=1)
            ax.set_color_cycle(['blue', 'red', 'green'])
            #plt.subplot(122)
            plt.plot(lst_nGeneration, lst_nIndSusceptibles)
            plt.plot(lst_nGeneration, lst_nIndInfected)
            plt.plot(lst_nGeneration, lst_nIndRecovered)
    
            plt.draw()
            plt.pause(0.005)
            plt.ioff()  
    #

#     def PlottProportionsOfIndividuals(self, lst_nGeneration, lst_nIndSusceptibles, lst_nIndInfected, lst_nIndRecovered):
#         #Achsenbereich (xmin, xmax, ymax) 
#         plt.ion()
#         plt.figure(1)
#         plt.clf()
#         plt.draw()
#         
#         #x = np.linspace(0, 1, 10)
#         fig, ax = plt.subplots()
#         ax.set_color_cycle(['blue', 'red', 'green'])
#         plt.plot(lst_nGeneration, lst_nIndSusceptibles)
#         plt.plot(lst_nGeneration, lst_nIndInfected)
#         plt.plot(lst_nGeneration, lst_nIndRecovered)
# 
#         plt.draw()
#         plt.pause(0.005)
#         plt.ioff()    
#     #
    
    
    
        
        
        
        