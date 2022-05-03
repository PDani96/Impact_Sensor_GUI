import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
#from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   widget = QWidget()

   p = widget.palette()
   p.setColor(widget.backgroundRole(), QtCore.Qt.black)
   widget.setPalette(p)

   logo = QLabel(widget)
   pixmap = QPixmap('Unaffiliated+Athletics-Red.jpg')
   logo.setPixmap(pixmap)

   gForce = QLabel(widget)
   gForce.setFont(QFont('Impact', 60))
   gForce.setText("G-Force : ")
   gForce.move(110,85)

   widget.setGeometry(50,50,1920,1080)
   widget.showFullScreen()
   widget.setWindowTitle("Impact Sensor")
   widget.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()