'''
Some basic prototypes for strategies and agents.

'''

import random

class Strategy(object):
    '''
    Abstract Strategy that we'll extend for specific strategies.
    '''
    
    def __init__(self):
        pass
    
    def run(self, data, a, b):
        '''
        Run the strategy and return a dictionary of weights for each element.
        
        Args:
            data: A dictionary mapping each node to the relevant indicator
            a, b: Two parameters for the strategy; e.g. slope and intercept.
        Returns:
            A dictionary of weights, with the same keys as the data dict.
        '''
        
        pass
    


class GenomeAgent(object):
    '''
    Parent class to prototype agents with behavioral genomes.
    '''

    def __init__(self, genome_length, genome = None):
        '''
        Create a new GenomeAgent. Defaults to a random genome.
        
        Args:
            genome_length: the length of the agent's genome
            genome: Instantiate the agent with an actual genome.
        '''
        
        if genome is None:
            self.genome = [random.random() for i in range(genome_length)]
        else:
            self.genome = genome
        
        