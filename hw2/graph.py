import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import patches

from utils import *

base_graph = nx.Graph()

# add edges from A to F, B to F, C to F, D to F, E to F, F to G, G to H, I to J, J to K, and K to L
base_graph.add_edges_from([(A, F), (B, F), (C, F), (D, F),
                           (E, F), (F, G), (G, H), (H, I), (I, J), (J, K), (K, L)])


def q5a():

    are_allies = dict()
    for x in base_graph:
        are_allies[x] = dict()
        for y in base_graph:
            d = nx.shortest_path_length(base_graph, x, y)

            # if the distance is at most 2, then they are allies
            are_allies[x][y] = d <= 2

    # create the graph
    graph = nx.Graph()
    graph.add_nodes_from(base_graph)

    # add the edges
    allies, enemies = list(), list()
    for x in base_graph:
        for y in base_graph:
            weight = 1 if are_allies[x][y] else -1
            graph.add_edge(x, y, weight=weight)

            # add the edge to the correct list
            if are_allies[x][y]:
                allies.append((x, y))
            else:
                enemies.append((x, y))

    for x in base_graph:
        for y in base_graph:
            for z in base_graph:
                # get the weights of the edges
                w1 = graph.get_edge_data(x, y)['weight']
                w2 = graph.get_edge_data(y, z)['weight']
                w3 = graph.get_edge_data(x, z)['weight']

                w_sum = w1 + w2 + w3

                if w_sum == 1:
                    break
            else:
                continue
            break
        else:
            continue
        break

    allies_adj = [
        edge for edge in allies if sum([x in edge, y in edge, z in edge]) > 1]
    enemies_adj = [
        edge for edge in enemies if sum([x in edge, y in edge, z in edge]) > 1]

    print(allies_adj, enemies_adj)

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, nodelist=[x, y, z], cmap=plt.get_cmap('jet'),
                           node_size=500)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, edgelist=allies_adj,
                           edge_color='b', arrows=False)
    nx.draw_networkx_edges(graph, pos, edgelist=enemies_adj,
                           edge_color='r', arrows=False)
    draw_and_close_on_input()


def q5b():
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


def q5d():
    # create the graph
    graph = nx.Graph()
    graph.add_nodes_from(base_graph)

    h_allies, l_allies = list(), list()
    for x in base_graph:
        for y in base_graph:
            dx = nx.shortest_path_length(base_graph, x, F)
            dy = nx.shortest_path_length(base_graph, y, F)

            # if both `x` and `y` have a distance of at most 5 from `F`, then
            # add an edge between them
            if dx <= 5 and dy <= 5:
                graph.add_edge(x, y, weight=1)

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'),
                           node_size=500)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos,
                           edge_color='b', arrows=False)
    draw_and_close_on_input()


def q2a():
    graph = nx.DiGraph()
    graph.add_edges_from(
        [(A, B), (A, F), (B, A), (B, F), (B, C), (C, B), (C, D),
         (C, E), (C, F), (D, C), (D, E), (D, G), (E, C), (E, D), (F, C)]
    )

    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, cmap=plt.get_cmap('jet'),
                           node_size=50)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos, edge_color='r', arrows=False)
    draw_and_close_on_input()


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
    q5d()
