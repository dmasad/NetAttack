import random
import networkx as nx
import copy
from array import *

from GenomeAgent import Strategy

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
        randomAttackCalculator = RandomAttackStrategy()
        resultDict = {}
        weightList = [betwennessWeightCalculator,degreeWeightCalculator,closenessWeightCalculator,clusteringWeightCalculator,eigenvectorCentralityWeightCalculator,randomAttackCalculator]
        j=0
        for i in weightList:
            tempWeight = i.run(graph,slope[j])
            j+=1
            print tempWeight
            for k in tempWeight:
                resultDict[k] = resultDict.get(k, 0)+tempWeight.get(k, 0)
        return resultDict
    
class AttackerProbabilityNodeSelector(object):
    
    def run(self,graph,slope):
        attackerSummer = AttackerSummer()
        sumWeightsMetrics = attackerSummer.run(graph,slope)# array of doubles representing slopes
        probability = copy.deepcopy(sumWeightsMetrics)
        totalWeightSum = sum(sumWeightsMetrics.values())
        probability.update((x, y/totalWeightSum) for x, y in probability.items())
        '''print 'sum'
        print sumWeightsMetrics
        print 'total'
        print totalWeightSum
        print 'probability'
        print probability'''
        nodeWithMaxProb = max(probability, key=probability.get)

        return nodeWithMaxProb
        
    
    
