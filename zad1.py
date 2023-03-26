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

    def addEdge(self, node1, node2): 
        self.graph_struct[node1].append(node2)
        if(self.directed==False):
            self.graph_struct[node2].append(node1)

    def bfs(self,s):
        q = queue.Queue()
        visited = set()
        visited.add(s)
        q.put(s)
        while(q.qsize()!=0):
            v = q.get()
            print(v, end=" ")
            for neighbour in self.graph_struct[v]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.put(neighbour)      
        print()  

    def dfs(self,visited,node):
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbour in self.graph_struct[node]:
                self.dfs(visited,neighbour)
 
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
    
    def testBfs(self):
        print("=== TEST BFS ===")
        for graph in self.graphs:
            graph.bfs(1)
    
    def testDfs(self):
        print("=== TEST DFS ===")
        for graph in self.graphs:
            graph.dfs(set(),1)
            print()
               

tester1 = Tester(str(pathlib.Path().resolve())+"\\testy\\1")
tester1.initGraphs()
tester1.testBfs()
tester1.testDfs()


