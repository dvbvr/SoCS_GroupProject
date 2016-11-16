'''
Created on 07.11.2016

@author: dori
'''

import numpy as np
import matplotlib.pyplot as plt

####################################################
class AgentsOnField(object):
    
    def __init__(self, nFieldNumber, xPos, yPos):
        self.nFieldNumber = nFieldNumber
        self.xPos = xPos
        self.yPos = yPos
        #creates a new empty list for each field
        self.Agent_S = [] 
        self.Agent_R = [] 
        self.Agent_I = [] 
    # S _______________________________________    
    def AddSAgentToField(self, numberOfAgent, agentType):
        self.Agent_S.append([numberOfAgent, agentType])
    # R _______________________________________    
    def AddRAgentToField(self, numberOfAgent, agentType):
        self.Agent_R.append([numberOfAgent, agentType])
    # I _______________________________________    
    def AddIAgentToField(self, numberOfAgent, agentType):
        self.Agent_I.append([numberOfAgent, agentType])
    # S _______________________________________    
    def CopySAgentsOfField(self):
        lst= [self.xPos, self.yPos, self.Agent_S.copy()]
        return  lst
    # R ________________________________________    
    def CopyRAgentsOfField(self):
        lst= [self.xPos, self.yPos, self.Agent_R.copy()]
        return  lst
    # I _______________________________________    
    def CopyIAgentsOfField(self):
        lst= [self.xPos, self.yPos, self.Agent_I.copy()]
        return  lst
    # S _______________________________________    
    def RemoveSAgentsOfField(self):
        self.Agent_S.clear()      
    # R _______________________________________    
    def RemoveRAgentsOfField(self):
        self.Agent_R.clear()  
    # I _______________________________________    
    def RemoveIAgentsOfField(self):
        self.Agent_I.clear()  
#========================================

class IntitializeAgents:
    # S _______________________________________    
    def InitializeSAgentsRandomly(self, AllFields, nRasterDimension, numberOfAgents, nStartingNumber):
    
        for i in range(numberOfAgents):
            randomField = np.random.randint(nRasterDimension*nRasterDimension)
            tmpOneField = AllFields[randomField]
            tmpNumber = i + nStartingNumber
            tmpOneField.AddSAgentToField(tmpNumber,'S')

    # R _______________________________________    
    def InitializeRAgentsRandomly(self, AllFields, nRasterDimension, numberOfAgents, nStartingNumber):
    
        for i in range(numberOfAgents):
            randomField = np.random.randint(nRasterDimension*nRasterDimension)
            tmpOneField = AllFields[randomField]
            tmpNumber = i + nStartingNumber
            tmpOneField.AddRAgentToField(tmpNumber,'R')
    
    # I _______________________________________    
    def InitializeIAgentsRandomly(self, AllFields, nRasterDimension, numberOfAgents, nStartingNumber):
    
        for i in range(numberOfAgents):
            randomField = np.random.randint(nRasterDimension*nRasterDimension)
            tmpOneField = AllFields[randomField]
            tmpNumber = i + nStartingNumber
            tmpOneField.AddIAgentToField(tmpNumber,'I')
#========================================

class PrintAgents:    
    def PrintAllAgentsInConsole(self, AllFields):
       
        for obj in AllFields:
            print(obj.nFieldNumber ,obj.xPos,  obj.yPos, obj.Agent_S, obj.Agent_R, obj.Agent_I)      
#========================================

class GetListOfAgents:
    # S _______________________________________
    # [xPos, yPos, [Agent_S]]
    def AllSusceptibles(self, AllFields):
        myTmp = []
        for obj in AllFields:
            if obj.Agent_S:
                myTmp.append([obj.xPos, obj.yPos, obj.Agent_S])  
        return myTmp
    # each Agent [xPos, yPos, Agent_S]
    def AllSusceptiblesSingles(self, AllFields):
        myTmp = []
        for obj in AllFields:
            if obj.Agent_S:
                for lstEntry in obj.Agent_S:
                    myTmp.append([obj.nFieldNumber, obj.xPos, obj.yPos, lstEntry])  
        return myTmp

    def AllSusceptiblesSinglesDelete(self, AllFields):
        for obj in AllFields:
            if obj.Agent_S:
                obj.RemoveSAgentsOfField()
        return AllFields
            
    def AllSusceptiblesSinglesCoordinates(self, AllFields):
        myTmp = []
        for obj in AllFields:
            if obj.Agent_S:
                for lstEntry in obj.Agent_S:
                    myTmp.append([obj.xPos, obj.yPos])  
        myTmpArray = np.array(myTmp)
        return myTmpArray # np.array <-- array[:,0] and array[:,1]

    # R _______________________________________
    def AllRecovered(self, AllFields):
        myTmp = []
        for obj in AllFields:
            if obj.Agent_R:
                myTmp.append([obj.xPos, obj.yPos, obj.Agent_R])  
        return myTmp

    def AllRecoveredSingles(self, AllFields):
        myTmp = []
        for obj in AllFields:
            if obj.Agent_R:
                for lstEntry in obj.Agent_R:
                    myTmp.append([obj.nFieldNumber, obj.xPos, obj.yPos, lstEntry])  
        return myTmp
    
    def AllRecoveredSinglesDelete(self, AllFields):
        for obj in AllFields:
            if obj.Agent_R:
                obj.RemoveRAgentsOfField()
        return AllFields
    
    def AllRecoveredSinglesCoordinates(self, AllFields):
        myTmp = []
        for obj in AllFields:
            if obj.Agent_R:
                for lstEntry in obj.Agent_R:
                    myTmp.append([obj.xPos, obj.yPos])  
        myTmpArray = np.array(myTmp)                    
        return myTmpArray

    # I _______________________________________
    def AllInfected(self, AllFields):
        myTmp = []
        for obj in AllFields:
            if obj.Agent_I:
                myTmp.append([obj.xPos, obj.yPos, obj.Agent_I])  
        return myTmp

    def AllInfectedSingles(self, AllFields):
        myTmp = []
        for obj in AllFields:
            if obj.Agent_I:
                for lstEntry in obj.Agent_I:
                    myTmp.append([obj.nFieldNumber, obj.xPos, obj.yPos, lstEntry])  
        return myTmp
    
    def AllInfectedSinglesDelete(self, AllFields):
        for obj in AllFields:
            if obj.Agent_I:
                obj.RemoveIAgentsOfField()
        return AllFields
    
    def AllRecoveredInfectedCoordinates(self, AllFields):
        myTmp = []
        for obj in AllFields:
            if obj.Agent_I:
                for lstEntry in obj.Agent_I:
                    myTmp.append([obj.xPos, obj.yPos])  
        myTmpArray = np.array(myTmp)
        return myTmpArray
#========================================


