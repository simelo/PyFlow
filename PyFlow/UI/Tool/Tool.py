from nine import str
from Qt import QtWidgets
from Qt import QtGui, QtCore


class ToolBase(object):
    """docstring for ToolBase."""
    def __init__(self):
        super(ToolBase, self).__init__()
        self.canvas = None

    def setCanvas(self, canvas):
        if self.canvas is None:
            self.canvas = canvas

    @staticmethod
    def toolTip():
        return "Default tooltip"

    @staticmethod
    def name():
        return "ToolBase"


class ShelfTool(ToolBase):
    """docstring for ShelfTool."""
    def __init__(self):
        super(ShelfTool, self).__init__()

    def contextMenuBuilder(self):
        return None

    @staticmethod
    def getIcon():
        return QtGui.QIcon.fromTheme("go-home")

    def do(self):
        print(self.name(), "called!", self.canvas)


class DockTool(QtWidgets.QDockWidget, ToolBase):
    """docstring for DockTool."""
    def __init__(self, parent=None):
        ToolBase.__init__(self)
        QtWidgets.QDockWidget.__init__(self, parent)
        self.setToolTip(self.toolTip())
        self.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea | QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea | QtCore.Qt.TopDockWidgetArea)
        self.setMinimumSize(QtCore.QSize(200, 200))

    @staticmethod
    def defaultDockArea():
        return QtCore.Qt.LeftDockWidgetArea

    def showEvent(self, event):
        self.onShow()
        super(DockTool, self).showEvent(event)

    def onShow(self):
        print(self.name(), "invoked")

    def onDestroy(self):
        print(self.name(), "destroyed")

    @staticmethod
    def showOnStartup():
        return False

    def closeEvent(self, event):
        self.onDestroy()
        self.parent().unregisterToolInstance(self)
        event.accept()