import sys
import random
from PyQt5.QtWidgets import QPushButton

from matplotlib.backends.qt_compat import QtCore, QtWidgets
if QtCore.qVersion() >= "5.":
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        static_canvas = FigureCanvas(Figure(figsize=(5, 3)))
        layout.addWidget(static_canvas)
        self.addToolBar(NavigationToolbar(static_canvas, self)) 

        # plot the vertices
        self._static_ax = static_canvas.figure.subplots()
        self._static_ax.plot(0, 0, ".", color="black")
        self._static_ax.plot(10, 0, ".", color="black")
        self._static_ax.plot(5, 5, ".", color="black")

        # plot the starting point, doesn't really matter where
        self.points = self._static_ax.plot(4, 3, ".", color="green")
        self.x = 4.0
        self.y = 3.0

        # buttons and connections for plotting points
        button1 = QPushButton("Plot point")
        button2 = QPushButton("Plot 100 points")
        button1.clicked.connect(self.plot_point)
        button2.clicked.connect(self.plot_one_hundred_points)
        layout.addWidget(button1)
        layout.addWidget(button2)
        
        # connect event for moving trace point
        self._static_ax.figure.canvas.mpl_connect('button_press_event', self.button_press_event)

    # calculates the midpoint from tracepoint to another point
    def find_midpoint(self, x2, y2) -> tuple[float, float]:
        x = (self.x+x2)/2
        y = (self.y+y2)/2
        return x, y

    # event for moving tracepoint
    def button_press_event(self, event):
        self.x = event.xdata
        self.y = event.ydata
        self.points[0].remove()
        self.points = self._static_ax.plot(self.x, self.y, ".", color="green")
        self._static_ax.figure.canvas.draw()
    
    # event for plotting point
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
        self.points[0].set_color("red")
        self.points = self._static_ax.plot(self.x, self.y, ".", color="green")
        self._static_ax.figure.canvas.draw()
        print(self.x, self.y)

    # event for plotting 100 points    
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