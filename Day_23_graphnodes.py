import networkx as nx
import re
import itertools

with open("inputs/day_23_input.txt") as file:
    data = file.read().splitlines()

nodes = []
for x in data:
    nodes.append(tuple((re.findall(r'[a-z]{2}', x))))

nodes_set = set(list(itertools.chain(*nodes)))

G = nx.Graph()

G.add_nodes_from(nodes_set)
G.add_edges_from(nodes)

node = "td"

connections = list(G.neighbors(node))

triangles = [clique for clique in nx.enumerate_all_cliques(G) if len(clique) == 3]

print(triangles)

print(len([x for x in triangles if x[0][0]=='t' or x[1][0]=='t' or x[2][0]=='t']))

cliquesp2 = list(nx.find_cliques(G))

largest_clique = max(cliquesp2, key=len)

print (",".join(sorted(largest_clique)))
