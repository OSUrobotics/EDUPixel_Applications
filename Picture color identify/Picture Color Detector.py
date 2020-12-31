###########################################################################################################################
## Author: Kenneth Kang                                                                                                  ##
## Purpose: This will identify the color of the image by the user color range for each Red, Green, and Blue value. This  ##
## software/GUI was created to aware the individuals to know the limitation of computer vision that computer vision is   ##
## not perfect to be depended. In other words, it is an education software for the users to play around with it.         ##
##                                                                                                                       ##
## Dependencies: PyQt5, Numpy, cv2, OS                                                                                   ##
##                                                                                                                       ##
## Other software Usage: Designer.exe for PyQt5(That can be found in .ui file)                                           ##
###########################################################################################################################


# https://realpython.com/documenting-python-code/ Need to Document the entire code when I complete it

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Global Variables
        self.redMin = 0
        self.redMax = 255
        self.greenMin = 0
        self.greenMax = 255
        self.blueMin = 0
        self.blueMax = 255
        self.filePath = "No_Path"
        
        # GUI Setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1152, 835)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(820, 0, 20, 821))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")

        self.colorDetectSwitch = QtWidgets.QCheckBox(self.centralwidget)
        self.colorDetectSwitch.setGeometry(QtCore.QRect(380, 770, 61, 21))
        self.colorDetectSwitch.setObjectName("colorDetectSwitch")

        self.imageLbl = QtWidgets.QLabel(self.centralwidget)
        self.imageLbl.setGeometry(QtCore.QRect(10, 10, 801, 751))
        self.imageLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imageLbl.setText("")
        self.imageLbl.setObjectName("imageLbl")

        self.imageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.imageBtn.setGeometry(QtCore.QRect(170, 770, 81, 31))
        self.imageBtn.setObjectName("imageBtn")

        self.redMaxSlider = QtWidgets.QSlider(self.centralwidget)
        self.redMaxSlider.setGeometry(QtCore.QRect(840, 200, 211, 22))
        self.redMaxSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.redMaxSlider.setMaximum(255)
        self.redMaxSlider.setSliderPosition(255)
        self.redMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redMaxSlider.setObjectName("redMaxSlider")

        self.redMaxBtn = QtWidgets.QPushButton(self.centralwidget)
        self.redMaxBtn.setGeometry(QtCore.QRect(910, 230, 75, 23))
        self.redMaxBtn.setObjectName("redMaxBtn")

        self.redMinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.redMinBtn.setGeometry(QtCore.QRect(910, 110, 75, 23))
        self.redMinBtn.setObjectName("redMinBtn")

        self.redMinText = QtWidgets.QLabel(self.centralwidget)
        self.redMinText.setGeometry(QtCore.QRect(910, 50, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.redMinText.setFont(font)
        self.redMinText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redMinText.setAlignment(QtCore.Qt.AlignCenter)
        self.redMinText.setObjectName("redMinText")

        self.redMinSlider = QtWidgets.QSlider(self.centralwidget)
        self.redMinSlider.setGeometry(QtCore.QRect(840, 80, 211, 22))
        self.redMinSlider.setMaximum(255)
        self.redMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redMinSlider.setObjectName("redMinSlider")

        self.greenMaxSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenMaxSlider.setGeometry(QtCore.QRect(840, 462, 211, 20))
        self.greenMaxSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.greenMaxSlider.setMaximum(255)
        self.greenMaxSlider.setSliderPosition(255)
        self.greenMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenMaxSlider.setObjectName("greenMaxSlider")

        self.greenMaxBtn = QtWidgets.QPushButton(self.centralwidget)
        self.greenMaxBtn.setGeometry(QtCore.QRect(910, 490, 75, 23))
        self.greenMaxBtn.setObjectName("greenMaxBtn")

        self.blueMaxSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueMaxSlider.setGeometry(QtCore.QRect(840, 720, 211, 22))
        self.blueMaxSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blueMaxSlider.setMaximum(255)
        self.blueMaxSlider.setSliderPosition(255)
        self.blueMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueMaxSlider.setObjectName("blueMaxSlider")

        self.blueMaxBtn = QtWidgets.QPushButton(self.centralwidget)
        self.blueMaxBtn.setGeometry(QtCore.QRect(910, 750, 75, 23))
        self.blueMaxBtn.setObjectName("blueMaxBtn")

        self.greenMinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.greenMinBtn.setGeometry(QtCore.QRect(910, 360, 75, 23))
        self.greenMinBtn.setObjectName("greenMinBtn")

        self.greenMinSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenMinSlider.setGeometry(QtCore.QRect(840, 330, 211, 22))
        self.greenMinSlider.setMaximum(255)
        self.greenMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenMinSlider.setObjectName("greenMinSlider")

        self.blueMinBtn = QtWidgets.QPushButton(self.centralwidget)
        self.blueMinBtn.setGeometry(QtCore.QRect(910, 620, 75, 23))
        self.blueMinBtn.setObjectName("blueMinBtn")

        self.blueMinSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueMinSlider.setGeometry(QtCore.QRect(840, 590, 211, 22))
        self.blueMinSlider.setMaximum(255)
        self.blueMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueMinSlider.setObjectName("blueMinSlider")

        self.redMaxText = QtWidgets.QLabel(self.centralwidget)
        self.redMaxText.setGeometry(QtCore.QRect(910, 170, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.redMaxText.setFont(font)
        self.redMaxText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redMaxText.setAlignment(QtCore.Qt.AlignCenter)
        self.redMaxText.setObjectName("redMaxText")

        self.greenMinText = QtWidgets.QLabel(self.centralwidget)
        self.greenMinText.setGeometry(QtCore.QRect(910, 300, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.greenMinText.setFont(font)
        self.greenMinText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenMinText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenMinText.setObjectName("greenMinText")

        self.greenMaxText = QtWidgets.QLabel(self.centralwidget)
        self.greenMaxText.setGeometry(QtCore.QRect(910, 430, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.greenMaxText.setFont(font)
        self.greenMaxText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenMaxText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenMaxText.setObjectName("greenMaxText")

        self.blueMinText = QtWidgets.QLabel(self.centralwidget)
        self.blueMinText.setGeometry(QtCore.QRect(910, 550, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.blueMinText.setFont(font)
        self.blueMinText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueMinText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueMinText.setObjectName("blueMinText")

        self.blueMaxText = QtWidgets.QLabel(self.centralwidget)
        self.blueMaxText.setGeometry(QtCore.QRect(910, 680, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.blueMaxText.setFont(font)
        self.blueMaxText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueMaxText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueMaxText.setObjectName("blueMaxText")

        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(580, 770, 81, 31))
        self.resetBtn.setObjectName("resetBtn")

        self.redMinValue = QtWidgets.QLabel(self.centralwidget)
        self.redMinValue.setGeometry(QtCore.QRect(1080, 80, 61, 31))
        self.redMinValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redMinValue.setNum(self.redMin)
        self.redMinValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redMinValue.setObjectName("redMinValue")

        self.redMaxValue = QtWidgets.QLabel(self.centralwidget)
        self.redMaxValue.setGeometry(QtCore.QRect(1080, 190, 61, 31))
        self.redMaxValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redMaxValue.setNum(self.redMax)
        self.redMaxValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redMaxValue.setObjectName("redMaxValue")

        self.greenMinValue = QtWidgets.QLabel(self.centralwidget)
        self.greenMinValue.setGeometry(QtCore.QRect(1080, 320, 61, 31))
        self.greenMinValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenMinValue.setNum(self.greenMin)
        self.greenMinValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenMinValue.setObjectName("greenMinValue")

        self.greenMaxValue = QtWidgets.QLabel(self.centralwidget)
        self.greenMaxValue.setGeometry(QtCore.QRect(1080, 460, 61, 31))
        self.greenMaxValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenMaxValue.setNum(self.greenMax)
        self.greenMaxValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenMaxValue.setObjectName("greenMaxValue")

        self.blueMinValue = QtWidgets.QLabel(self.centralwidget)
        self.blueMinValue.setGeometry(QtCore.QRect(1080, 580, 61, 31))
        self.blueMinValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueMinValue.setNum(self.blueMin)
        self.blueMinValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueMinValue.setObjectName("blueMinValue")

        self.blueMaxValue = QtWidgets.QLabel(self.centralwidget)
        self.blueMaxValue.setGeometry(QtCore.QRect(1080, 710, 61, 31))
        self.blueMaxValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueMaxValue.setNum(self.blueMax)
        self.blueMaxValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueMaxValue.setObjectName("blueMaxValue")

        self.settingText = QtWidgets.QLabel(self.centralwidget)
        self.settingText.setGeometry(QtCore.QRect(920, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.settingText.setFont(font)
        self.settingText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.settingText.setAlignment(QtCore.Qt.AlignCenter)
        self.settingText.setObjectName("settingText")

        self.creatorText = QtWidgets.QLabel(self.centralwidget)
        self.creatorText.setGeometry(QtCore.QRect(10, 800, 91, 16))
        self.creatorText.setObjectName("creatorText")

        self.borderLineWithRG = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithRG.setGeometry(QtCore.QRect(830, 270, 321, 16))
        self.borderLineWithRG.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithRG.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithRG.setObjectName("borderLineWithRG")

        self.borderLineWithGB = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithGB.setGeometry(QtCore.QRect(830, 520, 321, 16))
        self.borderLineWithGB.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithGB.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithGB.setObjectName("borderLineWithGB")

        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 1152, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        # Functions with Btn Connection
        self.imageBtn.clicked.connect(self.setImage)
        self.redMinBtn.clicked.connect(self.redMinUpdate)
        self.redMaxBtn.clicked.connect(self.redMaxUpdate)
        self.greenMinBtn.clicked.connect(self.greenMinUpdate)
        self.greenMaxBtn.clicked.connect(self.greenMaxUpdate)
        self.blueMinBtn.clicked.connect(self.blueMinUpdate)
        self.blueMaxBtn.clicked.connect(self.blueMaxUpdate)
        self.resetBtn.clicked.connect(self.resetToInitState)

        # Functions with CheckBox
        self.colorDetectSwitch.stateChanged.connect(self.checkBoxSwitch)

        # Functions with Slider
        self.redMinSlider.valueChanged.connect(self.updateRedMinValues)
        self.redMaxSlider.valueChanged.connect(self.updateRedMaxValues)
        self.greenMinSlider.valueChanged.connect(self.updateGreenMinValues)
        self.greenMaxSlider.valueChanged.connect(self.updateGreenMaxValues)
        self.blueMinSlider.valueChanged.connect(self.updateBlueMinValues)
        self.blueMaxSlider.valueChanged.connect(self.updateBlueMaxValues)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Color Detector"))
        self.colorDetectSwitch.setText(_translate("MainWindow", "Execute"))
        self.imageBtn.setText(_translate("MainWindow", "Select Image"))
        self.redMaxBtn.setText(_translate("MainWindow", "Confirm"))
        self.redMinBtn.setText(_translate("MainWindow", "Confirm"))
        self.redMinText.setText(_translate("MainWindow", "Red Min"))
        self.greenMaxBtn.setText(_translate("MainWindow", "Confirm"))
        self.blueMaxBtn.setText(_translate("MainWindow", "Confirm"))
        self.greenMinBtn.setText(_translate("MainWindow", "Confirm"))
        self.blueMinBtn.setText(_translate("MainWindow", "Confirm"))
        self.redMaxText.setText(_translate("MainWindow", "Red Max"))
        self.greenMinText.setText(_translate("MainWindow", "Green Min"))
        self.greenMaxText.setText(_translate("MainWindow", "Green Max"))
        self.blueMinText.setText(_translate("MainWindow", "Blue Min"))
        self.blueMaxText.setText(_translate("MainWindow", "Blue Max"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.settingText.setText(_translate("MainWindow", "Settings"))
        self.creatorText.setText(_translate("MainWindow", "By Kenneth Kang"))

###########################################################################################################################

    def setImage(self):
        """
        This function will ask the user to select an image to detect color. 
        Then it will set as the default image
        """
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        self.filePath = fileName
        if (fileName): # If the user gives a file
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageLbl.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center

###########################################################################################################################

    def redMinUpdate(self):
        """
        This function will set the lower limit to detect color.
        """        
        self.redMin = self.redMinSlider.sliderPosition()
        
    def redMaxUpdate(self):
        """
        This function will set the upper limit to detect color for red.
        """
        self.redMax = self.redMaxSlider.sliderPosition()

    def updateRedMinValues(self):
        """
        This function will update the number while the user moves the Red Min Slider.
        """
        self.redMinValue.setNum(self.redMinSlider.sliderPosition())

    def updateRedMaxValues(self):
        """
        This function will update the number while the user moves the Red Max Slider.
        """
        self.redMaxValue.setNum(self.redMaxSlider.sliderPosition())

###########################################################################################################################

    def greenMinUpdate(self):
        """
        This function will set the lower limit to detect color for green.
        """        
        self.greenMin = self.greenMinSlider.sliderPosition()
        
    def greenMaxUpdate(self):
        """
        This function will set the upper limit to detect color for green.
        """
        self.greenMax = self.greenMaxSlider.sliderPosition()

    def updateGreenMinValues(self):
        """
        This function will update the number while the user moves the Green Min Slider.
        """
        self.greenMinValue.setNum(self.greenMinSlider.sliderPosition())

    def updateGreenMaxValues(self):
        """
        This function will update the number while the user moves the Green Max Slider.
        """
        self.greenMaxValue.setNum(self.greenMaxSlider.sliderPosition())

###########################################################################################################################

    def blueMinUpdate(self):
        """
        This function will set the lower limit to detect color for blue.
        """        
        self.blueMin = self.blueMinSlider.sliderPosition()
        
    def blueMaxUpdate(self):
        """
        This function will set the upper limit to detect color for blue.
        """
        self.blueMax = self.blueMaxSlider.sliderPosition()

    def updateBlueMinValues(self):
        """
        This function will update the number while the user moves the Blue Min Slider.
        """
        self.blueMinValue.setNum(self.blueMinSlider.sliderPosition())

    def updateBlueMaxValues(self):
        """
        This function will update the number while the user moves the Blue Max Slider.
        """
        self.blueMaxValue.setNum(self.blueMaxSlider.sliderPosition())

###########################################################################################################################

    def checkBoxSwitch(self):
        """
        This function is the pre function of filtering out the color that is not in range.
        
        First, it will check if the user select an image. If there is no image, it will return an error.
        Also, it will check if the user select the appropriate color range: if Min value is higher than Max value, that will throw an error.
        Once those two are checked, it will run the filtering out function.
        
        If the user uncheck the checkbox, it will return its default image. 
        """
        if (self.filePath == "No_Path") and (self.colorDetectSwitch.isChecked() == True):
            self.error1()
            self.colorDetectSwitch.setCheckState(0)

        elif ((self.redMin > self.redMax) or (self.blueMin > self.blueMax) or (self.greenMin > self.greenMax)) and (self.colorDetectSwitch.isChecked() == True):
            self.error2()
            self.colorDetectSwitch.setCheckState(0)

        elif (self.colorDetectSwitch.isChecked()):
            self.color_detect()

        else:
            pixmap = QtGui.QPixmap(self.filePath) # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
            self.imageLbl.setPixmap(pixmap) # Set the pixmap onto the label
            self.imageLbl.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center

###########################################################################################################################

    def error1(self):
        """
        This function is the error message pop up if the user checked the Execute box yet select no image.
        """
        errorMessage1 = QtWidgets.QMessageBox()
        errorMessage1.setWindowTitle("Error")
        errorMessage1.setText("Please Select an Image File!")
        errorMessage1.setIcon(QtWidgets.QMessageBox.Critical)
        x = errorMessage1.exec_()

    def error2(self):
        """
        This function is the error message pop up if the user have invalid color range. 
        """
        errorMessage2 = QtWidgets.QMessageBox()
        errorMessage2.setWindowTitle("Error")
        errorMessage2.setText("One or more has Invalid Color Range!")
        errorMessage2.setIcon(QtWidgets.QMessageBox.Critical)
        x = errorMessage2.exec_()

###########################################################################################################################

    def color_detect(self):
        """
        This function will do the filering out process of if the color is identify by the user color range selection.
        """
        # Adding a filter on the image just to detect red
        image = cv2.imread(self.filePath)
        self.redLower = np.array([self.blueMin, self.greenMin, self.redMin], dtype = "uint8")
        self.redUpper = np.array([self.blueMax, self.greenMax, self.redMax], dtype = "uint8")
        mask = cv2.inRange(image, self.redLower, self.redUpper)
        output = cv2.bitwise_and(image, image, mask = mask)
            
        # Create a new image so that the GUI will replace the picture
        cv2.imwrite("Red_Detection.png", output)
        fileName = "Red_Detection.png"
            
        # Same as setImage function
        pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
        pixmap = pixmap.scaled(self.imageLbl.width(), self.imageLbl.height(), QtCore.Qt.KeepAspectRatio) # Scale pixmap
        self.imageLbl.setPixmap(pixmap) # Set the pixmap onto the label
        self.imageLbl.setAlignment(QtCore.Qt.AlignCenter) # Align the label to center
            
        # Remove the file that has the filter
        os.remove(fileName)

###########################################################################################################################

    def resetToInitState(self):
        """
        This function will reset to its init values like when the GUI just lanuched as fresh.
        """
        self.redMin = 0
        self.redMax = 255
        self.greenMin = 0
        self.greenMax = 255
        self.blueMin = 0
        self.blueMax = 255
        self.filePath = "No_Path"
        self.imageLbl.clear()
        self.redMaxSlider.setSliderPosition(255)
        self.redMinSlider.setSliderPosition(0)
        self.greenMaxSlider.setSliderPosition(255)
        self.greenMinSlider.setSliderPosition(0)
        self.blueMaxSlider.setSliderPosition(255)
        self.blueMinSlider.setSliderPosition(0)
        self.colorDetectSwitch.setCheckState(0)
        self.redMinValue.setNum(self.redMin)
        self.redMaxValue.setNum(self.redMax)
        self.greenMinValue.setNum(self.greenMin)
        self.greenMaxValue.setNum(self.greenMax)
        self.blueMinValue.setNum(self.blueMin)
        self.blueMaxValue.setNum(self.blueMax)

###########################################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
