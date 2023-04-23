import heapq
class Graph:
    V = None
    E = None

    def __init__(self):
        self.V = {}
        self.E = []

    def addVertex(self,v):
        if v not in self.V:
            self.V[v] = []

    def addEdge(self, e):
        if (e[0] not in self.V):
            self.V[e[0]] = []
        if (e[1] not in self.V):
            self.V[e[1]] = []
        self.V[e[0]].append((e[1],e[2]))
        self.V[e[1]].append((e[0],e[2]))
        self.E.append(e)

    
    
    def path(self,prev,v1,v2):
        v = v2
        path = [v]
        while v != v1:
            path.append(prev[v])
            v = prev[v]
        path.reverse()
        return path

    def djikstra(self,v1,v2):
        dist = {i:1e9 for i in self.V}
        dist[v1] = 0 
        unvisited = set(self.V)
        prev = {}
        pathNodes = {}
        heap = [(0,(v1,None))]
        
        while (unvisited):
            min_node = None
            min_node = heapq.heappop(heap)[1]

            if (min_node[0] not in unvisited):
                continue

            unvisited.remove(min_node[0])
            prev[min_node[0]] = min_node[1]
            

            if (min_node[0] == v2):
                return self.path(prev,v1,v2)


            for neighbor in self.V[min_node[0]]:
                if (neighbor[0] in unvisited):
                    #print(neighbor[0])
                    this_dist = dist[min_node[0]] + neighbor[1]
                    if (this_dist < dist[neighbor[0]]):
                        dist[neighbor[0]] = this_dist
                        heapq.heappush(heap, (dist[neighbor[0]], (neighbor[0], min_node[0])))
            
    def print(self):
        print(self.V)
        print(self.E)




