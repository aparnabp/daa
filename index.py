# usr/bin/python
import networkx as nx
import time
from source import dfs_edges,bfs_edges
# rnadom graph
G = nx.complete_graph(10)
G.add_node(12)
# print G.nodes()

#dfs_predecessors(G);

start_time = time.time()
print("the dfs edges are")
print list(dfs_edges(G,0));
print "time taken"
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
print("the bfs edges are")
print list(bfs_edges(G,0));
print "time taken"
print("--- %s seconds ---" % (time.time() - start_time))
# https://networkx.github.io/documentation/latest/reference/algorithms.traversal.html

# DFS source code
# https://networkx.github.io/documentation/latest/_modules/networkx/algorithms/traversal/depth_first_search.html

# BFS source code
# https://networkx.github.io/documentation/latest/_modules/networkx/algorithms/traversal/breadth_first_search.html

# ithokke nokki nale chythond vara, plus graph nokk

# json data kude padikk
# https://docs.python.org/2/library/json.html

# and githhubil account undakk IPPO!!

