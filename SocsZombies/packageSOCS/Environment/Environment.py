'''
Created on 19.11.2016

@author: dori
'''

import Agent
import GLOBAL_VARIABLES

####################################################
class Environment(object):
    '''
    classdocs:
    
    Abstract class Environment represents an environment for the agents.
    
    The Environment is a two dimensional plane, with locations labeled,
    (xPos, yPos) which are discrete points. Agents perceive objects in a
    square-shaped radius or in a Neumann radius. Each Agent in the Environment
    has a position like (4,9) and a holding slot which is a list of thinks he holds.
    
    The Environment has a list of objects. Where Human-Agents and Zombie-Agents 
    and Obstacles are a subset of objects.

    If you instantiate an Environment to get a "REAL-Environment" 
    this environment will inherit from this class.
    '''    
    def __init__(self, nWidth = 10, nHeight = 10):
        # Where nWidth is the width of our two dimensional field and nHeight is the height.

        # List of all things        
        self.lstThings = []     #walls, water, lava, Agents ...     
        # subset of things
        self.lstAgents = []
    #

   
        
####################################################
class TwoDimensionalEnvironment(Environment):
    '''
    classdocs:
    
    Abstract class Environment represents an environment for the agents.
    
    The Environment is a two dimensional plane, with locations labeled,
    (xPos, yPos) which are discrete points. Agents perceive objects in a
    square-shaped radius or in a Neumann radius. Each Agent in the Environment
    has a position like (4,9) and a holding slot which is a list of thinks he holds.
    
    The Environment has a list of objects. Where Human-Agents and Zombie-Agents 
    and Obstacles are a subset of objects.

    If you instantiate an Environment to get a "REAL-Environment" 
    this environment will inherit from this class.
    '''
    
    def __init__(self, nWidth = 10, nHeight = 10):
        # Where nWidth is the width of our two dimensional field and nHeight is the height.
        
        self.width = nWidth
        self.height = nHeight
    #
    
    #===========================================================================
    # Initialization methods
    #===========================================================================
    def DefaultLocation(self, thing):
        """Default location to place a new object with 
        unspecified location."""
        return None
    #

    def AddThing(self, thing, atPositionXY):
        """Add thinks to the world --> "environment", setting its location. 
        Also keep track of the things especially the agents."""
        
        # Check if we really got a instance of Thing
        if isinstance(thing, Agent.Thing):
            #or self.DefaultLocation(thing)
            thing.PositionXY = atPositionXY             
            self.lstThings.append(thing)
            
            
            """
            Here we need to keep track of the different Agent types.
            For this reason the hierarchy should be updated like
            
            Thing
                Agent
                    Human
                        ThatPanics
                        Random
                        ...
                    Zombie
                        InRageMode
                        ...
            """
            if isinstance(object, Agent.Agent) and Agent.State() == GLOBAL_VARIABLES.NAME_AGENTHUMAN:
                self.lstAgentHuman.append(object)           
            if isinstance(object, Agent.Agent) and Agent.State() == GLOBAL_VARIABLES.NAME_AGENTZOMBIE:
                self.lstAgentZombie.append(object)
    #
        
    #===========================================================================
    # Runtime methods
    #===========================================================================
    def IsDone(self):
        """By default, we're done when we can't find a human agent.
        The zombies are now ruling the world :("""
        return not any(agent.GetState() == GLOBAL_VARIABLES.NAME_AGENTHUMAN for agent in self.lstAgents)
    #    
            
    def Step(self):
        """Run the environment for one time step."""
        if not self.IsDone():
            actions = [agent.program(self.percept(agent))
                        for agent in self.lstAgentHuman]
            
            for (agent, action) in zip(self.lstAgentHuman, actions):
                self.execute_action(agent, action)
    #

    #===========================================================================
    # Methods to percieve the Environment:
    # Called by the agents.
    #===========================================================================
    def Percept(self, agent):
        """By default, agent perceives objects within radius r."""
        return [self.object_percept(obj, agent) for obj in self.ObjectsNear(agent)]
    #
            
    def ExecuteAction(self, agent, action):
        """Change the world to reflect this action. 
        Override this."""
    #

    def ObjectsAt(self, location):
        """Return all objects exactly at a given location.
        The location is a point like: [xPos,yPos] """
        return [obj for obj in self.lstThings if obj.location == location]
    #
    
    def ObjectsNear(self, location, radius):
        """Return all objects within radius of location."""
        #=======================================================================
        # tmpRadius = radius * radius
        # return [obj for obj in self.lstObjects
        #         if distanceMethod(location, obj.location) <= tmpRadius]
        #=======================================================================
    #
        
    #===========================================================================
    # Methods used for the plotting of the Environment
    #===========================================================================
    def GetEnvironmentSize(self):
        """This will be needed for the plot"""
        lstTmp = [self.width, self.height]
        return lstTmp
    #
    
   
    
    
    

        
        