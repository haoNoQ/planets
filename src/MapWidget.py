
from PyQt5 import Qt


class MapWidget(Qt.QGraphicsView):
    def __init__(self, parent):
        super(MapWidget, self).__init__(parent)
