'''
Created on Jun 11, 2013

@author: dmasad
'''
import networkx as nx

class RunManager(object):
    '''
    The object that manages a single run of the model.
    '''

    def __init__(self, attacker, defender, num_iterations, fitness):
        '''
        Create a new Run Manager.
        
        Args:
            attacker: An Attacker instance
            defender: Defender instance
            num_iterations: The number of iterations for them to compete for.
            fitness: A function computing the network metric used as fitness.
        '''
        
        self.attacker = attacker
        self.defender = defender
        self.num_iterations = num_iterations
        self.G = nx.Graph()
        self.fitness = fitness
        self.fitness_per_round = []
        
    def run(self):
        '''
        Run the run to completion, and return the network fitness series.
        '''
        
        self.build_initial_network()
        for round in range(self.num_iterations):
            self.attack_network()
            self.rebuild_network()
            new_fitness = self.fitness(self.G)
            self.fitness_per_round.append(new_fitness)
        return self.fitness_per_round
        
    def build_initial_network(self):
        pass
    
    def attack_network(self):
        pass
    
    def rebuild_network(self):
        pass
    