#AttackerAgent
import random
import networkx as nx
import copy
from array import *
from DefenderAgent import Weights

from GenomeAgent import Strategy

class AttackerAgent(object):
    '''
    Attacker Agent class that manages all the aspects of attack
    '''
    def __init__(self, genome = None):
        '''The genome is randomly created if no list is specified with the values
        The genome represents the slopes giving a preference to certain metrics to be used in the attack
        
        Args: list with genome
        '''
        self.strategies = [DegreeAttackStrategy(),BetweennessAttackStrategy(),ClosenessAttackStrategy(),ClusteringAttackStrategy(),EigenvectorCentralityAttackStrategy(),CommunicabilityCentralityAttackStrategy(),RandomAttackStrategy()]
#        self.strategies = [DegreeAttackStrategy()]

        maxSlopeValue = 100
        if(genome==None):
            self.genome=[]
            for i in range(len(self.strategies)*2):
                self.genome.append(random.random()*maxSlopeValue)
            #print self.genome
        else:
            self.genome=genome

    def get_genome(self):
        return self.genome
    
    def which_node_to_attack(self, graph):
        '''Function that is used by the run manager to invoke the most important function
        for the attack: obtaining a node to attack considereing the several metrics.
        If the graph is disconnected the metrics are anyway computed by the default of networkX the metrics are 
        evaluated on each component.
        In the case of a disconnected network, the values of the metrics are weighted by the fraction of the 
        nodes composing each component.
        
        Args: graph that is the target of the attack
        '''
        self.graphToAttack = graph
        
        sumWeightsMetrics = self.weightAllMetricsSum(graph,self.genome)# array (list) of doubles representing slopes
        orderOfGraph = graph.order()
        sumWeightsCoinsideringComponents = {}
        components = nx.connected_components(graph)
        numberOfComponents = nx.number_connected_components(graph)
        #print components
        for i in range(0,numberOfComponents):
            for key in components[i]:
                value = sumWeightsMetrics.get(key)
                length = len(components[i])
                componenetWeightedValue = value*length/graph.order()
                sumWeightsCoinsideringComponents[key]=componenetWeightedValue  
        probability = copy.deepcopy(sumWeightsCoinsideringComponents)
        totalWeightSum = sum(sumWeightsCoinsideringComponents.values())
        #print totalWeightSum
        if totalWeightSum == 0: #it means there is no strategy that the attacker can do, our choice so far is to go with a random node
            #totalWeightSum = 1
            nodeToAttack = random.choice(graph.nodes())
        else:
            probability.update((x, y/totalWeightSum) for x, y in probability.items())
            nodeToAttack = weighted_random(probability)
        #nodeWithMaxProb = max(probability, key=probability.get)
        #print nodeToAttack
        return nodeToAttack

    def weightAllMetricsSum(self, graph, slope):
        '''
        Sums all the values of the metrics
        
        Args:
        graph to compute the metrics
        list of double containing the genome (slopes)
        '''
        '''
        betwennessWeightCalculator = BetweennessAttackStrategy()
        degreeWeightCalculator = DegreeAttackStrategy()
        closenessWeightCalculator = ClosenessAttackStrategy()
        clusteringWeightCalculator = ClusteringAttackStrategy()
        eigenvectorCentralityWeightCalculator = EigenvectorCentralityAttackStrategy()
        communicabilityCentralityWeightCalculator = CommunicabilityCentralityAttackStrategy()
        randomAttackCalculator = RandomAttackStrategy()
        weightList = [betwennessWeightCalculator,degreeWeightCalculator,closenessWeightCalculator,clusteringWeightCalculator,eigenvectorCentralityWeightCalculator,communicabilityCentralityWeightCalculator,randomAttackCalculator]
        '''
        resultDict = {}
        j=0
        for i in range(len(self.strategies)):
            strategy = self.strategies[i]
            tempWeight = strategy.run(graph,slope[j*2],slope[j*2+1])
            j+=1
            #print tempWeight
            for k in tempWeight.get_weights():
                resultDict[k] = resultDict.get(k, 0)+tempWeight.get_weights().get(k, 0)
                resultDict[k] = resultDict.get(k, 0)+tempWeight.get_oweights().get(k, 0)
                
        return resultDict
        

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




