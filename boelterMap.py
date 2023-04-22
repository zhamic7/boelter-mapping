import graph

boelterG = graph.Graph()
# add edges
rooms = [] #add rooms
dest = {} #add dest
def djikstra(s,e):
    path = boelterG.djikstra(s,e)
    # process path to give real directions 
    #return printPath(path)
