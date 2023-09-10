import networkx as nx
import json
import matplotlib.pyplot as plt
import pandas as pd


G = nx.DiGraph()

department_labels = 'email-Eu-core-department-labels.txt'

department_labels_csv = pd.read_csv(department_labels, sep=',')

department_labels_csv.head()
print(department_labels_csv.head())

# x = nx.DiGraph(map)

# for i in range(len(inList)):
#     map[i] = 

# for i in range(NumOfNodes):
#     for j in range(len(inList[i])):
#         if inList[i][j] >= NumOfNodes:
#             continue
#         G.add_edge(i, inList[i][j], weight=inWeight[i][j]*1000)

# print(x.adj)
# nx.draw(G, with_labels=True)
# plt.show()