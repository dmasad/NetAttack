'''
Created on Jun 11, 2013

@author: dmasad
'''

import random
import networkx as nx

class RunManager(object):
    '''
    The object that manages a single run of the model.
    '''

    def __init__(self, attacker, defender, num_iterations, fitness, 
                 node_count, edge_count, instant_rewire=False):
        '''
        Create a new Run Manager.
        
        Args:
            attacker: An Attacker instance
            defender: Defender instance
            num_iterations: The number of iterations for them to compete for.
            fitness: A function computing the network metric used as fitness.
            node_count: How many nodes the network has.
            edge_count: How many edges the network (initially) has
            instant_rewire: If True, the fitness is not recomputed until the 
                            network finishes rewiring.
        '''
        
        self.attacker = attacker
        self.defender = defender
        self.node_count = node_count
        self.initial_edges = edge_count
        self.nodes_lost_edges = [] # Nodes with disconnected edges
        self.instant_rewire = instant_rewire
    
        self.num_iterations = num_iterations # Number of iterations per round
        self.G = nx.Graph()
        self.G.add_nodes_from(range(node_count))
        self.fitness = fitness # fitness function
        self.fitness_per_round = []
        
    def run(self):
        '''
        Run the run to completion, and return the network fitness series.
        '''
        self.build_initial_network()
        new_fitness = self.fitness(self.G)
        self.fitness_per_round.append(new_fitness)
        for round in range(self.num_iterations):
            self.attack_network()
            self.rewire_network()
        
        # Pleaceholder for aggregating fitness per round:
        total_fitness = 0
        for f in self.fitness_per_round:
            total_fitness += f
        total_fitness /= (1.0 * len(self.fitness_per_round))
        return total_fitness
        
    def build_initial_network(self):
        '''
        The defender initiates the network.
        '''
        for i in range(self.initial_edges):
            node = random.choice(self.G.nodes()) # Pick a random starting node
            new_edge = self.defender.rewire([node], self.G)
            self.G.add_edges_from(new_edge)
            
    
    def attack_network(self):
        '''
        The attacker picks a node to remove, and its neighbors are stored.
        '''
        self.attacked_node=self.attacker.which_node_to_attack(self.G)  
        self.nodes_lost_edges=self.G.neighbors(self.attacked_node)
        self.G.remove_node(self.attacked_node)

    
    def rewire_network(self):
            '''
            The defender rewires the network.
            '''
            edges_to_rewire=[]
            # Rewire the disconnected nodes
            if(len(self.nodes_lost_edges)>0):
                t=random.randrange(len(self.nodes_lost_edges))
                self.nodes_lost_edges.remove(self.nodes_lost_edges[t])
            
            if self.instant_rewire:
                # Rewire without recomputing fitness
                edges_to_rewire=self.defender.rewire(self.nodes_lost_edges, self.G)
                self.G.add_edges_from(edges_to_rewire)
        
            else:
                # Recompute fitness after each rewiring
                for node in self.nodes_lost_edges:
                    edges_to_rewire = self.defender.rewire([node], self.G)
                    self.G.add_edges_from(edges_to_rewire)
                    new_fitness = self.fitness(self.G)
                    self.fitness_per_round.append(new_fitness)
                    
            # Reinsert the disconnected node and rewire
            self.G.add_node(self.attacked_node)
            edges_to_rewire = self.defender.rewire([self.attacked_node], self.G)
            self.G.add_edges_from(edges_to_rewire)
            new_fitness = self.fitness(self.G)
            self.fitness_per_round.append(new_fitness)


    

        
