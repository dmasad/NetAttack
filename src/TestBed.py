'''
Created on Jun 13, 2013

@author: dmasad

Test bed for the Run Manager, basic Attacker and Defender classes

'''

from GenomeAgent import Strategy
import networkx as nx
import random

def weighted_random(item_dict):
    '''
    Randomly choose an item from the dictionary keys,
    with probability weights given in the dictionary values.

    Args:
        item_dict: a dictionary of the form:
            {Item: weight, Item: weight}
            where Item can be any key, and the weights are numeric.
    '''
    total = sum(item_dict.values())
    choice = random.random() * total
    counter = 0
    for key, wgt in item_dict.items():
        if choice < counter + wgt: 
            return key
        else: 
            counter += wgt

'''
Attacker
========
'''

class AttackRandom(Strategy):
    '''
    Assign attack weights at random.
    '''
    
    def run(self, graph, a, b):
        '''
        Assign random weights to each node.
        '''
        weights = {}
        for node in graph.nodes():
            weights[node] = random.random()
        return weights
    

class RandomAttacker(object):
    '''
    A test bed attacker that chooses a node at random.
    '''
    
    def __init__(self):
        '''
        Create a new RandomAttacker
        '''
        self.strategies = [AttackRandom()]

    def which_node_to_attack(self, graph):
        '''
        Choose a node from the graph to attack.
        
        Args:
            graph: A graph of nodes to choose from.
        
        Returns:
            The node chosen to attack.
        '''
        
        # Initialize the weight table
        attack_weights = {}
        for node in graph.nodes():
            attack_weights[node] = 0
        
        # Execute all the strategies, and add the appropriate weight.
        for strategy in self.strategies:
            strategy_weights = strategy.run(graph, 1, 1)
            for node, weight in strategy_weights.items():
                attack_weights[node] += weight
            
        # Choose one at random:
        target_node = weighted_random(attack_weights)
        print "Attacking", target_node
        return target_node

'''
Defender
========
'''

class DefendRandom(Strategy):
    '''
    Wire a given node at random
    '''
    
    def run(self, graph, node, a, b):
        '''
        Assign random weights to each node.
        '''
        weights = {}
        for alter in graph.nodes():
            if alter != node and alter not in graph[node]:
                weights[alter] = random.random()
            else: # Avoid repeating edges and self-loops 
                weights[alter] = 0 
        return weights

class RandomDefender(object):
    '''
    A test bed defender which wires nodes at random.
    '''
    
    def __init__(self):
        self.strategies = [DefendRandom()]
    
    def rewire(self, nodes, graph):
        '''
        Rewire the nodes in the graph.
        
        Args:
            nodes: a list of nodes to be rewired.
            graph: the graph within which the nodes are to be rewired.
        '''
        new_edges = []
        
        for node in nodes:
            #Initiate weights
            connect_weights = {}
            for candidate_node in graph.nodes():
                connect_weights[candidate_node] = 0
            # Apply strategies
            for strategy in self.strategies:
                strategy_weights = strategy.run(graph, node, 1, 1)
                for candidate_node, weight in strategy_weights.items():
                    connect_weights[candidate_node] += weight
            #Pick a connection
            target_node = weighted_random(connect_weights)
            new_edges.append((node, target_node))
            print "Connecting", node, "to", target_node
        return new_edges
        
        
        
        
        
        
        