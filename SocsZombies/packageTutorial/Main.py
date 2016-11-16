'''
Created on 07.11.2016

@author: dori
'''



#========================================
# Import
#========================================
import numpy as np
import matplotlib.pyplot as plt
import Agents as ag
import RandomWalk as rw
import PlottAgents as plag
import ChangeAgentStatus
#=========================
#http://stackoverflow.com/questions/409370/sorting-and-grouping-nested-lists-in-python
from pprint import pprint as pp
#from itertools import *
import itertools
import operator
##############################################################################


#========================================
# Create the fields for the plot
#========================================
#
# Raster:    I****I
# f.e. 4x4   I****I
#            I****I
#            I****I
nRasterDimension =50
#========================================
# Individuals
#========================================
nIndividualsSusceptibles_S = 450
nIndividualsInfected_I = 10
nIndividualsRecovered_R = 0
nIndividualsAll_N = nIndividualsSusceptibles_S + nIndividualsInfected_I + nIndividualsRecovered_R
#========================================
# For the RandomWalk
#========================================
nDiffusionRate_d = .3 #Where the diffusionRate is in [0,1[
#========================================
# Change Agent status
#========================================
nGamma = 0.005    # healing rate      (I --> R)
nBeta = 0.2       # transmission rate (S --> I)
#========================================
# Set iteration variables here
#========================================
nIterations =200
PLOT_AGENTS_EVERY_N = 100

plt.close("all")
######################################################################



#========================================
# Initialize xPos and yPos of fields
#========================================
# List containing all the fields <-- nRasterDimension * nRasterDimension        
AllFields = []
for i in range(nRasterDimension):

    for j in range(nRasterDimension):
        tmpMyAgent = ag.AgentsOnField(j+i*nRasterDimension, i,j)
        AllFields.append(tmpMyAgent)
    #


        
#========================================
# Randomly add the SIR Agents to the raster fields
#========================================
nStart = 0
# initialize class
myInitAgent = ag.IntitializeAgents()
# S Agents
myInitAgent.InitializeSAgentsRandomly(AllFields, nRasterDimension, nIndividualsSusceptibles_S, nStart)
# R Agents
myInitAgent.InitializeRAgentsRandomly(AllFields, nRasterDimension, nIndividualsRecovered_R, nIndividualsSusceptibles_S)
# I Agents
myInitAgent.InitializeIAgentsRandomly(AllFields, nRasterDimension, nIndividualsInfected_I, nIndividualsInfected_I + nIndividualsSusceptibles_S)
#initialize class
#check results:
# myPrintAgent = ag.PrintAgents()
# myPrintAgent.PrintAllAgentsInConsole(AllFields)



#========================================
# Plot the values
#========================================
myAgentPlotter = plag.PlotIntoScatter()
myAgentPlotter.PlottAgents(AllFields,nRasterDimension)
    
##############################################################################



