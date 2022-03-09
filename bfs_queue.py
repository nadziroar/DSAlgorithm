#Breadth-First Traversal for a graph is similar to Breadth-First Traversal of a tree. The only catch here is, unlike trees
#graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once , we use a boolean
#visited array. For simplicity, it is assumed that all vertices are reachable from the starting vertex.

#Python3 Program to print BFS traversal from a given source vertex. BFS (int s ) traverses vertices reachable from s.
from collections import defaultdict
import queue

#This class represents a directed graph using adjancency list representation
class Graph:
    
    #Constructor:
    def __init__(self):
        #Default dictionary to store graph
        self.graph = defaultdict(list)
        
    #Function to add edge to graph
    def addEdge(self , u , v):
        self.graph[u].append(v)
        
    #Function to print a BFS of graph
    def BFS(self , s):
        #Mark all the vertices as not visited 
        visited = [False] * (max(self.graph) + 1)
        
        #Create a queue for BFS
        queue = []
        
        #Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        
        while queue:
            #Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s , end = " ")
            
            #Get all adjacent vertices of the dequeued vertexs. If a adjacent has not been visited, then mark it visited and enqueue it.
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
                    
#Driver Code
#Create a graph given in the above diagram
g = Graph()
g.addEdge(0,1)