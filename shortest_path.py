import networkx as nx
import json

def shortest_path(json_file,p1,p2):
    G = nx.DiGraph()
    with open(json_file, 'r') as f:
        data = json.load(f)
    for key,values in data.items():
        for element in values:
            G.add_edge(str(key),str(element)) 
    
    return nx.shortest_path(G,p1,p2)

x=shortest_path("dico_unique.json","Winston_Churchill","Survivalisme") 
print(x)