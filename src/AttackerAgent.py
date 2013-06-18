import random
import networkx as nx
import copy
from array import *

from GenomeAgent import Strategy

class AttackerAgent(object):

    def __init__(self,genome=None): 
        self.strategies = [DegreeAttackStrategy(),BetweennessAttackStrategy(),ClosenessAttackStrategy(),ClusteringAttackStrategy,EigenvectorCentralityAttackStrategy(),CommunicabilityCentralityAttackStrategy(),RandomAttackStrategy()]
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
    
    def which_node_to_attack(self,graph):
        attackerSummer = AttackerSummer()
        sumWeightsMetrics = attackerSummer.run(graph,self.genome)# array (list) of doubles representing slopes
        orderOfGraph = graph.order()
        
        sumWeightsCoinsideringComponents = {}
        #######################
        components = nx.connected_components(graph)
        #print components
        numberOfComponents = nx.number_connected_components(graph)
        ##print "number of components"
        ##print numberOfComponents
        for i in range(0,numberOfComponents):
            ##print "comp i"
            #print components[i]
            for key in components[i]:
                value = sumWeightsMetrics.get(key)
        ##                print "key"
        ##                print key
        ##                print "value"
        ##                print value
        ##                print "len comp i"
                ##print len(components[i])
                length = len(components[i])
                
                componenetWeightedValue = value*length/graph.order()
                sumWeightsCoinsideringComponents[key]=componenetWeightedValue  
        
        ########################
        
        probability = copy.deepcopy(sumWeightsCoinsideringComponents)
        totalWeightSum = sum(sumWeightsCoinsideringComponents.values())
        
        
        probability.update((x, y/totalWeightSum) for x, y in probability.items())
        ##        print 'sum'
        ##        print sumWeightsMetrics
        ##        print 'total'
        ##        print totalWeightSum
        ##        print 'probability'
        ##        print probability
        nodeToAttack = weighted_random(probability)
        #nodeWithMaxProb = max(probability, key=probability.get)
        
        return nodeToAttack





class DegreeAttackStrategy(Strategy):
    '''
    Example Degree-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        degree_data = nx.degree_centrality(graph)
        weights = {}
        for node, deg in degree_data.items():
            weights[node] = degree_data[node] * slope
        return weights
    
class BetweennessAttackStrategy(Strategy):
    '''
    Example Betweenness Centality-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        betweenness_data = nx.betweenness_centrality(graph)
        weights = {}
        for node, betw in betweenness_data.items():
            weights[node] = betweenness_data[node] * slope
        return weights



class ClosenessAttackStrategy(Strategy):
    '''
    Example Closeness Centality-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        closeness_data = nx.closeness_centrality(graph)
        weights = {}
        for node, close in closeness_data.items():
            weights[node] = closeness_data[node] * slope
        return weights



class ClusteringAttackStrategy(Strategy):
    '''
    Example clustering-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        clustering_data = nx.clustering(graph)
        weights = {}
        for node, cluster in clustering_data.items():
            weights[node] = clustering_data[node] * slope
        return weights




class EigenvectorCentralityAttackStrategy(Strategy):
    '''
    Example eigenvector centrality-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        eigenvector_data = nx.eigenvector_centrality(graph)
        weights = {}
        for node, eigenv in eigenvector_data.items():
            weights[node] = eigenvector_data[node] * slope
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
            weights[node] = communicability_data[node] * slope / max_comm_for_normaliz
        return weights


class RandomAttackStrategy(Strategy):
    '''
    Examplerandom-attack strategy implementation
    '''
    
    def run(self, graph, slope):
        num_nodes = graph.order()
        node_to_attack = random.randint(0,num_nodes)
        weights = {}
        for i in range(0,num_nodes):
            if i==node_to_attack:
                weights[i]=1*slope
            else:
                weights[i]=0
        return weights



class AttackerSummer(object):
    
    def run(self, graph, slope):
        betwennessWeightCalculator = BetweennessAttackStrategy()
        degreeWeightCalculator = DegreeAttackStrategy()
        closenessWeightCalculator = ClosenessAttackStrategy()
        clusteringWeightCalculator = ClusteringAttackStrategy()
        eigenvectorCentralityWeightCalculator = EigenvectorCentralityAttackStrategy()
        communicabilityCentralityWeightCalculator = CommunicabilityCentralityAttackStrategy()
        randomAttackCalculator = RandomAttackStrategy()
        resultDict = {}
        weightList = [betwennessWeightCalculator,degreeWeightCalculator,closenessWeightCalculator,clusteringWeightCalculator,eigenvectorCentralityWeightCalculator,communicabilityCentralityWeightCalculator,randomAttackCalculator]
        j=0
        for i in weightList:
            tempWeight = i.run(graph,slope[j])
            j+=1
            #print tempWeight
            for k in tempWeight:
                resultDict[k] = resultDict.get(k, 0)+tempWeight.get(k, 0)
        return resultDict
    
##class AttackerProbabilityNodeSelector(object):
##    
##    def run(self,graph,slope):
##        attackerSummer = AttackerSummer()
##        sumWeightsMetrics = attackerSummer.run(graph,slope)# array (list) of doubles representing slopes
##        probability = copy.deepcopy(sumWeightsMetrics)
##        totalWeightSum = sum(sumWeightsMetrics.values())
##        probability.update((x, y/totalWeightSum) for x, y in probability.items())
##        '''print 'sum'
##        print sumWeightsMetrics
##        print 'total'
##        print totalWeightSum
##        print 'probability'
##        print probability'''
##        nodeToAttack = weighted_random(probability)
##        #nodeWithMaxProb = max(probability, key=probability.get)
##
##        return nodeToAttack
        


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

    
