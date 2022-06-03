import random

import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
A = nx.Graph()
F = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 4)
G.add_edge(3, 4)
G.add_edge(5, 6)
G.add_edge(5, 9)
G.add_edge(5, 10)
G.add_edge(6, 10)
G.add_edge(6, 7)
G.add_edge(7, 10)
G.add_edge(7, 8)
G.add_edge(8, 9)
G.add_edge(8, 10)
G.add_edge(9, 10)
G.add_edge(8, 6)
G.add_edge(6, 9)

G.add_node(11)

# explicitly set positions
pos = {1: (-20, 8), 2: (-20, -8), 3: (-8, 0), 4: (-16, 0), 5: (15, 8), 6: (6, 0), 7: (8, -8), 8: (20, -8), 9: (20, 4),
       10: (15, -2), 11: (30, 0)}

options = {
    "font_size": 10,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 3,
    "width": 3,
}
nx.draw_networkx(G, pos, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
H = nx.DiGraph(G)

'''
When you call plt.show() in your script, it seems something like
file object is still open, and plt.savefig method for writing
can not read from that stream completely. but there is a block option 
for plt.show that can change this behavior, so you can use it:
'''
#plt.show()

'''
dpi= specifies how many dots per inch (image resolution) are in the saved image,
And that's why the program executed so slow
'''
plt.savefig("output/Graph.png", dpi=1000, format="PNG")

graph = {
        '1': set(['2', '3', '4']),
        '2': set(['1', '4', '3']),
        '3': set(['1', '4', '2']),
        '4': set(['1', '2', '3']),
        '5': set(['6', '9', '10']),
        '6': set(['5', '9', '10', '8', '7']),
        '7': set(['6', '8', '10']),
        '8': set(['10', '9', '7', '6']),
        '9': set(['10', '5', '6', '8']),
        '10': set(['5', '6', '7', '8', '9']),
        '11': set([])}







def dfs(visited, graph, node):  #function for dfs
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


nx.draw_networkx(G, pos, **options)
visited = []
dfs(visited, graph, '1')
i=0
for each in visited:
    while i < len(visited) - 1:
        A.add_edge(int(visited[i]), int(visited[i + 1]))
        i += 1

options = {
    "font_size": 10,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "edge_color": "red",
    "linewidths": 3,
    "width": 3,
}
nx.draw_networkx(F, pos, **options)


visited = []
dfs(visited, graph, '5')
i=0
while i < len(visited)-1:
    A.add_edge(int(visited[i]), int(visited[i+1]))
    i+=1
options = {
    "font_size": 10,
    "node_size": 500,
    "node_color": "white",
    "edgecolors": "black",
    "edge_color": "red",
    "linewidths": 3,
    "width": 3,
}
nx.draw_networkx(A, pos, **options)

#plt.show()
plt.savefig("output/tree.png", dpi=1000, format="PNG")
# Pick a random node
source = random.choice(list(G.nodes))

# Find the longest shortest path from the node
shortest_paths = nx.shortest_path(G, source=source)
target = max(shortest_paths, key=lambda i: len(shortest_paths[i]))
l_s_path = shortest_paths[target]
l_s_path_edges = list(zip(l_s_path, l_s_path[1:]))

# Draw the graph, then draw over the required edges in red.
nx.draw(G, pos=pos, with_labels=True)
nx.draw_networkx_edges(G, edge_color='r', edgelist=l_s_path_edges, pos=pos)
#plt.show()
plt.savefig("output/diam_random_draph.png", dpi=1000, format="PNG")