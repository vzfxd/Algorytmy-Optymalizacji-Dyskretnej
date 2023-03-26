import queue
import pathlib
import os
from collections import defaultdict
class Graph:

    def __init__(self, directed, n, m):
        self.directed = directed
        self.n = n
        self.m = m
        self.graph_struct = defaultdict(list)
        self.blue = []
        self.red = []


    def addEdge(self, node1, node2): 
        self.graph_struct[node1].append(node2)
        if(self.directed==False):
            self.graph_struct[node2].append(node1)
    
    def isBipartite(self):
        colors = [-1]*self.n
        q = queue.Queue()
        for idx in range(len(colors)):
            if(colors[idx]!=-1): continue
            colors[idx] = 1
            q.put(idx+1)
            while(q.empty()==False):
                v = q.get()
                for neighbour in self.graph_struct[v]:
                    if(colors[neighbour-1]==colors[v-1]): return False
                    if(colors[neighbour-1]==-1):
                        colors[neighbour-1] = 1 - colors[v-1]
                        q.put(neighbour)

        if(self.n<=200):
            for i in range(len(colors)):
                if(colors[i]==0):
                    self.blue.append(i+1)
                else:
                    self.red.append(i+1)
        return True
 
    
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
    
    def testBipartite(self):
        for idx,graph in enumerate(self.graphs):
            dwudzielny = graph.isBipartite()
            print("GRAF NR "+str(idx+1)+" || dwudzielny:"+str(dwudzielny))
            if(dwudzielny and graph.n<=200): print(str(graph.blue) + "," + str(graph.red))
    

tester4 = Tester(str(pathlib.Path().resolve())+"\\testy\\4")
tester4.initGraphs()
tester4.testBipartite()
