# Prototype window to be used for HAB team's communications platform

import sys
from PySide import QtGui

class CommWindow (QtGui.QMainWindow):

    def __init__(self):
        super (CommWindow, self).__init__()
        self.initUI()

    def initUI(self):               
        # Set window properties
        self.setGeometry(300, 300, 650, 500) # setGeometry(x,y,width,height)
        self.setWindowTitle('HAB Communications')

        # Define menu bar actions
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        # Add a menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # Create the tool bar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # Show the status bar
        self.statusBar().showMessage('Ready')

        # Display the window
        self.show()



# Main Loop
app = QtGui.QApplication(sys.argv)
winMain = CommWindow()

sys.exit(app.exec_())
