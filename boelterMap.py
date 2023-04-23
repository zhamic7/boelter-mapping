import graph

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
    if (not r or not r.isdigit() or r[0] == '0' or r[0] == '9' or r[1] in ['0','1','9'] or len(r) != 4):
        return None
    hard_coded = set(("8500", "8251", "8436", "8427", "8470", "8438", "2780", "2444", "2684","SEASCAFE","CONNECTIONLAB","ROOF","SEL"))
    if (r in hard_coded):
        return r
    if (int(r[0]) > 1 and r[0] != '8'):
        if (r[1] == '5'):
            return (r[0] + 'n')
        elif (r[1] == '7'):
            if (r[0] != '2'):
                return (r[0] + 's')
            else:
                return ('2e-sw')
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
def djikstra(s,e):
    path = boelterG.djikstra(s,e)
    return path
    # process path to give real directions 
    #return printPath(path)

out = boelterG.djikstra('7e-sw','HILL')
print(out)
