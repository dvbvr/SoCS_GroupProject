'''
Created on 07.11.2016

@author: dori
'''
import numpy as np
import Agents as ag

#Let the puppets(agents) walk as randomly(drunkly looking) as possible!
class AgentsWalkRandomly:
    
    def AgentsWalkRandomly(self, Agents, nDiffusionRate_d, nRasterDimension):
    
 
        #For every agent I have to decide if this agent moves and if it moves in which direction.    
        for i in range(len(Agents)): 
     
            #Agent likes to move it! 
            if np.random.random() <= (1-nDiffusionRate_d):     
                    
                #In which direction should this agent move?!
                oneOutOfFour = np.random.randint(0,3) #choice(4,1)[0]
                
                #    X
                if oneOutOfFour == 0:
                    #ith agent x-Position links --> rechts | links
                    if Agents[i][1] == nRasterDimension -1: #jump
                        #new yPos
                        Agents[i][1] = 0
                        #new Fieldnr
                        Agents[i][0] = Agents[i][0] - (nRasterDimension)*(nRasterDimension-1)
                    else:
                        Agents[i][1] = Agents[i][1] +1
                        Agents[i][0] = Agents[i][0] + nRasterDimension

                #ith agent x-Position rechts| links <-- rechts 
                if oneOutOfFour == 1:
                    if Agents[i][1] == 0: #jump
                        #new yPos
                        Agents[i][1] = nRasterDimension -1
                        #new Fieldnr
                        Agents[i][0] = Agents[i][0] + (nRasterDimension)*(nRasterDimension-1)
                    else:
                        Agents[i][1] = Agents[i][1] -1
                        Agents[i][0] = Agents[i][0] - nRasterDimension
                
                #     X
                if oneOutOfFour == 2:
                    #ith agent y-Position unten --> oben | unten
                    if Agents[i][2] == nRasterDimension -1: #jump
                        #new yPos
                        Agents[i][2] = 0
                        #new Fieldnr
                        Agents[i][0] = Agents[i][0] - (nRasterDimension-1)
                    else:
                        Agents[i][2] = Agents[i][2] +1
                        Agents[i][0] = Agents[i][0] +1

                if oneOutOfFour == 3:
                    #ith agent y-Position oben --> unten | oben
                    if Agents[i][1] == 0: #jump
                        #new yPos
                        Agents[i][1] = nRasterDimension -1
                        #new Fieldnr
                        Agents[i][0] = Agents[i][0] + (nRasterDimension-1)
                    else:
                        Agents[i][1] = Agents[i][1] -1
                        Agents[i][0] = Agents[i][0] -1
                
            #else: #Agents does not want to move! --> nothing happens 
           
        return Agents
    #=========================

    def AddAgentsToField(self, Agents, AllFields, nRasterDimension):
        if Agents[0]:
            if Agents[0][3][1] == 'S':
                for agent in Agents:
                    tmpField = AllFields[agent[0]]
                    tmpField.AddSAgentToField(agent[3][0],agent[3][1])
            if Agents[0][3][1] == 'R':
                for agent in Agents:
                    tmpField = AllFields[agent[0]]
                    tmpField.AddRAgentToField(agent[3][0],agent[3][1])
            if Agents[0][3][1] == 'I':
                for agent in Agents:
                    tmpField = AllFields[agent[0]]
                    tmpField.AddIAgentToField(agent[3][0],agent[3][1])
    #            
                    
                    
                    
