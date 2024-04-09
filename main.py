import networkx as nx
import json
# import matplotlib.pyplot as plt

class Graph:
    def __init__(self,json_file):
        self.G = nx.DiGraph()
        with open(json_file, 'r') as f:
            data = json.load(f)
        for key,values in data.items():
            for element in values:
                    self.G.add_edge(str(key),str(element)) 
    def shortest_path(self,p1,p2):
        return nx.shortest_path(self.G,p1,p2)
    # def draw(self):
    #     plt.figure(num=None, figsize=(20, 20), dpi=80)
    #     plt.axis('off')
    #     nx.draw_spring(self.G, with_labels=False)
    #     plt.show()

g = Graph("dico_unique.json")
s = g.shortest_path("Afrique","Terrorisme")
print(s)