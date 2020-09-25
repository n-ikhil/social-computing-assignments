import networkx as nx
import random


def analyze_network(G):
    nNodes = G.order()
    nEdges = G.size()
    avDeg = 2 * (nEdges / nNodes)
    avClusCoef = nx.average_clustering(G)
    print("\nNumber of nodes = " + str(nNodes),
          "\nNumber of edges = " + str(nEdges),
          "\nAverage degree  = " + str(avDeg),
          "\nAverage clustering coefficient = " + str(avClusCoef), "\n")


def find_num_edges(n):
    G = nx.Graph()
    G.add_nodes_from(range(n))
    allNodes = list(G.nodes())
    while nx.is_connected(G) == False:
        nodeA = random.choice(allNodes)
        nodeB = random.choice(allNodes)
        if (nodeA != nodeB):
            G.add_edge(nodeA, nodeB)
    print("Number of edges for connecting the graph = ", G.size())


def find_num_comm(G):
    while nx.is_connected(G):
        bets = nx.edge_betweenness_centrality(G)
        betsAsList = bets.items()
        remEdge = max(betsAsList, key=lambda item: item[1])
        remEdge = remEdge[0]
        G.remove_edge(*remEdge)
    print("\nNumber of communities = ", nx.number_connected_components(G),
          "\n")


# return len(nx.connected_components(G))

G = nx.complete_graph(5)
analyze_network(G)
find_num_edges(20)
find_num_comm(G)