class DegreeAttackStrategy(Strategy):
    '''
    Example Degree-attack strategy implementation
    '''
    
    def run(self, graph, slope,slope1):
        degree_data = nx.degree_centrality(graph)
        weights = {}
        oweights={}
        for node, deg in degree_data.items():
            weights[node] = degree_data[node] * slope
            oweights[node] = (1-degree_data[node])*slope1 
        
        return Weights(weights,oweights)
      
class BetweennessAttackStrategy(Strategy):
    '''
    Example Betweenness Centality-attack strategy implementation
    '''
    
    def run(self, graph, slope,slope1):
        betweenness_data = nx.betweenness_centrality(graph)
        weights = {}
        oweights = {}
        for node, betw in betweenness_data.items():
            weights[node] = betweenness_data[node] * slope
            oweights[node] = (1-betweenness_data[node]) * slope1
        return Weights(weights,oweights)



class ClosenessAttackStrategy(Strategy):
    '''
    Example Closeness Centality-attack strategy implementation
    '''
    
    def run(self, graph, slope,slope1):
        closeness_data = nx.closeness_centrality(graph)
        weights = {}
        oweights={}
        for node, close in closeness_data.items():
            weights[node] = closeness_data[node] * slope
            oweights[node] = (1-closeness_data[node]) * slope1

        return Weights(weights,oweights)



class ClusteringAttackStrategy(Strategy):
    '''
    Example clustering-attack strategy implementation
    '''
    
    def run(self, graph, slope,slope1):
        clustering_data = nx.clustering(graph)
        weights = {}
        oweights={}
        for node, cluster in clustering_data.items():
            weights[node] = clustering_data[node] * slope
            oweights[node] = (1-clustering_data[node]) * slope1

        return Weights(weights,oweights)




class EigenvectorCentralityAttackStrategy(Strategy):
    '''
    Example eigenvector centrality-attack strategy implementation
    '''
    
    def run(self, graph, slope,slope1):
        weights = {}
        oweights={}
        try:
            eigenvector_data = nx.eigenvector_centrality(graph)
        except: # catch *all* exceptions
            eigenvector_data = {}
            for node in range(0,graph.order()):
                eigenvector_data[node]= 0
        for node, eigenv in eigenvector_data.items():
            weights[node] = eigenvector_data[node] * slope
            oweights[node] = (1-eigenvector_data[node]) * slope1
            
            #print weights
        return Weights(weights,oweights)
    
    
class CommunicabilityCentralityAttackStrategy(Strategy):
    '''
    Example communicability centrality-attack strategy implementation
    '''
    
    def run(self, graph, slope,slope1):
        communicability_data = nx.communicability_centrality(graph)
        weights = {}
        oweights={}
        max_comm_for_normaliz = max(communicability_data.values())
        for node, commu in communicability_data.items():
            weights[node] = communicability_data[node] * slope / max_comm_for_normaliz
            oweights[node] = (1-communicability_data[node]) * slope1 / max_comm_for_normaliz
        
        return Weights(weights,oweights)


class RandomAttackStrategy(Strategy):
    '''
    Examplerandom-attack strategy implementation
    '''
    
    def run(self, graph, slope,slope1):
        num_nodes = graph.order()
        node_to_attack = random.randint(0,num_nodes)
        weights = {}
        oweights={}
        for i in range(0,num_nodes):
            if i==node_to_attack:
                weights[i]=1*slope
                oweights[i]=0
            else:
                weights[i]=0
                oweights[i]=1
        return Weights(weights,oweights)


# ------------
# TESTING TOOLS
# -------------

class StupidAttacker(AttackerAgent):
    '''
    Attacker Agent class which only attacks on Degree
    '''
    def __init__(self, genome = None):
        '''The genome is randomly created if no list is specified with the values
        The genome represents the slopes giving a preference to certain metrics to be used in the attack
        
        Args: list with genome
        '''
        self.strategies = [DegreeAttackStrategy()]
        maxSlopeValue = 100
        if(genome==None):
            self.genome=[]
            for i in range(len(self.strategies)):
                self.genome.append(random.random()*maxSlopeValue+0.1)
            #print self.genome
        else:
            self.genome=genome

