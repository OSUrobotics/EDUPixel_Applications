#TODO: Need to update the blub


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """
    This is the parent class of the two child classes for GUI
    In other words, this is the main GUI for this program
    """
    def setupUi(self, MainWindow):
        """
        Initializes the child GUI that only have a QLabel from PyQt5
        At the same time, it also link other functions to each object

        Connected Functions:
            Format: Description
                Object Name: Function

            Timer: Set a timer for every 0.01 second to trigger updateValue function

            Slider: By changing the position of the slider will trigger certain function
                redSlider: colorChangeRed function
                greenSlider: colorChangeGreen function
                blueSlider: colorChangeBlue function
        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 180)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.colorDisplay = QtWidgets.QLabel(self.centralwidget)
        self.colorDisplay.setGeometry(QtCore.QRect(430, 60, 91, 61))
        self.colorDisplay.setFrameShape(QtWidgets.QFrame.Box)
        self.colorDisplay.setText("")
        self.colorDisplay.setFont(font)
        self.colorDisplay.setObjectName("colorDisplay")

        self.redText = QtWidgets.QLabel(self.centralwidget)
        self.redText.setGeometry(QtCore.QRect(10, 20, 61, 21))
        self.redText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.redText.setAlignment(QtCore.Qt.AlignCenter)
        self.redText.setFont(font)
        self.redText.setObjectName("redText")

        self.greenText = QtWidgets.QLabel(self.centralwidget)
        self.greenText.setGeometry(QtCore.QRect(10, 80, 61, 21))
        self.greenText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.greenText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenText.setFont(font)
        self.greenText.setObjectName("greenText")

        self.blueText = QtWidgets.QLabel(self.centralwidget)
        self.blueText.setGeometry(QtCore.QRect(10, 140, 61, 21))
        self.blueText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueText.setFont(font)
        self.blueText.setObjectName("blueText")

        self.redSlider = QtWidgets.QSlider(self.centralwidget)
        self.redSlider.setGeometry(QtCore.QRect(70, 20, 291, 22))
        self.redSlider.setMaximum(255)
        self.redSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redSlider.setObjectName("redSlider")

        self.greenSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenSlider.setGeometry(QtCore.QRect(70, 80, 291, 22))
        self.greenSlider.setMaximum(255)
        self.greenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenSlider.setObjectName("greenSlider")

        self.blueSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueSlider.setGeometry(QtCore.QRect(70, 140, 291, 22))
        self.blueSlider.setMaximum(255)
        self.blueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueSlider.setObjectName("blueSlider")

        self.redValueText = QtWidgets.QLabel(self.centralwidget)
        self.redValueText.setGeometry(QtCore.QRect(370, 20, 47, 21))
        self.redValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.redValueText.setNum(0)
        self.redValueText.setFont(font)
        self.redValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.redValueText.setObjectName("redValueText")

        self.greenValueText = QtWidgets.QLabel(self.centralwidget)
        self.greenValueText.setGeometry(QtCore.QRect(370, 80, 47, 21))
        self.greenValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.greenValueText.setNum(0)
        self.greenValueText.setFont(font)
        self.greenValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenValueText.setObjectName("greenValueText")

        self.blueValueText = QtWidgets.QLabel(self.centralwidget)
        self.blueValueText.setGeometry(QtCore.QRect(370, 143, 47, 20))
        self.blueValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.blueValueText.setNum(0)
        self.blueValueText.setFont(font)
        self.blueValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueValueText.setObjectName("blueValueText")

        MainWindow.setCentralWidget(self.centralwidget)

        self.timer = QtCore.QTimer()

        # Global Variables
        self.redValueInput = 0
        self.greenValueInput = 0
        self.blueValueInput = 0

        # Functions with Sliders
        self.redSlider.valueChanged[int].connect(self.colorChangeRed)
        self.greenSlider.valueChanged[int].connect(self.colorChangeGreen)
        self.blueSlider.valueChanged[int].connect(self.colorChangeBlue)

        # Timer
        self.timer.timeout.connect(self.update)
        self.timer.start(10)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Replaces the name of the object when it displayes to the user

        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.redText.setText(_translate("MainWindow", "Red"))
        self.greenText.setText(_translate("MainWindow", "Green"))
        self.blueText.setText(_translate("MainWindow", "Blue"))

    def update(self):
        """
        This function will be (almost) continuously running when the GUI is up.
        When the user change any values, it will automatically update text value or functions that uses those values.
        """
        hexColor = '#'+'%02x%02x%02x' % (self.redValueInput, self.greenValueInput, self.blueValueInput)
        self.colorDisplay.setStyleSheet(f'background-color: {hexColor}')

    def colorChangeRed(self, value):
        """
        Change the value of Red when the user move the Red Slider.
        
        Args:
            Value: The red slider current location.
        """
        self.redValueInput = value
        self.redValueText.setNum(value)

    def colorChangeGreen(self, value):
        """
        Change the value of Green when the user move the Green Slider.
        
        Args:
            Value: The green slider current location.
        """
        self.greenValueInput = value
        self.greenValueText.setNum(value)
        

    def colorChangeBlue(self, value):
        """
        Change the value of Blue when the user move the Blue Slider.
        
        Args:
            Value: The blue slider current location.
        """
        self.blueValueInput = value
        self.blueValueText.setNum(value)

# Basic functions and statements to call the Main GUI to run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
