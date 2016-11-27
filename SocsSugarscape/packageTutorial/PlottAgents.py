'''
Created on 08.11.2016

@author: dori
'''
import numpy as np
import matplotlib.pyplot as plt
import Agents as ag
from matplotlib import gridspec
from IPython.core.pylabtools import figsize

class PlotIntoScatter:
    def PlottAgents(self, AllFields, nRasterDimension,
                    lst_nGeneration=None, lst_nIndSusceptibles=None, 
                    lst_nIndInfected=None, lst_nIndRecovered=None,
                    nDiffusionRate_d = None, nGamma = None, nBeta = None
                    ):


        #========================================
        # Plott the vlaues
        #========================================
        # initialize class
        myAgentGetter = ag.GetListOfAgents()

        plt.ion()
        figsize=(21, 7)
        figname='Task1'
        plt.figure(figname,figsize)
        plt.figure(figname)
        gs = gridspec.GridSpec(1, 2, 
                                width_ratios=[1, 2])
                                #height_ratios=[1,1])
        
        plt.clf()
        plt.draw()
        plt.axis([0, nRasterDimension, 0, nRasterDimension])
        #ax1 = plt.subplot(121)
        ax1 = plt.subplot(gs[0])
        #ax1.figsize=(10,10)
        ax1.set(title=r'Lattice')
        ax1.set(xlabel=r'x', ylabel=r'y')
        ax1.set_aspect('equal')
        
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
            #ax2 = plt.subplot(122)
            ax2 = plt.subplot(gs[1])
            ax2.set(title = 'd = %s ; gamma = %s ; beta = %s ;' % (nDiffusionRate_d, nGamma, nBeta))
            ax2.set(xlabel=r'Iteration', ylabel=r'Population density')
            ax2.set_color_cycle(['blue', 'red', 'green'])
            ax2.set_aspect('auto')
            
            plt.plot(lst_nGeneration, lst_nIndSusceptibles)
            plt.plot(lst_nGeneration, lst_nIndInfected)
            plt.plot(lst_nGeneration, lst_nIndRecovered)
    
            plt.draw()
            plt.pause(0.005)
            plt.ioff()  
            plt.savefig(figname + '.pdf')
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
    
    
    
        
        
        
        