import sys
import traceback
import subprocess

from myexcp.WException import WException,WExceptionWidget

from PyQt5 import Qt

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication,QPushButton,QLineEdit,QLabel
from PySide2.QtCore import QFile,QObject
class Form(QObject):

    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        self.btn = self.getChild ( QPushButton, 'ButtonClickMe' )
        self.btn.clicked.connect(self.ok_handler)

        self.line = self.getChild(QLineEdit,'lineEditName')

        self.label = self.getChild(QLabel,'labelResponse' )

        self.window.show()


    def getChild(self, cls, name):
        obj = self.window.findChild ( cls, name )
        if not isinstance ( obj, cls ):
           raise WExceptionWidget(name)
        return obj

    def ok_handler(self):
        self.label.setText("Hello "
        +self.line.text())
        #
        # brief example about command pipe from python
        out = subprocess.Popen (['bshow', '-a'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

        for line in out.stdout:
            list=line.decode().rstrip("\n").split(' ')
            storage=list[0].split(':')[1].rstrip("_")
            nvol=list[3]
            space=list[5]
            print ( storage, nvol, space )

if __name__ == "__main__":


    app = QApplication(sys.argv)
    try:
        form = Form('ui/form.ui')
    except WException as e:
      e.print()
      sys.exit()

    sys.exit(app.exec_())