import math
import networkx as nx
import random


def homophily(G):
    ans = []
    ans.append(G.size())
    allNodes = list(G.nodes(data=True))
    for node1 in allNodes:
        if (node1[1]['type'] == 'foci'):
            continue
        for node2 in allNodes:
            if (node2[0] == node1[0] or node2[1]['type'] == 'foci'):
                continue
            diff = abs(node1[1]['name'] - node2[1]['name'])
            p = float(1) / (diff + 1000)
            r = random.uniform(0, 1)
            if (r < p):
                G.add_edge(node1[0], node2[0])
    ans.append(G.size())
    return ans


def common_neighbors(u, v, G):
    nu = set(G.neighbors(u))
    nv = set(G.neighbors(v))
    return len(nu & nv)


def closure(G):
    ans = []
    ans.append(G.size())
    farray = []
    pconnection = 0.01
    allNodes = list(G.nodes(data=True))
    for node1 in allNodes:
        for node2 in allNodes:
            if ((node1[0] != node2[0]) and (node1[1]['type'] == 'person'
                                            or node2[1]['type'] == 'person')):
                k = common_neighbors(node1[0], node2[0], G)
                p = 1 - math.pow((1 - pconnection), k)
                cur = [node1[0], node2[0], p]
                farray.append(cur)
    for newEdge in farray:
        [u, v, p] = newEdge
        r = random.uniform(0, 1)
        if r < p:
            G.add_edge(u, v)

    ans.append(G.size())
    return ans


def count_bmi(val, G):
    sum = 0
    allNodes = list(G.nodes(data=True))
    for node in allNodes:
        if (node[1]['type'] == 'person' and node[1]['name'] == val):
            sum += 1
    return sum


def change_bmi(G):
    ans = []
    ans.append(count_bmi(40, G))
    allNodes = list(G.nodes(data=True))
    for fnode in allNodes:
        if (fnode[1]['type'] == 'foci' and fnode[1]['name'] == 'eat_out'):
            for pnode in G.neighbors(fnode[0]):
                if G.nodes[pnode]['name'] < 40:
                    G.nodes[pnode]['name'] += 1
    ans.append(count_bmi(40, G))
    return ans