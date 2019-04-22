import sys

from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QMainWindow,QPlainTextEdit
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

        self.setMinimumSize(QSize(440,240))
        self.setWindowTitle( "test" )

        self.e = QPlainTextEdit(self)
        self.e.insertPlainText("This is a test")
        self.e.move ( 10, 10 )
        self.e.resize ( 400, 200 )

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



