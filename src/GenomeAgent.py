'''
Some basic prototypes for strategies and agents.

'''

import random
import networkx as nx

class Strategy(object):
    '''
    Abstract Strategy that we'll extend for specific strategies.
    '''
    
    def __init__(self):
        pass
    
    def run(self, graph, a, b):
        '''
        Run the strategy and return a dictionary of weights for each element.
        
        Args:
            graph: The relevant graph
            a, b: Two parameters for the strategy; e.g. slope and intercept.
        Returns:
            A dictionary of weights, with the same keys as the data dict.
        '''
        
        pass
    


class DegreeAttackStrategy(Strategy):
    '''
    Example Degree-attack strategy implementation
    '''
    
    def run(self, graph, a, b):
        degree_data = nx.degree(G, nbunch, weight)
        weights = {}
        for node, deg in degree_data.items():
            weights[node] = a + b * deg
        return weights


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
        
        