import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import patches

from utils import *


def q2a():
    graph = nx.DiGraph()
    graph.add_edges_from(
        [(A, B), (A, F), (B, A), (B, F), (B, C), (C, B), (C, D),
         (C, E), (C, F), (D, C), (D, E), (D, G), (E, C), (E, D), (F, C)]
    )

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'),
                           node_size=500)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, edge_color='r', arrows=False)
    plt.show()


def q2b():
    graph = nx.DiGraph()

    # create the nodes
    graph.add_node(A, pos=(2.5, -2.5))
    graph.add_node(B, pos=(0, 0))
    graph.add_node(C, pos=(1, 0))
    graph.add_node(D, pos=(2, 0))
    graph.add_node(E, pos=(3, 0))
    graph.add_node(F, pos=(4, 0))
    graph.add_node(G, pos=(5, 0))

    # draw the graph
    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'))
    nx.draw_networkx_edges(graph, pos, edge_color='r', arrows=False)
    nx.draw_networkx_labels(graph, pos)

    # create the visibility rectangles
    visibility_rectangles = [
        patches.Rectangle(
            (x, -.25/2), .5, .25, fill=True, edgecolor='r', linewidth=2, facecolor='r'
        )
        for x in [.25, 1.25, 2.25, 3.25, 4.25]]

    # draw the rectangles
    ax = plt.gca()
    for rect in visibility_rectangles:
        ax.add_patch(rect)

    draw_and_close_on_input()


def q2c():
    graph = nx.DiGraph()

    # create the nodes
    graph.add_node(B, pos=(2, 0))
    graph.add_node(C, pos=(2.5, 1))
    graph.add_node(A, pos=(3, -1))
    graph.add_node(D, pos=(3, 0))
    graph.add_node(E, pos=(4, -1))
    graph.add_node(F, pos=(4, 0))

    # create the edges
    graph.add_edges_from(
        [(B, C), (B, A), (A, D), (A, F), (F, E), (E, D), (D, C)])

    # create the visibility rectangles
    visibility_rectangles = [
        visibility_rectange(2.625, 0, .25, .5),
        visibility_rectange(3, -.5, .25, .25),
        visibility_rectange(3.5, .75, .25, 2),
        visibility_rectange(3.5, -1, .25, .5),
    ]

    # draw the graph
    pos = nx.get_node_attributes(graph, 'pos')
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'))
    nx.draw_networkx_edges(graph, pos, edge_color='r',
                           arrows=False, style="--")
    nx.draw_networkx_labels(graph, pos)

    # draw the rectangles
    ax = plt.gca()
    for rect in visibility_rectangles:
        ax.add_patch(rect)

    draw_and_close_on_input()


def q2d():
    graph = nx.DiGraph()

    # create the nodes
    graph.add_node(B, pos=(2, 0))
    graph.add_node(C, pos=(2.5, 1))
    graph.add_node(A, pos=(3, -1))
    graph.add_node(D, pos=(3, 0))
    graph.add_node(E, pos=(4, -1))
    graph.add_node(F, pos=(4, 0))

    # create the edges
    graph.add_edges_from(
        [(B, C), (B, A), (A, D), (A, F), (F, E), (E, D), (D, C)])

    # create the visibility rectangles
    visibility_rectangles = [
        visibility_rectange(2.5, -.25, .25, .5),
        visibility_rectange(3.25 + .25/2, -.25, .25, 2),
        visibility_rectange(3.25+.25/2, -1.25, .25, .5),
    ]

    # draw the graph
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'))
    nx.draw_networkx_edges(graph, pos, edge_color='r',
                           arrows=False, style="--")
    nx.draw_networkx_labels(graph, pos)

    # draw the rectangles
    ax = plt.gca()
    for rect in visibility_rectangles:
        ax.add_patch(rect)

    draw_and_close_on_input()


def q3a():
    graph = nx.DiGraph()

    # create edges from vipul to wendy, wendy to yvette, yvette to zoe, xin to wendy, and xin to yvette
    graph.add_edges_from([("Vipul", "Wendy"), ("Wendy", "Yvette"),
                         ("Yvette", "Zoe"), ("Xin", "Wendy"), ("Xin", "Yvette")])

    # draw the graph
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(
        graph, pos, cmap=plt.get_cmap('jet'), node_size=5000)
    nx.draw_networkx_edges(graph, pos, edge_color='r', arrows=False)
    nx.draw_networkx_labels(graph, pos)

    draw_and_close_on_input()


def q3b():
    graph = nx.DiGraph()

    # create edges from vipul to wendy, wendy to yvette, yvette to zoe, xin to wendy, and xin to yvette
    edges = [("Vipul", "Wendy"), ("Wendy", "Yvette"),
             ("Yvette", "Zoe"), ("Xin", "Wendy"), ("Xin", "Yvette")]
    graph.add_edges_from(edges)

    # create the strong/weak edge labels
    edge_labels = ["weak", "strong", "strong", "strong", "weak"]

    # draw the graph
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(
        graph, pos, cmap=plt.get_cmap('jet'), node_size=2000)
    nx.draw_networkx_edges(
        graph, pos, edge_color='r', arrows=False)
    nx.draw_networkx_edge_labels(
        graph, pos, edge_labels={e: l for e, l in zip(edges, edge_labels)}, font_color="red")
    nx.draw_networkx_labels(graph, pos)

    draw_and_close_on_input()


def q4a():
    graph = nx.DiGraph()

    # 20 students
    n = 4

    # create 20 nodes for the floors 1 through 4
    for i in range(n):
        graph.add_node(f"f1s{i}", pos=(i*10000, 1))
        graph.add_node(f"f2s{i}", pos=(i*10000, 2))
        graph.add_node(f"f3s{i}", pos=(i*10000, 3))
        graph.add_node(f"f4s{i}", pos=(i*10000, 4))

    for f in range(1, 5):
        for s1 in range(n):
            for s2 in range(n):
                if s1 == s2:
                    continue
                graph.add_edge(f"f{f}s{s1}", f"f{f}s{s2}")

    # draw the graph
    pos = nx.get_node_attributes(graph, 'pos')
    print(pos)
    nx.draw_networkx_nodes(
        graph, pos, cmap=plt.get_cmap('jet'), node_size=1000)
    nx.draw_networkx_edges(
        graph, pos, edge_color='r', connectionstyle="arc3,rad=0.1")
    # nx.draw_networkx_edge_labels(
    #     graph, pos, edge_labels={e: l for e, l in zip(edges, edge_labels)}, font_color="red")
    nx.draw_networkx_labels(graph, pos)

    ax = plt.gca()
    ax.set_ylim([0, 4.5])

    draw_and_close_on_input()


if __name__ == '__main__':
    q4a()
