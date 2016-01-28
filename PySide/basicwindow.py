import sys
from PySide import QtGui

app = QtGui.QApplication(sys.argv)

wid = QtGui.QWidget()
wid.resize(600, 500)
wid.setWindowTitle('Basic Window')
wid.show()

sys.exit(app.exec_())
