#Social Computing CS522
#Programming Assignment #5
#(Submission Deadline: 22nd October 2020)

#Note: The functions given in the assignment are entirely based on the video lectures related to Random Walk Method for Implementing Page Rank. For further details you can refer the related videos.

#If there is any query related to assignment you should ask at least 48 hours before the deadline, no reply would be given in case you ask during the last 48 hours.
#Please avoid asking any syntax related queries, if you feel anything given can lead to an error, you may change it but make sure the desired output does not change.
#Kindly do not delete any test cases given in the program.

import networkx as nx
import random
from networkx.algorithms.distance_measures import radius
import numpy as np

random.seed(30)


#Creating empty graph, adding 'N' nodes and some edges based on the probability 'p'
def create_graph(N, p):
    G = nx.DiGraph()  #empty graph
    G.add_nodes_from([i for i in range(N)])
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                r = random.random()
                if r <= p:
                    G.add_edge(i, j)
                else:
                    continue
    return G


#Returns the sorted nodes based on the points accumulated using random walk in descending order
def get_nodes_sorted_by_RW(points):
    ##Your Code goes here
    parray = np.array(points)
    nodes_sorted_by_RW = np.argsort(-parray)
    return nodes_sorted_by_RW


#Returns the points accumulated using random walk executed for 10000 steps, as given in the video lectures
def random_walk(G):
    ##Your Code goes here
    nodes = list(G.nodes())
    RW_points = [0] * G.number_of_nodes()
    rd = random.choice(nodes)
    count = 10000
    for i in range(count):
        out = list(G.out_edges(rd))
        if (len(out) == 0):
            rd = random.choice(nodes)
        else:
            rd = random.choice(out)[1]
        RW_points[rd] += 1
    return RW_points


#Please print your entry number, for example replace <Entry number> by 2014csz0001, Kindly do not delete this statement.
print('2017csb1091')

# Test Case 1 with N=5 and p=0.3
N = 5
p = 0.3

G = create_graph(N, p)
# 2. Perform a random walk
RW_points = random_walk(G)

# 3. Get nodes' raking as per the points accumulated
nodes_sorted_by_rwalk = get_nodes_sorted_by_RW(RW_points)

print('Nodes sorted by Random Walk : ',
      ' '.join(map(str, nodes_sorted_by_rwalk)))

# 4. Compare the ranks thus obtained with the ranks obtainrd from the inbuilt Page rank method
pr = nx.pagerank(G)  # Return a dictionary
pr_sorted = sorted(pr.items(), key=lambda x: x[1], reverse=True)

inbuilt_node_list = []
for i in pr_sorted:
    inbuilt_node_list.append(i[0])

print('Nodes sorted by Inbuilt Page Rank Method: ',
      ' '.join(map(str, inbuilt_node_list)))

# Test Case 2 with N=10 and p=0.3
N = 10
p = 0.3

G = create_graph(N, p)
# 2. Perform a random walk
RW_points = random_walk(G)

# 3. Get nodes' raking as per the points accumulated
nodes_sorted_by_rwalk = get_nodes_sorted_by_RW(RW_points)

print('Nodes sorted by Random Walk : ',
      ' '.join(map(str, nodes_sorted_by_rwalk)))

# 4. Compare the ranks thus obtained with the ranks obtainrd from the inbuilt Page rank method
pr = nx.pagerank(G)  # Return a dictionary
pr_sorted = sorted(pr.items(), key=lambda x: x[1], reverse=True)

inbuilt_node_list = []
for i in pr_sorted:
    inbuilt_node_list.append(i[0])

print('Nodes sorted by Inbuilt Page Rank Method: ',
      ' '.join(map(str, inbuilt_node_list)))

# Test Case 3 with N=20 and p=0.5
N = 20
p = 0.5

G = create_graph(N, p)
# 2. Perform a random walk
RW_points = random_walk(G)

# 3. Get nodes' raking as per the points accumulated
nodes_sorted_by_rwalk = get_nodes_sorted_by_RW(RW_points)

print('Nodes sorted by Random Walk : ',
      ' '.join(map(str, nodes_sorted_by_rwalk)))

# 4. Compare the ranks thus obtained with the ranks obtainrd from the inbuilt Page rank method
pr = nx.pagerank(G)  # Return a dictionary
pr_sorted = sorted(pr.items(), key=lambda x: x[1], reverse=True)

inbuilt_node_list = []
for i in pr_sorted:
    inbuilt_node_list.append(i[0])

print('Nodes sorted by Inbuilt Page Rank Method: ',
      ' '.join(map(str, inbuilt_node_list)))
'''
##Expected Output after running your code
<Entry number>
Nodes sorted by Random Walk :  2 0 3 1 4
Nodes sorted by Inbuilt Page Rank Method:  2 0 3 1 4
Nodes sorted by Random Walk :  4 2 9 0 3 8 7 6 1 5
Nodes sorted by Inbuilt Page Rank Method:  4 2 9 0 3 8 7 6 1 5
Nodes sorted by Random Walk :  19 16 11 4 17 2 0 14 10 8 1 7 15 18 3 12 9 13 5 6
Nodes sorted by Inbuilt Page Rank Method:  19 16 11 4 2 17 14 10 18 8 0 1 7 15 3 13 5 12 6 9
'''

##You may use other functions but make sure I would be directly running your .py file on terminal and no marks will be provided for any kind of errors.
## Kindly do not add any additional print statements other than given in the code.
'''
Important Notes: 
1)Your file should be named as scomp_asg05_<Your entry number>.py. For example if your entry number is 2014csz0001, your file name should be scomp_asg05_2014csz0001.py. (use only small letters)
2) Make sure you do not copy the code neither from internet nor from any other student.
3) Strictly follow the guidelines given regarding the unimplemented functions and use only Python3.
4) No marks will be given in case of syntactical errors, logical errors of any kind.
5) Your .py file will be executed directly on the command prompt or terminal, so do take care of that.

'''