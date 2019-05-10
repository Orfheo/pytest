import sys

import testrc

from PyQt5.QtGui import QIcon
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QMainWindow,QPlainTextEdit,QComboBox,QAction
from PyQt5.QtCore import QSize

from zaza.gigio import gigio
from zaza.papero import zizo

from myexcp.WException import WException

class Test :
    """
        A test class
    """
    def __init__ ( self, x=0, y=0) :
        """
        Init method, with default values

        :param x: x coordinate
        :param y: y coordinate
        :rtype: None
        """
        self.x = 0
        self.y = 0

    def __str__(self):
        """
        String representation
        :return: string
        """
        return "(%s,%s)" % (self.x,self.y)

    def pippo (self):
        """
        A test method, without arguments

        :return: Noe
        """
        self.x = 1
        self.y = 2


class MyQPlainTextEdit(QPlainTextEdit):
    def __init__(self,parent):
        super().__init__(parent)

    def goTop(self):
        self.verticalScrollBar().setValue(self.verticalScrollBar().maximum())

    def goBottom(self):
        self.verticalScrollBar().setValue(0)

class Window(QMainWindow):
    """
    TODO: test it
    """
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(440, 240))
        self.setWindowTitle("test")

        self.addText(self)
        #self.addCombo(self)

        self.copy = QAction ( QIcon(':/images/copy.png'), "Copy", self, triggered=self.actionCopy )
        self.new  = QAction ( QIcon(':/images/new.png'),  "New", self,  triggered=self.actionNew  )

        self.t = self.addToolBar("Test")

        self.t.addAction( self.copy )
        self.t.addAction( self.new )

        #raise WException ( "test" )


    def addText(self, parent):
        self.e = MyQPlainTextEdit(self)
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


    def actionCopy(self):
        self.e.insertPlainText("action got Copy\n")
        self.e.goTop()

    def actionNew(self):
        self.e.insertPlainText("action got New\n")
        self.e.goBottom()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    try:
        w = Window()
    except WException as e:
        e.print()
        sys.exit()

    w.show()
    t = Test ( 0, 0 )
    t.pippo()
    g = gigio(2)
    """
        comment test
    """
    z = zizo("a")

    print ( t, g, z )

    z.__str__()



    sys.exit ( app.exec() )



