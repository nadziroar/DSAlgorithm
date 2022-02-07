#This is program about Breadth-First-Search algorithm 
# Breadth-First-Search(BFS) algorithm is to find the shortest path/route. 

#What is Graph : 
# A graph models a set of connections.
# 2 question BFS can answer for you : 
# -Is there a path from node A to node B (Is there a mango seller in your network?)
# -What is the shortest path from node A to node B? (Who is the closest mango seller? )
from collections import defaultdict
from operator import truediv
import queue

#This class represents a directed graph using adjancency list representation
class Graph:
    #constructor
    def __init__(self):
        #default dictionary to store graph
        self.graph = defaultdict(list)
        
    #function to add an edge to graph
    def addEdge (self, u, v):
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
            #Get all adjacent vertices of the dequeued vertex s. If a adjacent
            #has not been visited, then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
#Driver Code

#Create a graph given in the above diagram
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("Following is Breadth First Traversal (starting from vertex 2")
g.BFS(2)