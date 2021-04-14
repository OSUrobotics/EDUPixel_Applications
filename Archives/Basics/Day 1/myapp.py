# #https://www.learnpyqt.com/tutorials/signals-slots-events/ 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
# These are the basic three libraries that needs to be imported to use PyQt5

import sys
# Import system so that the GUI can take user import in the future such as command line arguments

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        # *Args = arguments, **kwargs = keywords arguments
        super(MainWindow, self).__init__(*args, **kwargs)
        # Calling the function just for the init function in this class

        self.windowTitleChanged.connect(self.onWindowTitleChange)


        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())


        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))


        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))



        # Setting up the title of the GUI
        self.setWindowTitle("Wow")

        # Setting up a label
        label = QLabel("This is the first label")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

    def onWindowTitleChange(self, s):
        print(s)
    
    def my_custom_fn(self, a = "Hello", b = 5):
        print(a,b)

    def contextMenuEvent(self, event):
        print("Context menu event!")
        # super(MainWindow, self).contextMenuEvent(event)





app = QApplication(sys.argv) # This will set up the application

window = MainWindow() # This will run the class to set up the GUI with its variables
window.show() # This will show the GUI


app.exec_()
