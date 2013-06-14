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
    
    def run(self, graph, slope):
        '''
        Run the strategy and return a dictionary of weights for each element.
        
        Args:
            graph: The relevant graph
            a, b: Two parameters for the strategy; e.g. slope and intercept.
            We agreed on just the slope right? -- Andrea
        Returns:
            A dictionary of weights, with the same keys as the data dict.
        '''
        
        pass
    


class DegreeAttackStrategy(Strategy):
    '''
    Example Degree-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        degree_data = nx.degree_centrality(graph)
        weights = {}
        for node, deg in degree_data.items():
            weights[node] = slope[node] * deg
        return weights
    
class BetweennessAttackStrategy(Strategy):
    '''
    Example Betweenness Centality-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        betwenness_data = nx.betwenness_centrality(graph)
        weights = {}
        for node, betw in betweenness_data.items():
            weights[node] = slope[node] * betw
        return weights



class ClosenessAttackStrategy(Strategy):
    '''
    Example Closeness Centality-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        closeness_data = nx.closeness_centrality(graph)
        weights = {}
        for node, close in closeness_data.items():
            weights[node] = slope[node] * close
        return weights



class ClusteringAttackStrategy(Strategy):
    '''
    Example clustering-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        clustering_data = nx.clustering(graph)
        weights = {}
        for node, cluster in clustering_data.items():
            weights[node] = slope[node] * cluster
        return weights




class EigenvectorCentralityAttackStrategy(Strategy):
    '''
    Example eigenvector centrality-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        eigenvector_data = nx.eigenvector_centrality(graph)
        weights = {}
        for node, eigenv in eigenvector_data.items():
            weights[node] = slope[node] * eigenv
        return weights
    
    
class CommunicabilityCentralityAttackStrategy(Strategy):
    '''
    Example communicability centrality-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        communicability_data = nx.communicability_centrality(graph)
        weights = {}
        max_comm_for_normaliz = max(communicability_data.values())
        for node, commu in communicability_data.items():
            weights[node] = slope[node] * commu / max_comm_for_normaliz
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
        
        