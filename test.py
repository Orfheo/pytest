import sys

import testrc

from PyQt5.QtGui import QIcon
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QMainWindow,QPlainTextEdit,QComboBox,QAction
from PyQt5.QtCore import QSize

from zaza.gigio import gigio
from zaza.papero import zizo

class Test :
    """
        Again class for testing
    """
    def __init__ ( self, x=0, y=0) :
        self.x = 0
        self.y = 0

    def __str__(self):
        return "(%s,%s)" % (self.x,self.y)

    def pippo (self):
        """
            x = 1
            y = 2
        """
        self.x = 1
        self.y = 2

class Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__( self )

        self.setMinimumSize(QSize(440, 240))
        self.setWindowTitle("test")

        self.addText(self)
        #self.addCombo(self)

        self.a = QAction ( QIcon(':/images/copy.png'), "Copy", self, triggered=self.action )
        self.t = self.addToolBar("Test")
        self.t.addAction( self.a )


    def addText(self, parent):
        self.e = QPlainTextEdit(self)
        self.e.appendPlainText("This is a test\n")
        self.e.move(40, 40)
        self.e.resize(400, 200)

    def addCombo(self, parent):
        self.i = QComboBox(parent)
        self.i.move(40, 10)
        self.i.addItem(QIcon(':/images/copy.png'), "Copy")
        self.i.addItem(QIcon(':/images/new.png'), "New")
        self.i.addItem(QIcon(':/images/cut.png'), "Cut")
        self.i.addItem(QIcon(':/images/paste.png'), "Paste")
        self.i.addItem(QIcon(':/images/save.png'), "Save")
        self.i.addItem(QIcon(':/images/open.png'), "Open")

    def action(self):
        self.e.insertPlainText("got it\n")
        self.e.verticalScrollBar().setValue(self.e.verticalScrollBar().maximum())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    t = Test ( 0, 0 )
    t.pippo()
    g = gigio(2)
    z = zizo("a")

    print ( t, g, z )

    z.__str__()

    sys.exit ( app.exec() )



