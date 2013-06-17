'''
Created on Jun 15, 2013

@author: dmasad
'''

class EvolutionManager(object):
    '''
    Class to manage the entire coevolution of network and attacker agents.
    '''


    def __init__(self, Attacker, Defender,
                 network_size, edge_count, 
                 pop_size, generation_count, mutation_rate):
        '''
        Create a new complete coevolution run.
        
        Args:
            Attacker: The Attacker class
            Defender: The Defender class
            network_size: The number of nodes in each network
            edge_count: The number of edges in each network
            pop_size: Number of attackers and defenders in each generation
            generation_count: The number of generations to run for
            mutation_rate: The rate of mutation
        '''
        self.Attacker = Attacker
        self.Defender = Defender
        self.pop_size = pop_size
        self.generation_count = generation_count
        self.mutation_rate = mutation_rate
        
        # Create the initial generation.
        
        
        