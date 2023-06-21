import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def draw_graph(ax, canvas):
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y)  # sin 함수를 그립니다.
    canvas.draw()

