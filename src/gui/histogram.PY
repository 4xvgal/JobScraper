import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def draw_graph(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.ax.plot(x, y)  # sin 함수를 그립니다.
        self.canvas.draw()  # 그래프를 캔버스에 그립니다.

