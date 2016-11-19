'''
Created on 19.11.2016

@author: dori
'''

class TwoDimensionalEnvironment:
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
        '''
        Where nWidth is the width of our two dimensional field and nHeight is the 
        height.
        '''
        self.lstObjects = [] 
        self.lstObstacles = []  #walls, dirt, ...
        
        self.lstAgentHuman =[]
        self.lstAgentZombie =[]
        
        self.width = nWidth
        self.height = nHeight
        
        
        
    def objects_at(self, location):
        """Return all objects exactly at a given location."""
        return [obj for obj in self.lstObjects if obj.location == location]

    def objects_near(self, location, radius):
        """Return all objects within radius of location."""
        tmpRadius = radius * radius
        return [obj for obj in self.lstObjects
                if distance2(location, obj.location) <= tmpRadius]

    def percept(self, agent):
        """By default, agent perceives objects within radius r."""
        return [self.object_percept(obj, agent)
                for obj in self.objects_near(agent)]
        
    def execute_action(self, agent, action):
        """Change the world to reflect this action. 
        Override this."""

    def default_location(self, object):
        """Default location to place a new object with unspecified location."""
        return None
    
    def is_done(self):
        """By default, we're done when we can't find a human agent."""
        for agent in self.lstAgentHuman:
            if agent.is_alive(): 
                return False
            else:
                return True
            
    def step(self):
        """Run the environment for one time step."""
        if not self.is_done():
            actions = [agent.program(self.percept(agent))
                        for agent in self.lstAgentHuman]
            
            for (agent, action) in zip(self.lstAgentHuman, actions):
                self.execute_action(agent, action)
           
    def add_object(self, object, location):
        """Add an object to the environment, setting its location. Also keep
        track of objects that are agents. Shouldn't need to override this."""
        object.location = location or self.default_location(object)
        
        self.lstObjects.append(object)
        
        """
        Here we need to keep track of the different Agent types.
        For this reason the hierarchy should be updated like
        
        Agent
            Human
                ThatPanics
                Random
                ...
            Zombie
                InRageMode
                ...
        """
        if isinstance(object, Agent.Human):
            self.lstAgentHuman.append(object)           
        if isinstance(object, Agent.Zombie):
            self.lstAgentZombie.append(object)
    

        
        