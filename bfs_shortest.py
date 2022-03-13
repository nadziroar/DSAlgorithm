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
         
         