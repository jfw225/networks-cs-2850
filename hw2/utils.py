import matplotlib.pyplot as plt
from matplotlib import patches

##### Letter Enumeration #####
A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"
H = "H"
I = "I"
J = "J"
K = "K"
L = "L"


def draw_and_close_on_input():
    plt.draw()
    plt.pause(0.1)
    input("Press Enter to continue...")
    plt.close()


def visibility_rectange(x, y, w, h):
    """
    Returns a matplotlib patch representing a visibility rectangle centered at 
    (x, y) with width w and height h.
    """

    return patches.Rectangle((x - w/2, y - h/2), w, h, fill=True, edgecolor='black', linewidth=2, facecolor='black')
