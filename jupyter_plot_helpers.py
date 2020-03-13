import matplotlib
from matplotlib import pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import FancyArrowPatch, Circle, RegularPolygon
import numpy as np
matplotlib.rc('text', usetex=True)
size = 1.35

class std_kwargs:
    text = {'ha': 'center', 'va': 'bottom', 'fontsize': 18}

def setup_plot():
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    plt.axis("equal")
    limit = 1.0/size
    plt.xlim(left=-limit)
    plt.xlim(right=limit)
    plt.ylim(bottom=-limit)
    plt.ylim(top=limit)
    return fig, ax

def base_circle(ax):
    center = Circle((0,0), 0.02, fill=True, clip_on=False, color='k')
    ax.add_artist(center)
    circle = Circle((0,0), 1.0, fill=False, clip_on=False, color='k')
    ax.add_artist(circle)
    radius = FancyArrowPatch((0.0, 0.0), (1.0, 0.0), clip_on=False, color='k', arrowstyle='->', mutation_scale=50)
    ax.add_artist(radius)
    radius_label = plt.text(0.5, -0.1, "r=1.0", **std_kwargs.text)
