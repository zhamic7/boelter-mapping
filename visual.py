# Import library
from d3graph import d3graph, vec2adjmat
import boelterMap 
import graph


def createVisual(s,e):

    print('VISUAL working: ', s, ', ', e)

    source = []
    target = []
    weight = []

    s = convertNodeName(s)
    e = convertNodeName(e)

    boelterG = graph.Graph()
    with open('nodes.txt','r') as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            if (line and line[0] != '#'):
                data = line.split(',')
                boelterG.addEdge((convertNodeName(data[0]),convertNodeName(data[1]),int(data[2])))
            line = f.readline()

    a = boelterG.djikstra(s,e)
    
    with open('nodes.txt','r') as f:
        line = f.readline()
        while line:
            line = line.rstrip()
            data = line.split(',')
            if (line and line[0] != '#'):
                if(convertNodeName(data[0]) in a):
                    source.append(convertNodeName(data[0]))
                    target.append(convertNodeName(data[1]))
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

def convertNodeName(node_name):
    if node_name[:4].isdigit():
        return "RM" + node_name[:4]
    elif len(node_name) == 2 and node_name[1] in ['n', 'e', 's', 'w']:
        floor_num = node_name[0]
        direction = {'n': 'North', 'e': 'East', 's': 'South', 'w': 'West'}[node_name[1]]
        return f"{floor_num}-{direction}_ELEV"
    elif len(node_name) > 2 and node_name[1:3] in ['e-', 'w-'] and node_name[3:] in ['n', 'ne', 'nw', 's', 'se', 'sw']:
        floor_num = node_name[0]
        direction = node_name[3:].replace('ne', 'Northeast').replace('nw', 'Northwest').replace('se', 'Southeast').replace('sw', 'Southwest').title()
        return f"{floor_num}-{direction}_ELEV"
    elif node_name == "COS":
        return "Court_of_Sciences"
    elif node_name[:4] == "COS-":
        direction = {'n': 'North', 'e': 'East', 's': 'South', 'w': 'West', 'm': 'Middle'}[node_name[-1]]
        return f"{direction}_Court_of_Sciences"
    elif node_name == "BOMB":
        return "Bomb_Shelter"
    elif node_name == "e4":
        return "Engineering_4"
    else:
        return node_name