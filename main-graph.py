import networkx as nx
import matplotlib.pyplot as plt
import json

def create_from_json(json_file):
    G = nx.Graph()
    with open(json_file, 'r') as f:
        data = json.load(f)
    for key,values in data.items():
        for element in values:
            G.add_edge(str(key),str(element)) 
    
    # print(nx.shortest_path(G,"x","y")) 
    plt.figure(num=None, figsize=(20, 20), dpi=80)
    plt.axis('off')
    nx.draw_spring(G, with_labels=True)
    plt.show()

create_from_json("dico_unique.json")