import networkx as nx
import scomp_asg02_2017csb1091 as ass
import random


def create_graph():
    G = nx.Graph()
    G.add_nodes_from(range(1, 101))
    return G


def assign_bmi(G):
    for node in G.nodes():
        G.nodes[node]['name'] = random.randint(15, 40)
        G.nodes[node]['type'] = 'person'
    return G


foci_nodes = ['gym', 'eat_out', 'movie_club', 'karate_club', 'yoga_club']


def add_foci_nodes(G):
    global foci_nodes
    n = G.number_of_nodes()
    i = n + 1
    for j in range(len(foci_nodes)):
        G.add_node(i)
        G.nodes[i]['name'] = foci_nodes[j]
        G.nodes[i]['type'] = 'foci'
        i = i + 1
    return G


def add_foci_edges(G):
    global foci_nodes
    allNodes = list(G.nodes(data="type"))
    fociNodes = []
    for node in allNodes:
        if (node[1] == 'foci'):
            fociNodes.append(node[0])
    for node in allNodes:
        if (node[1] == 'person'):
            G.add_edge(node[0], random.choice(fociNodes))
    return G


G = create_graph()
G = assign_bmi(G)
G = add_foci_nodes(G)
G = add_foci_edges(G)
print(ass.homophily(G))
print(ass.closure(G))
print(ass.change_bmi(G))
