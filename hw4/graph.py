
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import patches
import pandas as pd

from utils import *


def q(graph):
    transpose = {
        key: [k for k, v in graph.items() if key in v] for key in graph
    }

    def appendToDataFrame(df, auth, hub, step):
        df.loc[step*4] = auth
        df.rename(
            index={step*4: "Step {}: unnormalized auth".format(step)}, inplace=True)

        df.loc[step*4 + 1] = hub
        df.rename(
            index={step*4 + 1: "Step {}: unnormalized hub".format(step)}, inplace=True)

        # df.loc[step*4+2] = [str(i) + "/" + str(sum(auth)) for i in auth]
        df.loc[step*4+2] = [round(100 * i / sum(auth)) / 100 for i in auth]
        df.rename(
            index={step*4+2: "Step {}: normalized auth".format(step)}, inplace=True)

        # df.loc[step*4+3] = [str(i) + "/" + str(sum(hub)) for i in hub]
        df.loc[step*4+3] = [round(100 * i / sum(hub)) / 100 for i in hub]
        df.rename(
            index={step*4+3: "Step {}: normalized hub".format(step)}, inplace=True)

    STEPS = 2
    df = pd.DataFrame(columns=graph.keys())

    auth = [1 for i in range(len(graph))]
    hub = [1 for i in range(len(graph))]
    df.loc[0] = auth
    df.rename(index={0: "Step 0: initial auth"}, inplace=True)
    df.loc[1] = hub
    df.rename(index={1: "Step 0: initial hub"}, inplace=True)
    for step in range(STEPS):
        for key, value in transpose.items():
            auth[ord(key) - 65] = sum(hub[ord(v)-65] for v in value)

        for key, value in graph.items():
            hub[ord(key) - 65] = sum(auth[ord(v)-65] for v in value)

        appendToDataFrame(df, auth, hub, step+1)

    print(df)


graph = {
    A: [],
    B: [],
    C: [A],
    D: [A],
    E: [A, B],
    F: [B]
}

option1 = {**graph,
           G: [],
           H: [G]
           }

option2 = {**graph,
           G: [],
           H: [G, A, B]
           }

option3 = {**graph,
           G: [G, H],
           H: [G, I, B],
           I: [G, H, A, C],
           }

if __name__ == '__main__':
    # q(option1)
    # q(option2)
    q(option3)
