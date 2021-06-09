import networkx as nx
from get_col_values import get_col_values
from datas import wgm_bool

def make_graph(list_of_nodes, metrics, exclude_same_question=True, df=wgm_bool):
    G = nx.Graph()
    for i, node_i in enumerate(list_of_nodes):
        for j, node_j in enumerate(list_of_nodes):
            if j <= i:
                continue

            if exclude_same_question:
                if node_i.split(sep=':')[0] == node_j.split(sep=':')[0]:
                    # if they belong to the same question
                    continue

            [c1, c2] = get_col_values([node_i,node_j], df=df)
            weight = metrics(c1, c2)
            G.add_weighted_edges_from([(node_i,node_j,weight)])
    return G