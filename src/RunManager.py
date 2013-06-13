'''
Created on Jun 11, 2013

@author: dmasad
'''
import networkx as nx

class RunManager(object):
    '''
    The object that manages a single run of the model.
    '''

    def __init__(self, attacker, defender, num_iterations, fitness, nmb_nodes):
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
        
	self.nodes_lost_edges = []

	self.num_iterations = num_iterations
        self.G = nx.Graph()
	G.add_nodes_from(range(nmb_nodes))
        self.fitness = fitness
        self.fitness_per_round = []
        
    def run(self):
        '''
        Run the run to completion, and return the network fitness series.
        '''
        
        self.build_initial_network(initialEdges)
	new_fitness = self.fitness(self.G)
        self.fitness_per_round.append(new_fitness)
        for round in range(self.num_iterations):
	    self.calculate_network_metrics()
            self.attack_network()
            self.defend_network()
            new_fitness = self.fitness(self.G)
            self.fitness_per_round.append(new_fitness)
        return self.fitness_per_round
        
    def build_initial_network(self,initialEdges):
	for i in range(initialEdges):
		self.defend_network()        
	pass
    
    def attack_network(self):

	attacked_node=self.attacker.which_node_to_attack()  
	self.nodes_lost_edges=self.G.neighbors(attacked_node)
	self.G.remove_node(attacked_node)	

	pass

    
    def defend_network(self):
	edges_to_rewire=self.defender.defender_network(self.nodes_lost_edges)
	'''
	edges to rewire are contained within edges_to_rewire
	'''
	self.G.add_edges_from(edges_to_rewire)
	
        pass

    def calculate_network_metrics_attacker():
	'''
        calculate the network metrics used by the attacker
        for all nodes in the network
        returns a matrix of nodes*metrics
        '''
   	
	return []
    
    def calculate_network_metrics_defender():
        '''
        calculate the network metrics used by the defender
        for all nodes in the network
        returns a matrix of nodes*metrics
        '''
        return []
        pass
        
