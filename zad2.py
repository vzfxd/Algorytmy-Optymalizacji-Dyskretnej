import queue
import pathlib
import os
from collections import defaultdict
from collections import deque
class Graph:

    def __init__(self, directed, n, m):
        self.directed = directed
        self.n = n
        self.m = m
        self.graph_struct = defaultdict(list)
        self.reverse_struct = defaultdict(list)

    def addEdge(self, node1, node2): 
        self.graph_struct[node1].append(node2)
        if(self.directed==False):
            self.graph_struct[node2].append(node1)

    def indegree_list(self):
        indegree = [0]*self.n
        for nodeList in self.graph_struct.values():
            for node in nodeList:
                indegree[node-1] += 1
        return indegree
    
    def topologicalSort(self):
        degrees = self.indegree_list()
        stack = deque()
        result = deque()
        next = 0    
        for i in range(len(degrees)):
            if(degrees[i]==0):
                stack.append(i+1)
        while(len(stack)!=0):
            i = stack.pop()
            result.append(i)
            next += 1
            i = next
            for neighbour in self.graph_struct[i]:
                degrees[neighbour-1] -= 1
                if(degrees[neighbour-1]==0): stack.append(neighbour)
        if(next<self.n): 
            print("CYKL")
        else:
            print("ACYKLICZNY",end=" ")
            if(self.n<=200):
                print(result)
            else:
                print()


    
    
class Tester():

    graphs = []
    
    def __init__(self,path):
        self.path = path

    def initGraphs(self):
        for file in os.listdir(self.path):
            with open(self.path+"\\"+file,"r") as f:
                content = f.read().strip().split("\n")
                graph = Graph(content[0]=='D',int(content[1]),int(content[2]))
                [graph.addEdge(  int(x.split()[0]), int(x.split()[1]) ) for x in content[3::]]
                self.graphs.append(graph)  
               
    def testTopologicalSort(self):
        print("=== TOPOLOGICAL SORT ===")
        for graph in self.graphs:
            graph.topologicalSort()



tester2 = Tester(str(pathlib.Path().resolve())+"\\testy\\2")
tester2.initGraphs()
tester2.testTopologicalSort()


