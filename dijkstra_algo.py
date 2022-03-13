#Python program for Dijkstra's single source shortest path algorithm. The program is for adjacency matrix representation of the graph

import sys
 
class Graph():
    def __init__(self , vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)]
                       for row in range(vertices)]
         
    def printSolution(self, dist):
        print('Vertex \t Distance From Source : ')
        for node in range(self.V):
            print (node , "\t" , dist(node))
         
    #A utility function to find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree
    def minDistance (self, dist, sptSet):
        #Initialize the minimum distance for next node:
        min = sys.maxsize
        #Search not the nearest vertex not in the shortest path tree
        for u in range (self.V):
            if dist[u] < min and  sptSet[u] == False:
                min = dist[u]
                min_index = u
                
        return min_index
    
    #Function that implement Dijkstra's single source shortest path algorithm for a graph represented using adjacency matrix representation
    def dijkstra (self, src):
        dist = [sys.maxsize] * self.V 
        dist[src] = 0 
        sptSet = [False] *self.v
        
        for cout in range(self.V):
            #Pick the minimum distance vertex from the set of vertices not yet processed. X is always equal to src in first iteration
            x = self.minDistance(dist , sptSet)
            #Put the minimum distance vertex in the shortest path tree
            sptSet[x] = True
            #Update dist value of the adjacent vertices of the picked vertex only if the current distance is greater than  new distance 
            # and the vertex is not in the shortest path tree
            for y in range (self.V):
                if self.graph[x][y] > 0 and sptSet == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)
        
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
 
g.dijkstra(0);
 