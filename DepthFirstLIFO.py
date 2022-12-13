import networkx as nx
from Graph import City, load_graph

def is_twentieth_century(year):
    return year and 1901 <= year <= 2000

nodes, graph = load_graph("roadmap.dot", City.from_dict)
for node in nx.dfs_tree(graph, nodes["oxford"]):
    print("->", node.name)
    if is_twentieth_century(node.year):
        print("\n\nFound:", node.name, node.year)
        break
    else:
        print("Not found")