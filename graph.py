
class Node : 
    
    def __init__(self, idx, data = 0) : # Constructor   
        """
        id : Integer (1, 2, 3, ...)
        """
        self.id = idx
        self.data = data
        self.connectedTo = dict()

    def addNeighbour(self, neighbour , weight = 0) :
        """
        neighbour : Node Object
        weight : Default Value = 0

        adds the neightbour_id : wt pair into the dictionary
        """
        if neighbour.id not in self.connectedTo.keys() :  
            self.connectedTo[neighbour.id] = weight

    # setter
    def setData(self, data) : 
        self.data = data 

    #getter
    def getConnections(self) : 
        return self.connectedTo.keys()

    def getID(self) : 
        return self.id
    
    def getData(self) : 
        return self.data

    def getWeight(self, neighbour) : 
        return self.connectedTo[neighbour.id]

    def __str__(self) : 
        return str(self.data) + " Connected to : "+ \
         str([x.data for x in self.connectedTo])

class Graph : 

    totalV = 0 # total vertices in the graph
    
    def __init__(self) : 
        """
        allNodes = Dictionary (key:value)
                   idx : Node Object
        """
        self.allNodes = dict()

    def addNode(self, idx) : 
        """ adds the node """
        if idx in self.allNodes : 
            return None
        
        Graph.totalV += 1
        node = Node(idx=idx)
        self.allNodes[idx] = node
        return node

    def addNodeData(self, idx, data) : 
        """ set node data acc to idx """
        if idx in self.allNodes : 
            node = self.allNodes[idx]
            node.setData(data)
        else : 
            print("No ID to add the data.")

    def addEdge(self, src, dst, wt = 0) : 
        """
        Adds edge between 2 nodes
        Undirected graph

        src = node_id = edge starts from
        dst = node_id = edge ends at

        To make it a directed graph comment the second line
        """
        self.allNodes[src].addNeighbour(self.allNodes[dst], wt)
        self.allNodes[dst].addNeighbour(self.allNodes[src], wt)
    
    def isNeighbour(self, u, v) : 
        """
        check neighbour exists or not
        """
        if u >=1 and u <= 81 and v >=1 and v<= 81 and u !=v : 
            if v in self.allNodes[u].getConnections() : 
                return True
        return False



    def printEdges(self) : 
        """ print all edges """
        for idx in self.allNodes :
            node =  self.allNodes[idx]
            for con in node.getConnections() : 
                print(node.getID(), " --> ", 
                self.allNodes[con].getID())
    
    # getter
    def getNode(self, idx) : 
        if idx in self.allNodes : 
            return self.allNodes[idx]
        return None

    def getAllNodesIds(self) : 
        return self.allNodes.keys()

    # methods
    def DFS(self, start) :
        """
        start is an id of the start node
        """ 
        # STACK
        visited = [False]*Graph.totalV

        if start in self.allNodes.keys() : 
            self.__DFSUtility(node_id = start, visited=visited) 
        else : 
            print("Start Node not found")

    def __DFSUtility(self, node_id, visited) : 
        visited = self.__setVisitedTrue(visited=visited, node_id=node_id)
        #print
        print(self.allNodes[node_id].getID(), end = " ")

        #Recursive Stack
        for i in self.allNodes[node_id].getConnections() : 
            if visited[self.allNodes[i].getID()] == False : 
                self.__DFSUtility(node_id = self.allNodes[i].getID(), 
                visited=visited)

    def BFS(self, start) : 
        """
        start is an id of the start node
        """
        #Queue
        visited = [False]*Graph.totalV

        if start in self.allNodes.keys() : 
            self.__BFSUtility(node_id = start, visited=visited) 
        else : 
            print("Start Node not found")

    def __BFSUtility(self, node_id, visited) :
        queue = []
        visited = self.__setVisitedTrue(visited=visited, node_id=node_id)

        queue.append(node_id)

        while queue != [] : 
            x = queue.pop(0) 
            #print
            print(self.allNodes[x].getID(), end = " ")

            for i in self.allNodes[x].getConnections() : 
                idx = self.allNodes[i].getID()
                if visited[idx]  == False : 
                    queue.append(idx)
                    visited = self.__setVisitedTrue(visited=visited,
                     node_id=idx)
        


    def __setVisitedTrue(self, visited, node_id) : 
        """
        Utility function for BFS and DFS 
        
        Through this function we will set visited[id] = True
        Preprocessing node_id if required
        Since now node_id is an integer it is not required to preprocess it
        """
        visited[node_id] = True
        return visited


"""
TESTING
"""
def test() : 
    g = Graph()
    for i in range(6) :
        g.addNode(i)

    print("Vertices : ",g.getAllNodesIds())

    g.addEdge(src = 0, dst = 1, wt = 5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)

    g.printEdges()

    print("DFS : (starting with 0)")
    g.DFS(0)
    print()
    
    print("BFS : (starting with 0)")
    g.BFS(0)
    print()

if __name__ == "__main__" : 
    test()