#========================================
# List in which the numbers of SIR-Agents
# will be stored every Generation
#========================================
lstSIRAgentsInGeneration = []
lstSIRAgentsInGeneration.append([0, nIndividualsSusceptibles_S, nIndividualsInfected_I, nIndividualsRecovered_R])    
nGenerations = 0
# The following lists will be plotted
lst_nGeneration = []
lst_nIndSusceptibles = []
lst_nIndInfected = []
lst_nIndRecovered = []


  
#for i in range(nIterations):
while nIndividualsInfected_I >0:     
    nGenerations = nGenerations + 1
   
   
   
    
    #========================================
    # Evaluate the fields: 
    #    Infected --> heal = Recovered
    #    Susceptible + Infected = Transmitted (S-->I)
    #========================================
    # initialize class
    clsIniChngAg = ChangeAgentStatus.ChangeAgentStatus()
    
    # keep track how many s --> I transmission happened
    nTransmitted_Tau = 0
    # keep track of the healing I --> R
    nHealed = 0
    
    # execute the transmission method 
    nGenerationTau = clsIniChngAg.AgS2AgI_Transmit(AllFields, nBeta, nRasterDimension)
    nIndividualsSusceptibles_S = nIndividualsSusceptibles_S - nGenerationTau
    nIndividualsInfected_I = nIndividualsInfected_I + nGenerationTau
    nTransmitted_Tau = nTransmitted_Tau + nGenerationTau
    
    # execute the healing method 
    nGenerationHealed = clsIniChngAg.AgI2AgR_Heal(AllFields, nGamma, nRasterDimension)
    nHealed = nHealed + nGenerationHealed   
    nIndividualsInfected_I = nIndividualsInfected_I - nGenerationHealed
    nIndividualsRecovered_R = nIndividualsRecovered_R + nGenerationHealed

    
    # Count and report these Agents to the other plot
    lst_nGeneration.append(nGenerations)
    lst_nIndSusceptibles.append(nIndividualsSusceptibles_S)
    lst_nIndInfected.append(nIndividualsInfected_I)
    lst_nIndRecovered.append(nIndividualsRecovered_R)
    ##############################################################################

    
    
    #========================================
    # Random walk!
    # The random walk will be performed 
    # for all SIR by group S,I and R   
    #========================================
    
    # initialize class 
    inGetAgents = ag.GetListOfAgents()

    # initialize the random walk
    inRandWalk = rw.AgentsWalkRandomly()

    # get all the SIR Agents save them to tmp lists
    tmpAgents_S = inGetAgents.AllSusceptiblesSingles(AllFields)
    tmpAgents_R = inGetAgents.AllRecoveredSingles(AllFields)
    tmpAgents_I = inGetAgents.AllInfectedSingles(AllFields)
    
    # delete the entries in the SIR Agents in AllFields as we will use the tmp lsts
    delSAgentsOfFields = inGetAgents.AllSusceptiblesSinglesDelete(AllFields)
    delSAgentsOfFields = inGetAgents.AllRecoveredSinglesDelete(AllFields)
    delSAgentsOfFields = inGetAgents.AllInfectedSinglesDelete(AllFields)
    
    # get new "random" positions for the tmp SIR Agents  
    tmpLstAgents_S = []
    tmpLstAgents_S = inRandWalk.AgentsWalkRandomly(tmpAgents_S, nDiffusionRate_d, nRasterDimension)
    tmpLstAgents_R = []
    tmpLstAgents_R = inRandWalk.AgentsWalkRandomly(tmpAgents_R, nDiffusionRate_d, nRasterDimension)
    tmpLstAgents_I = []
    tmpLstAgents_I = inRandWalk.AgentsWalkRandomly(tmpAgents_I, nDiffusionRate_d, nRasterDimension)
    
    # append the new position to the AllFields list!
    if tmpLstAgents_S:
        inRandWalk.AddAgentsToField(tmpLstAgents_S, AllFields, nRasterDimension)
    
    if tmpLstAgents_R:
        inRandWalk.AddAgentsToField(tmpLstAgents_R, AllFields, nRasterDimension)
    
    if tmpLstAgents_I:
        inRandWalk.AddAgentsToField(tmpLstAgents_I, AllFields, nRasterDimension)
    
    # replott

    #for i in range(1000):
    if (nGenerations % PLOT_AGENTS_EVERY_N) == 0:    
        myAgentPlotter = plag.PlotIntoScatter()
        myAgentPlotter.PlottAgents(AllFields,nRasterDimension,lst_nGeneration, lst_nIndSusceptibles, lst_nIndInfected, lst_nIndRecovered,
                                   nDiffusionRate_d, nGamma, nBeta)  
        
        #myAgentPlotter.PlottProportionsOfIndividuals(lst_nGeneration, lst_nIndSusceptibles, lst_nIndInfected, lst_nIndRecovered)
##############################################################################
    
plt.show()    
        
    
    


