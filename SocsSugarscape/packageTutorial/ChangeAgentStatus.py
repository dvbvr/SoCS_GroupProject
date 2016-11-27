'''
Created on 08.11.2016

@author: dori
'''
  
import numpy as np
import Agents as ag
 
class ChangeAgentStatus:
     
    def GetAllAgentsWhoHaveContactWithInfected(self, AllFields):
        inGetAgents = ag.GetListOfAgents()
        allTheInfected = inGetAgents.AllInfectedSingles(AllFields)
        #[obj.nFieldNumber, obj.xPos, obj.yPos,  lstEntry]
        #                                        [AgentNr, 'I'] <--'I'-- [3][1]
        return allTheInfected
    #
     
    def AgS2AgI_Transmit(self, AllFields, nBeta, nRasterDimension):

        nfractionOfInfected_Tau_forOneGeneration = 0

        for Field in AllFields:
            
            if Field.Agent_S and Field.Agent_I: #python says false if len(Fields[3])=0
                multiplicatorBeta = len(Field.Agent_I) 
                
                if np.random.random() < nBeta*multiplicatorBeta:
                    nfractionOfInfected_Tau_forOneGeneration = nfractionOfInfected_Tau_forOneGeneration + len(Field.Agent_S)
                    # get all Ag_S from this field as they are now infected
                    tmpAgS = Field.Agent_S.copy()
                    # delete them as they will be added to the I lst
                    Field.Agent_S.clear()

                    # AgentType will be switched from S to I
                    for AgS2I in tmpAgS:
                        AgS2I[1] = 'I'
                        # transformed agents will be added to Agents_I
                        Field.Agent_I.append(AgS2I)
                        
        return nfractionOfInfected_Tau_forOneGeneration
    #
         
    def AgI2AgR_Heal(self,AllFields, nGamma, nRasterDimension):
         
        nHealedInfected = 0

        for Field in AllFields:
            
            if Field.Agent_I: 
                
                indexOfSingle = 0
                
                for singleAgI in Field.Agent_I: 
    
                    if np.random.random() < nGamma:
#                         nHealedInfected = nHealedInfected + len(Field.Agent_)
                        # get single Ag_I from this field, as this guy is now healed
                        tmpSinAgI = singleAgI
                        # delete them as they will be added to the R lst
                        del Field.Agent_I[indexOfSingle]
    
                        # AgentType will be switched from I to R
                        tmpSinAgI[1] = 'R'
                        Field.Agent_R.append(tmpSinAgI)
                        
                        nHealedInfected = nHealedInfected + 1

                    indexOfSingle = indexOfSingle +1
                    
        return nHealedInfected
    #



