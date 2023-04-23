import graph
import re

directionDict = {
        'n':'north',
        's':'south',
        'e':'east',
        'w':'west'
        }


boelterG = graph.Graph()
with open('nodes.txt','r') as f:
    line = f.readline()
    while line:
        line = line.rstrip()
        if (line and line[0] != '#'):
            data = line.split(',')
            boelterG.addEdge((data[0],data[1],int(data[2])))
        line = f.readline()
            
def getRoom(r):
    hard_coded = set(("8500", "8251", "8436", "8427", "8470", "8438", "2780", "2444", "2684","SEASCAFE","CONNECTIONLAB","ROOF","SEL"))
    if (not r or ((not r.isdigit() or len(r) != 4) and r not in hard_coded) or r[0] == '0' or r[0] == '9' or r[1] in ['0','1','9']):
        return None
    if (r in hard_coded):
        return r
    if (int(r[0]) > 1 and r[0] != '8'):
        if (r[1] == '5'):
            return (r[0] + 'n')
        elif (r[1] == '7'):
            if (r[0] != '2'):
                return (r[0] + 's')
            else:
                return ('27x')
        elif (r[1] == '8' or r[1] == '6'):
            return (r[0] + 'w')
        else:
            return (r[0] + 'e')
    elif (r[0] == '1'):
        if (r[1] == '5'):
            return ('1e-nw')
        elif (r[1] == '7'):
            return ('1e-sw')
        elif (r[1] == '6' or r[1] == '8'):
            return ('1w')
        else:
            return None
    else:
        return None


dest = {
    "1":"ACKERMAN",
    "2":"BOMB",
    "3":"COS",
    "4":"e4",
    "5":"HILL",
    "6":"MEDICAL",
    "7":"m",
    "8":"NORTH",
    "9":"POWELL"
}
dest2 = {
    "1":"Ackerman",
    "2":"Bomb shelter",
    "3":"Court of Sciences",
    "4":"Engineering IV",
    "5":"The Hill",
    "6":"Medical Plaza",
    "7":"Math Sci",
    "8":"North Campus",
    "9":"Powell Library"
}
def directions(start, end, path):
    directions = []
    i = 1
    incos = False
    while (i < len(path) - 1):
        pattern = '^[0-9]e-'
        rmatch = re.search(pattern,path[i])
        estart = None
        eend = None
        if (rmatch):
            estart = path[i][0]
        while (i < len(path)-1 and rmatch):
            eend = path[i][0]
            i+=1
            rmatch = re.search(pattern,path[i])
        if (eend == estart):
            estart = None
            if (eend is not None):
                i-=1
        if (estart is not None):
            directions.append(f"Take elevator from floor {int(estart)} to {int(eend)}")
            i-=1
        elif ("COS" in path[i]):
            if (incos):
                pass
            else:
                directions.append("Exit to the Court of Sciences")
                incos = True
        elif (path[i] == "ACKERMAN"):
            directions.append("Head to Ackerman")
        elif (path[i] == "POWELL"):
            directions.append("Head to Powell library")
        elif (path[i] == "EXIT-3"):
            directions.append("Exit onto the catwalk outside of floor 3, on the west side. Walk north towards Ackerman")
        elif (path[i] == "BOMB"):
            directions.append("Head to the bomb shelter")
        elif (len(path[i-1]) == 2 and path[i-1][0] != 'm'):
            if re.search(pattern,path[i]):
                if path[i-1][-1] == path[i][-1]:
                    directions.append(f"Walk {directionDict[path[i][-2]]}")
                elif path[i-1][-1] == path[i][-2]:
                    directions.append(f"Walk {directionDict[path[i][-1]]}")
                else:
                    pass
        elif (len(path[i]) == 2):
            if (path[i][0] == 'm'):
                directions.append(f"Go to mathsci floor {path[i][1]}")
            else:
                pass
        elif (re.search(pattern,path[i])):
            pass
        elif (path[i] == '8500'):
            pass
        else:
            directions.append(path[i])
        i+=1
    return directions

def djikstra(s,e,S,E):
    path = directions(S,E,boelterG.djikstra(s,e))
    return path

