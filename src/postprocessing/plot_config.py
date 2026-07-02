import matplotlib.pyplot as plt
from matplotlib import rcParams

styles = {
    'markers': ['o', '+', '^', 's'],  # circle, square, triangle, diamond
    'linestyles': ['-', '--', ':', '-.'],  # solid, dashed, dotted, dash-dot
    'colors': ['blue', 'red', 'green', 'purple']
}

def configure_matplotlib():
    SMALL_SIZE = 18
    MEDIUM_SIZE = 20
    BIGGER_SIZE = 22

    rcParams.update({'figure.autolayout': True, 
                     'text.usetex': True,
                     'font.family': 'serif',
                     "font.serif": ["Computer Modern Roman"],
                     'text.latex.preamble':r"\usepackage{amsmath}\usepackage{amssymb}\usepackage{bm}",
                     'legend.loc':'upper right',
                     'font.size': SMALL_SIZE,
                     'axes.titlesize': BIGGER_SIZE,
                     'axes.labelsize': MEDIUM_SIZE,
                     'xtick.labelsize': SMALL_SIZE,
                     'legend.fontsize': SMALL_SIZE,
                     'figure.titlesize': BIGGER_SIZE
                     })
    