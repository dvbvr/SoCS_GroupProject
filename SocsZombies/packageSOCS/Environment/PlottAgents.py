'''
Created on 19.11.2016
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
                    nDiffusionRate_d = None, nGamma = None, nBeta = None,
                    TaskName = None
                    ):


        #========================================
        # Plott the vlaues
        #========================================
        # initialize class
        myAgentGetter = ag.GetListOfAgents()

        plt.ion()
        figsize=(34,9)#21, 7)
        figname='Task1'
        plt.figure(figname,figsize)
        plt.figure(figname)
        gs = gridspec.GridSpec(1, 2, 
                                width_ratios=[1, 2])
                                #height_ratios=[1,1])
        
        plt.clf()
        plt.draw()
        plt.axis([0, nRasterDimension-1, 0, nRasterDimension-1])
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
            susc = ax1.scatter(x_S,y_S, color='blue', s=100, edgecolor='none',label='Susceptible')    
            ax1.set_xlim([0, nRasterDimension-1])
            ax1.set_ylim([0, nRasterDimension-1])

        #

        myRAgents = myAgentGetter.AllRecoveredSinglesCoordinates(AllFields)
        ## the data
        if myRAgents.size:
            x_R = myRAgents[:,0]
            y_R = myRAgents[:,1]
            ax1.scatter(x_R,y_R, color='green', s=100, edgecolor='none', label='Recovered')
            ax1.set_xlim([0, nRasterDimension-1])
            ax1.set_ylim([0, nRasterDimension-1])
        #

        myIAgents = myAgentGetter.AllRecoveredInfectedCoordinates(AllFields)
        ## the data
        if myIAgents.size:
            x_I = myIAgents[:,0]
            y_I = myIAgents[:,1]
            infe = ax1.scatter(x_I,y_I, color='red', s=100, edgecolor='none', label='Infected')
            ax1.set_xlim([0, nRasterDimension-1])
            ax1.set_ylim([0, nRasterDimension-1])
        #
        
        #plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)        
        #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
        #   ncol=3, mode="expand", borderaxespad=0.)        
        #ax1.legend(loc='upper right', bbox_to_anchor=(1.05, 1))        
        leg = ax1.legend(loc='center left', bbox_to_anchor=(1,0.815),numpoints=1)
        
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
            
            plt.plot(lst_nGeneration, lst_nIndSusceptibles, label='Susceptible')
            plt.plot(lst_nGeneration, lst_nIndInfected,label='Infected')
            plt.plot(lst_nGeneration, lst_nIndRecovered,label='Recovered')
    
            #plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
            #    ncol=1, mode="expand", borderaxespad=0.)
            leg1 = ax2.legend(loc='center left', bbox_to_anchor=(1,0.815),numpoints=1)
            
            plt.draw()
            plt.pause(0.005)
            plt.ioff()  
            plt.savefig(figname + '_' + str(len(lst_nGeneration)) +'.png', bbox_extra_artists=(leg,leg1,), bbox_inches='tight')
    #
