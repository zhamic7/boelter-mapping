# Import library
from d3graph import d3graph, vec2adjmat
import boelterMap 
import graph


def createVisual(s,e):

    print('VISUAL working: ', s, ', ', e)

    source = []
    target = []
    weight = []

    boelterG = graph.Graph()
    with open('nodes.txt','r') as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            if (line and line[0] != '#'):
                data = line.split(',')
                boelterG.addEdge((data[0],data[1],int(data[2])))
            line = f.readline()

    a = boelterG.djikstra(s,e)
    
    with open('nodes.txt','r') as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            data = line.split(',')
            if (line and line[0] != '#'):
                if(data[0] in a):
                    source.append(data[0])
                    target.append(data[1])
                    if(int(data[2]) == 0):
                        weight.append(0.1)
                    else:
                        weight.append(int(data[2]))
            line = f.readline()

    # Convert to adjacency matrix
    adjmat = vec2adjmat(source, target, weight)

    # Initialize
    d3 = d3graph()
    # Proces adjmat
    d3.graph(adjmat)

    d3.set_node_properties(color='#dcdcdc', fontcolor='#5a4866')
    for x in range(len(a)):
        d3.node_properties[a[x]]['color']='#9791b5'
        d3.node_properties[a[x]]['fontcolor']='#000000'


    # Plot
    d3.show(filepath='templates/', show_slider=False, showfig = False, overwrite = True)

