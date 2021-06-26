import sys
import time
import numpy as np
import random
import math
from PyQt5.QtWidgets import QPushButton

from matplotlib.backends.qt_compat import QtCore, QtWidgets
if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

@QtCore.Slot()
def say_hello():
    print("Button clicked, Hello!")




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)
        self.addToolBar(NavigationToolbar(static_canvas, self)) 

        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.plot(0, 0, ".", color="black")
        self._static_ax.plot(10, 0, ".", color="black")
        self._static_ax.plot(5, 5, ".", color="black")
        self._static_ax.plot(4, 3, ".", color="red")

        self.x = 4.0
        self.y = 3.0

        button1 = QPushButton("Plot point")
        button2 = QPushButton("Plot 100 points")
        button1.clicked.connect(self.plot_point)
        button2.clicked.connect(self.plot_one_hundred_points)
        
        layout.addWidget(button1)
        layout.addWidget(button2)

    def _update_canvas(self):
        t = np.linspace(0, 10, 101)
        # Shift the sinusoid as a function of time.
        self._line.set_data(t, np.sin(t + time.time()))
        self._line.figure.canvas.draw()

    def find_midpoint(self, x2, y2) -> tuple[float, float]:
        x = (self.x+x2)/2
        y = (self.y+y2)/2
        return x, y
    
    @QtCore.Slot()
    def plot_point(self):
        print(f"start: ({self.x}, {self.y})")
        r = random.randint(0, 2)
        if r == 0:
            print("vertice (0,0)")
            self.x, self.y = self.find_midpoint(0.0, 0.0)
        elif r == 1:
            print("vertice (5, 5)")
            self.x, self.y = self.find_midpoint(5.0, 5.0)
        else:
            print("vertice (10, 0)")
            self.x, self.y = self.find_midpoint(10.0, 0.0)
        
        self._static_ax.plot(self.x, self.y, ".", color="red")
        self._static_ax.figure.canvas.draw()
        print(self.x, self.y)

    
    @QtCore.Slot()
    def plot_one_hundred_points(self):
        for i in range(100):
            self.plot_point()


if __name__ == "__main__":
    # Check whether there is already a running QApplication (e.g., if running
    # from an IDE).
    qapp = QtWidgets.QApplication.instance()
    if not qapp:
        qapp = QtWidgets.QApplication(sys.argv)

    app = ApplicationWindow()
    app.show()
    app.activateWindow()
    app.raise_()
    qapp.exec_()