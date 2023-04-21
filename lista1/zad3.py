import time
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

    def addEdge(self, node1, node2): 
        self.graph_struct[node1].append(node2)
        if(self.directed==False):
            self.graph_struct[node2].append(node1)
    
    def dfsFinishedTime(self):
        visited = set()
        visited_second = set()
        result = deque()
        stack = deque()
        stack.append(1)
        while(len(stack)!=0):
            v = stack.pop()
            stack.append(v)
            if(v not in visited_second):
                visited.add(v)
                finished = True
                for neighbour in self.graph_struct[v]:
                    if neighbour not in visited:
                        finished = False
                        stack.append(neighbour)
                if(finished==True):
                    result.append(v)
                    visited_second.add(v)
                    stack.pop()
            else:
                stack.pop()
        return result

    def reverseGraph(self):
        reversed_graph = defaultdict(list)
        for key,nodeList in self.graph_struct.items():
            for node in nodeList:
                reversed_graph[node].append(key)
        self.graph_struct = reversed_graph
    
    def dfs(self,s,visited):
        result = []
        stack = deque()
        stack.append(s)
        while(len(stack)!=0):
            v =  stack.pop()
            result.append(v)
            if v not in visited:
                visited.add(v)
            for neighbour in self.graph_struct[v]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(neighbour)
        return result

    def scc(self):
        order = self.dfsFinishedTime()
        self.reverseGraph()
        visited = set()
        scc = []
        while(len(order)!=0):
            v = order.pop()
            if v not in visited:
                scc.append(self.dfs(v,visited))

        
        return scc
       
class Tester():

    graphs = []
    
    def __init__(self,path):
        self.path = path

    def initGraphs(self):
        for file in os.listdir(self.path):
            with open(self.path+"\\"+file,"r") as f:
                content = f.read().strip().split("\n")
                graph = Graph(content[0]=='D',int(content[1]),int(content[2]))
                [graph.addEdge(  int(x.split()[0]), int(x.split()[1]) ) for x in content[:2:-1]]
                self.graphs.append(graph)  
    
    def testSCC(self):
        print("=== TEST SCC ===")
        for idx,graph in enumerate(self.graphs):
            scc = graph.scc()
            print("\n\n=== GRAF NR "+str(idx+1)+"===")
            if(graph.n<=200):print(scc)
            print("Liczba składowych: "+str(len(scc)))
            for i in range(len(scc)):
                print(str(i+1)+".składowa: "+str(len(scc[i])))
        



tester3 = Tester(str(pathlib.Path().resolve())+"\\testy\\3")
tester3.initGraphs()
tester3.testSCC()
