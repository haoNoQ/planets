
from PyQt5 import Qt

from src.MapWidget import MapWidget
from src.ControlWidget import ControlWidget


class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self._gameMenu = self.menuBar().addMenu("&Game")
        self._widgetsMenu = self.menuBar().addMenu("&Widgets")

        self._mapWidget = MapWidget(self)
        self.setCentralWidget(self._mapWidget)

        self._exitAction = Qt.QAction("&Quit", self)
        self._exitAction.setShortcut("Ctrl+Q")
        self._exitAction.triggered.connect(self.close)

        self._gameMenu.addAction(self._exitAction)

        self._controlWidget = ControlWidget(self)
        self._controlDockWidget = Qt.QDockWidget("&Controls", self)
        self._controlDockWidget.setWidget(self._controlWidget)
        self.addDockWidget(Qt.Qt.RightDockWidgetArea, self._controlDockWidget)

        self._widgetsMenu.addAction(self._controlDockWidget.toggleViewAction())

    def mapWidget(self):
        return self._mapWidget

    def controlWidget(self):
        return self._controlWidget
