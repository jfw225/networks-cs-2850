
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import patches

from utils import *


def q():
    # create the graph
    graph = nx.Graph()
    graph.add_nodes_from(base_graph)

    h_allies, l_allies = list(), list()
    for x in base_graph:
        dh = nx.shortest_path_length(base_graph, x, H)
        di = nx.shortest_path_length(base_graph, x, I)

        # if `x` is closer to `H` than `I`, then it is an ally of `H`
        if dh < di:
            h_allies.append(x)
            graph.add_edge(x, H, weight=1)

        # if `x` is closer to `I` than `H`, then it is an ally of `I`
        else:
            l_allies.append(x)
            graph.add_edge(x, I, weight=1)

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'),
                           node_size=500)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos,
                           edge_color='b', arrows=False)
    draw_and_close_on_input()


def q():
    # create the graph
    graph = nx.Graph()

    # create a list of edges from A to B, A to C, C to B, A to D, D to B
    route1 = [((A, C), "4"), ((C, B), r"$\frac{x}{20}$")]
    route2 = [((A, D), r"$\frac{y}{10}$"), ((D, B), "2")]
    route3 = [((A, B), "12")]
    route4 = [((C, D), "0")]

    # add the edges to the graph
    graph.add_edges_from([e for e, _ in route1])
    graph.add_edges_from([e for e, _ in route2])
    graph.add_edges_from([e for e, _ in route3])
    graph.add_edges_from([e for e, _ in route4])

    pos = nx.spring_layout(graph)
    print(pos)
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'),
                           node_size=500)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos,  connectionstyle="arc3,rad=0.1",
                           edge_color='b', arrows=False)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=dict(route1))
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=dict(route2))
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=dict(route3))
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=dict(route4))
    draw_and_close_on_input()


if __name__ == '__main__':
    q()
