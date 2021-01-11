from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
from sklearn.cluster import KMeans

# Global Variables Between Three Classes
filePath = "No_Path"
xValue = 0
yValue = 0
redAverage = 128
redRange = 0
greenAverage = 128
greenRange = 0
blueAverage = 128
blueRange = 0
redValue = 0
greenValue = 0 
blueValue = 0
width = 0
height = 0
failed = False
num_clusters = 1
RGB = []

class Image(object):
    """
    This class is the child GUI for displaying the image from user selection
    """
    def setupUi(self, MainWindow, width, height):
        """
        Initializes the child GUI that only have a QLabel from PyQt5
        At the same time, it also link other functions to each object

        Connected Functions:
            MouseEvent: When the user select an position on the Image Label, it will trigger captureIt function 

        Args:
            MainWindow: The whole GUI that contains the Widget
            width: The width of the GUI
            height: The height of the GUI
        """
        MainWindow.setObjectName("Image")
        MainWindow.resize(width, height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imgLbl = QtWidgets.QLabel(self.centralwidget)
        self.imgLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLbl.setText("")
        self.imgLbl.setCursor(QtCore.Qt.CrossCursor)
        self.imgLbl.setObjectName("imgLbl")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Functions
        self.imgLbl.mousePressEvent = self.captureIt


    def retranslateUi(self, MainWindow):
        """
        Replaces the name of the object when it displayes to the user

        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image"))

    def captureIt(self, event):
        """
        Get all the information of the positions and color RGB values when the user

        Args:
            event: It registers the event information of the user selection when the left mouse is clicked

        Returns:
            It will replace the global variables of xValue, yValue, redValue, greenValue, and blueValue to be used in other classes
        """
        global xValue, yValue, redValue, greenValue, blueValue, filePath
        xValue = event.pos().x()
        yValue = event.pos().y()
        qImg = QtGui.QImage(filePath)
        c = qImg.pixel(xValue,yValue)
        colors = QtGui.QColor(c).getRgb()
        redValue = colors[0]
        greenValue = colors[1]
        blueValue = colors[2] 

class AnalyzeColor(object):
    """
    This class is another child GUI for displaying the most common color from user selection of image and numbers
    """
    def setupUi(self, MainWindow, width):
        """
        Initializes the child GUI that only have a QLabel from PyQt5

        Args:
            MainWindow: The whole GUI that contains the Widget
            width: The width of the GUI
        """
        MainWindow.setObjectName("Analyze")
        MainWindow.resize(width, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.anzLbl = QtWidgets.QLabel(self.centralwidget)
        self.anzLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.anzLbl.setText("")
        self.anzLbl.setCursor(QtCore.Qt.CrossCursor)
        self.anzLbl.setObjectName("anzLbl")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Function
        self.anzLbl.mousePressEvent = self.captureIt

    def captureIt(self, event):
        global redAverage, greenAverage, blueAverage
        print(1)
        qImg = QtGui.QImage("Common_Colors.png")
        print(1)
        c = qImg.pixel(event.pos().x(), event.pos().y())
        print(1)
        colors = QtGui.QColor(c).getRgb()
        redAverage = colors[0]
        greenAverage = colors[1]
        blueAverage = colors[2]


    def retranslateUi(self, MainWindow):
        """
        Replaces the name of the object when it displayes to the user

        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f'Top {num_clusters} Most Common Colors with Color Code'))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.blueSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueSlider.setGeometry(QtCore.QRect(580, 270, 510, 22))
        self.blueSlider.setMaximum(255)
        self.blueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueSlider.setObjectName("blueSlider")

        self.analyzeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.analyzeBtn.setGeometry(QtCore.QRect(700, 640, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.analyzeBtn.setFont(font)
        self.analyzeBtn.setObjectName("analyzeBtn")

        self.yText = QtWidgets.QLabel(self.centralwidget)
        self.yText.setGeometry(QtCore.QRect(720, 320, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yText.setFont(font)
        self.yText.setAlignment(QtCore.Qt.AlignCenter)
        self.yText.setObjectName("yText")

        self.imgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.imgBtn.setGeometry(QtCore.QRect(550, 420, 280, 90))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.imgBtn.setFont(font)
        self.imgBtn.setObjectName("imgBtn")

        self.greenAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.greenAverageValue.setGeometry(QtCore.QRect(410, 350, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenAverageValue.setFont(font)
        self.greenAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenAverageValue.setText("")
        self.greenAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenAverageValue.setObjectName("greenAverageValue")

        self.greenSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenSlider.setGeometry(QtCore.QRect(580, 210, 510, 22))
        self.greenSlider.setMaximum(255)
        self.greenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenSlider.setObjectName("greenSlider")

        self.colorChangeText = QtWidgets.QLabel(self.centralwidget)
        self.colorChangeText.setGeometry(QtCore.QRect(760, 70, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.colorChangeText.setFont(font)
        self.colorChangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.colorChangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorChangeText.setObjectName("colorChangeText")

        self.redAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.redAverageValue.setGeometry(QtCore.QRect(410, 140, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redAverageValue.setFont(font)
        self.redAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redAverageValue.setText("")
        self.redAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redAverageValue.setObjectName("redAverageValue")

        self.greenText = QtWidgets.QLabel(self.centralwidget)
        self.greenText.setGeometry(QtCore.QRect(830, 190, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenText.setFont(font)
        self.greenText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenText.setObjectName("greenText")

        self.redText = QtWidgets.QLabel(self.centralwidget)
        self.redText.setGeometry(QtCore.QRect(830, 120, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redText.setFont(font)
        self.redText.setAlignment(QtCore.Qt.AlignCenter)
        self.redText.setObjectName("redText")

        self.blueAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueAverageSlider.setGeometry(QtCore.QRect(40, 570, 351, 22))
        self.blueAverageSlider.setMaximum(255)
        self.blueAverageSlider.setProperty("value", 128)
        self.blueAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueAverageSlider.setObjectName("blueAverageSlider")

        self.redAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.redAverageSlider.setGeometry(QtCore.QRect(40, 140, 351, 22))
        self.redAverageSlider.setMaximum(255)
        self.redAverageSlider.setSliderPosition(128)
        self.redAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redAverageSlider.setObjectName("redAverageSlider")

        self.blueAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.blueAverageValue.setGeometry(QtCore.QRect(410, 570, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueAverageValue.setFont(font)
        self.blueAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueAverageValue.setObjectName("blueAverageValue")

        self.xText = QtWidgets.QLabel(self.centralwidget)
        self.xText.setGeometry(QtCore.QRect(610, 320, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xText.setFont(font)
        self.xText.setAlignment(QtCore.Qt.AlignCenter)
        self.xText.setObjectName("xText")

        self.redRangeText = QtWidgets.QLabel(self.centralwidget)
        self.redRangeText.setGeometry(QtCore.QRect(180, 190, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redRangeText.setFont(font)
        self.redRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.redRangeText.setObjectName("redRangeText")

        self.greenValueText = QtWidgets.QLabel(self.centralwidget)
        self.greenValueText.setGeometry(QtCore.QRect(1100, 210, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenValueText.setFont(font)
        self.greenValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.greenValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenValueText.setObjectName("greenValueText")

        self.redRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.redRangeValue.setGeometry(QtCore.QRect(410, 220, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redRangeValue.setFont(font)
        self.redRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redRangeValue.setText("")
        self.redRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redRangeValue.setObjectName("redRangeValue")

        self.blueValueText = QtWidgets.QLabel(self.centralwidget)
        self.blueValueText.setGeometry(QtCore.QRect(1100, 270, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueValueText.setFont(font)
        self.blueValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.blueValueText.setText("")
        self.blueValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueValueText.setObjectName("blueValueText")

        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setGeometry(QtCore.QRect(1040, 690, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.author.setFont(font)
        self.author.setObjectName("author")

        self.colorPreview = QtWidgets.QLabel(self.centralwidget)
        self.colorPreview.setGeometry(QtCore.QRect(870, 340, 130, 50))
        self.colorPreview.setFrameShape(QtWidgets.QFrame.Box)
        self.colorPreview.setText("")
        self.colorPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreview.setObjectName("colorPreview")

        self.greenRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenRangeSlider.setGeometry(QtCore.QRect(40, 432, 351, 20))
        self.greenRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.greenRangeSlider.setMaximum(127)
        self.greenRangeSlider.setProperty("value", 0)
        self.greenRangeSlider.setSliderPosition(0)
        self.greenRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenRangeSlider.setObjectName("greenRangeSlider")

        self.greenAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenAverageSlider.setGeometry(QtCore.QRect(40, 350, 351, 22))
        self.greenAverageSlider.setMaximum(255)
        self.greenAverageSlider.setProperty("value", 128)
        self.greenAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenAverageSlider.setObjectName("greenAverageSlider")

        self.descriptionBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.descriptionBox.setGeometry(QtCore.QRect(870, 420, 311, 261))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.descriptionBox.setFont(font)
        self.descriptionBox.setObjectName("descriptionBox")

        self.xValueText = QtWidgets.QLabel(self.centralwidget)
        self.xValueText.setGeometry(QtCore.QRect(610, 360, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xValueText.setFont(font)
        self.xValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.xValueText.setText("")
        self.xValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.xValueText.setObjectName("xValueText")

        self.questionText = QtWidgets.QLabel(self.centralwidget)
        self.questionText.setGeometry(QtCore.QRect(540, 580, 301, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.questionText.setFont(font)
        self.questionText.setObjectName("questionText")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(490, 60, 20, 651))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")

        self.borderLineWithImg = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithImg.setGeometry(QtCore.QRect(500, 400, 691, 20))
        self.borderLineWithImg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithImg.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithImg.setObjectName("borderLineWithImg")

        self.blueRangeText = QtWidgets.QLabel(self.centralwidget)
        self.blueRangeText.setGeometry(QtCore.QRect(180, 610, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueRangeText.setFont(font)
        self.blueRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueRangeText.setObjectName("blueRangeText")

        self.blueRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueRangeSlider.setGeometry(QtCore.QRect(40, 650, 351, 22))
        self.blueRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blueRangeSlider.setMaximum(127)
        self.blueRangeSlider.setSliderPosition(0)
        self.blueRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueRangeSlider.setObjectName("blueRangeSlider")

        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(530, 650, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.resetBtn.setFont(font)
        self.resetBtn.setObjectName("resetBtn")

        self.greenAverageText = QtWidgets.QLabel(self.centralwidget)
        self.greenAverageText.setGeometry(QtCore.QRect(170, 320, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.greenAverageText.setFont(font)
        self.greenAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenAverageText.setObjectName("greenAverageText")

        self.yValueText = QtWidgets.QLabel(self.centralwidget)
        self.yValueText.setGeometry(QtCore.QRect(720, 360, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yValueText.setFont(font)
        self.yValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.yValueText.setText("")
        self.yValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.yValueText.setObjectName("yValueText")

        self.blueText = QtWidgets.QLabel(self.centralwidget)
        self.blueText.setGeometry(QtCore.QRect(830, 250, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueText.setFont(font)
        self.blueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueText.setObjectName("blueText")

        self.changeColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.changeColorBtn.setGeometry(QtCore.QRect(1020, 350, 130, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.changeColorBtn.setFont(font)
        self.changeColorBtn.setObjectName("changeColorBtn")

        self.colorPreviewText = QtWidgets.QLabel(self.centralwidget)
        self.colorPreviewText.setGeometry(QtCore.QRect(870, 310, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.colorPreviewText.setFont(font)
        self.colorPreviewText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreviewText.setObjectName("colorPreviewText")

        self.blueRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.blueRangeValue.setGeometry(QtCore.QRect(410, 650, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueRangeValue.setFont(font)
        self.blueRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueRangeValue.setText("")
        self.blueRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueRangeValue.setObjectName("blueRangeValue")

        self.greenRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.greenRangeValue.setGeometry(QtCore.QRect(410, 430, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenRangeValue.setFont(font)
        self.greenRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenRangeValue.setText("")
        self.greenRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenRangeValue.setObjectName("greenRangeValue")

        self.redValueText = QtWidgets.QLabel(self.centralwidget)
        self.redValueText.setGeometry(QtCore.QRect(1100, 150, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redValueText.setFont(font)
        self.redValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.redValueText.setText("")
        self.redValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.redValueText.setObjectName("redValueText")

        self.redAverageText = QtWidgets.QLabel(self.centralwidget)
        self.redAverageText.setGeometry(QtCore.QRect(180, 110, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redAverageText.setFont(font)
        self.redAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.redAverageText.setObjectName("redAverageText")

        self.blueAverageText = QtWidgets.QLabel(self.centralwidget)
        self.blueAverageText.setGeometry(QtCore.QRect(180, 530, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueAverageText.setFont(font)
        self.blueAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueAverageText.setObjectName("blueAverageText")

        self.colorRangeText = QtWidgets.QLabel(self.centralwidget)
        self.colorRangeText.setGeometry(QtCore.QRect(130, 70, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.colorRangeText.setFont(font)
        self.colorRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.colorRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorRangeText.setObjectName("colorRangeText")

        self.borderLineWithGB = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithGB.setGeometry(QtCore.QRect(-10, 500, 511, 20))
        self.borderLineWithGB.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithGB.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithGB.setObjectName("borderLineWithGB")

        self.executeDetect = QtWidgets.QCheckBox(self.centralwidget)
        self.executeDetect.setGeometry(QtCore.QRect(550, 520, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.executeDetect.setFont(font)
        self.executeDetect.setObjectName("executeDetect")

        self.borderLineWithRG = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithRG.setGeometry(QtCore.QRect(-10, 290, 511, 20))
        self.borderLineWithRG.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithRG.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithRG.setObjectName("borderLineWithRG")

        self.redRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.redRangeSlider.setGeometry(QtCore.QRect(40, 220, 351, 22))
        self.redRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.redRangeSlider.setMaximum(127)
        self.redRangeSlider.setProperty("value", 0)
        self.redRangeSlider.setSliderPosition(0)
        self.redRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redRangeSlider.setObjectName("redRangeSlider")

        self.redSlider = QtWidgets.QSlider(self.centralwidget)
        self.redSlider.setGeometry(QtCore.QRect(580, 150, 510, 22))
        self.redSlider.setMaximum(255)
        self.redSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redSlider.setObjectName("redSlider")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 10, 1141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.greenRangeText = QtWidgets.QLabel(self.centralwidget)
        self.greenRangeText.setGeometry(QtCore.QRect(180, 400, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.greenRangeText.setFont(font)
        self.greenRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenRangeText.setObjectName("greenRangeText")

        self.commonColorSlider = QtWidgets.QSlider(self.centralwidget)
        self.commonColorSlider.setGeometry(QtCore.QRect(570, 610, 160, 22))
        self.commonColorSlider.setMinimum(1)
        self.commonColorSlider.setMaximum(5)
        self.commonColorSlider.setOrientation(QtCore.Qt.Horizontal)
        self.commonColorSlider.setObjectName("commonColorSlider")

        self.commonColorValue = QtWidgets.QLabel(self.centralwidget)
        self.commonColorValue.setGeometry(QtCore.QRect(750, 610, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.commonColorValue.setFont(font)
        self.commonColorValue.setFrameShape(QtWidgets.QFrame.Box)
        self.commonColorValue.setText("")
        self.commonColorValue.setAlignment(QtCore.Qt.AlignCenter)
        self.commonColorValue.setObjectName("commonColorValue")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()


        #Timer
        self.timer.timeout.connect(self.updateValue)
        self.timer.start(10)

        # CheckBox
        self.executeDetect.stateChanged.connect(self.colorDetect)

        # Button
        self.imgBtn.clicked.connect(self.openWindow)
        self.changeColorBtn.clicked.connect(self.changePixel)
        self.resetBtn.clicked.connect(self.resetAll)
        self.analyzeBtn.clicked.connect(self.showCommonColor)

        # Slider
        self.redSlider.valueChanged.connect(self.colorChangeRed)
        self.greenSlider.valueChanged.connect(self.colorChangeGreen)
        self.blueSlider.valueChanged.connect(self.colorChangeBlue)
        self.redAverageSlider.valueChanged.connect(self.redAverageUpdate)
        self.redRangeSlider.valueChanged.connect(self.redRangeUpdate)
        self.greenAverageSlider.valueChanged.connect(self.greenAverageUpdate)
        self.greenRangeSlider.valueChanged.connect(self.greenRangeUpdate)
        self.blueAverageSlider.valueChanged.connect(self.blueAverageUpdate)
        self.blueRangeSlider.valueChanged.connect(self.blueRangeUpdate)
        self.commonColorSlider.valueChanged.connect(self.commonColorUpdate)

    def updateValue(self):
        """
        When the timer is triggered, it will update the global variables along with
        It will update the main GUI of xValue, yValue, redValue, greenValue, blueValue, redAverage, redRange, greenAverage, greenRange, blueAverage, and blueRange
        if the user has made a change
        """
        global xValue, yValue, redValue, greenValue, blueValue, redAverage, redRange, greenAverage, greenRange, blueAverage, blueRange
        
        self.xValueText.setNum(xValue)
        self.yValueText.setNum(yValue)
        self.redValueText.setNum(redValue)
        self.greenValueText.setNum(greenValue)
        self.blueValueText.setNum(blueValue)
        self.redSlider.setSliderPosition(redValue)
        self.greenSlider.setSliderPosition(greenValue)
        self.blueSlider.setSliderPosition(blueValue)
        hexColor = '#'+'%02x%02x%02x' % (redValue, greenValue, blueValue)
        self.colorPreview.setStyleSheet(f'background-color: {hexColor}')

        self.redAverageValue.setNum(redAverage)
        self.redRangeValue.setNum(redRange)
        self.greenAverageValue.setNum(greenAverage)
        self.greenRangeValue.setNum(greenRange)
        self.blueAverageValue.setNum(blueAverage)
        self.blueRangeValue.setNum(blueRange)
        self.redAverageSlider.setSliderPosition(redAverage)
        self.redRangeSlider.setSliderPosition(redRange)
        self.greenAverageSlider.setSliderPosition(greenAverage)
        self.greenRangeSlider.setSliderPosition(greenRange)
        self.blueAverageSlider.setSliderPosition(blueAverage)
        self.blueRangeSlider.setSliderPosition(blueRange)

        self.commonColorSlider.setSliderPosition(num_clusters)
        self.commonColorValue.setNum(num_clusters)

    def redRangeUpdate(self):
        global redRange
        redRange = self.redRangeSlider.sliderPosition()

    def redAverageUpdate(self):
        global redAverage
        redAverage = self.redAverageSlider.sliderPosition()

    def greenRangeUpdate(self):
        global greenRange
        greenRange = self.greenRangeSlider.sliderPosition()

    def greenAverageUpdate(self):
        global greenAverage
        greenAverage = self.greenAverageSlider.sliderPosition()

    def blueRangeUpdate(self):
        global blueRange
        blueRange = self.blueRangeSlider.sliderPosition()

    def blueAverageUpdate(self):
        global blueAverage
        blueAverage = self.blueAverageSlider.sliderPosition()

    def commonColorUpdate(self):
        global num_clusters
        num_clusters = self.commonColorSlider.sliderPosition()

    def colorChangeRed(self):
        global redValue
        redValue = self.redSlider.sliderPosition()

    def colorChangeGreen(self):
        global greenValue
        greenValue = self.greenSlider.sliderPosition()

    def colorChangeBlue(self):
        global blueValue
        blueValue = self.blueSlider.sliderPosition()

    def openWindow(self):
        """
        Open a file selection screen for only Image file type and show the image once the user has selected
        This image will be display from the child GUI of the Image Class
        It will replace the global variables width, height, and filePath as the following
            width: The width of the Image will be used for setting up the Image GUI 
            height: The height of the Image will be used for setting up the Image GUI
            filePath: This filePath of the Image as NewImage.png that will create a new copy that the file will only
                      be modify as the program continues to run while the original image is saved as a copy
        """
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        if (fileName):
            global width, height, filePath
            newImg = cv2.imread(fileName)
            height = newImg.shape[0]
            width = newImg.shape[1]
            cv2.imwrite("NewImage.png", newImg)
            filePath = "NewImage.png"
            pixmap = QtGui.QPixmap(filePath) # Setup pixmap with the provided image
            self.window = QtWidgets.QMainWindow()
            self.ui = Image()
            self.ui.setupUi(self.window, width, height)
            self.ui.imgLbl.setPixmap(pixmap)
            self.ui.imgLbl.setAlignment(QtCore.Qt.AlignLeft)
            self.window.show()
            self.analyzeColor()

    def make_histogram(self, clusters):
        numLabels = np.arange(0, len(np.unique(clusters.labels_)) + 1)
        hist, _ = np.histogram(clusters.labels_, bins = numLabels)
        hist = hist.astype('float32')
        hist /= hist.sum()
        return hist
    
    def analyzeColor(self):
        global filePath, RGB
        RGB = []
        img = cv2.imread(filePath)
        height, width, _ = np.shape(img)
        image = img.reshape((height * width, 3))
        clusters = KMeans(n_clusters=5)
        clusters.fit(image)
        histogram = self.make_histogram(clusters)
        ordered = zip(histogram, clusters.cluster_centers_)
        ordered = sorted(ordered, key=lambda x: x[0], reverse = True)
        for index, row in enumerate(ordered):
            RGB.append((int(row[1][2]), int(row[1][1]), int(row[1][0])))

    def make_bar(self, color):
        bar = np.zeros((200, 200, 3), np.uint8)
        bar[:] = [color[2], color[1], color[0]]
        print(bar)
        return bar

    def showCommonColor(self):
        global RGB, nun_clusters
        bars = []
        for i in range(num_clusters):
            bar = self.make_bar(RGB[i])
            bars.append(bar)
        img = np.hstack(bars)
        for j in range(num_clusters):
            img = cv2.putText(img, str(RGB[j]), (5 + (j * 200), 20), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)

        cv2.imwrite("Common_Colors.png", img)
        fileName = "Common_Colors.png"
        pixmap = QtGui.QPixmap(fileName)
        self.window2 = QtWidgets.QMainWindow()
        self.ui2 = AnalyzeColor()
        self.ui2.setupUi(self.window2, 200 * num_clusters)
        self.ui2.anzLbl.setPixmap(pixmap)
        self.ui2.anzLbl.setAlignment(QtCore.Qt.AlignLeft)
        self.window2.show()

    def changePixel(self):
        """ 
        When this function is triggered, it will replace the pixel color RGB value with the user custom color from the sliders' positions
        It will replace from (x-5) to (x+5) and (y-5) to (y+5) rather than one pixel value unless if the user select the extremes which will only replace that value
        Then it will save a new Image called "NewImage.png" which does not effect the original copy of the image
        """
        global xValue, yValue, redValue, greenValue, blueValue, filePath, width, height
        newImg = cv2.imread(filePath)
        interval = 10
        if ((xValue >= 1196) or (xValue <= 4) or (yValue <= 4) or (yValue >= 671)):
            interval = 0
        halfInterval = int(interval / 2)
        newImg[yValue: yValue + interval, xValue: xValue + halfInterval] = (blueValue, greenValue, redValue)
        newImg[yValue - interval: yValue, xValue: xValue + halfInterval] = (blueValue, greenValue, redValue)
        newImg[yValue: yValue + interval, xValue - halfInterval: xValue] = (blueValue, greenValue, redValue)
        newImg[yValue - interval: yValue, xValue - halfInterval: xValue] = (blueValue, greenValue, redValue)
        cv2.imwrite("NewImage.png", newImg)
        pixmap = QtGui.QPixmap(filePath)
        self.window = QtWidgets.QMainWindow()
        self.ui = Image()
        self.ui.setupUi(self.window, width, height)
        self.ui.imgLbl.setPixmap(pixmap)
        self.ui.imgLbl.setAlignment(QtCore.Qt.AlignLeft)
        self.window.show()
        self.analyzeColor()

    def resetAll(self):
        """
        Reset all the global variables to its original state
        """
        global filePath, xValue, yValue, redRange, redAverage, greenRange, greenAverage, blueRange, blueAverage, redValue, greenValue, blueValue, failed, width, height, num_clusters, RGB
        filePath = "No_Path"
        xValue = 0
        yValue = 0
        redAverage = 128
        redRange = 0
        greenAverage = 128
        greenRange = 0
        blueAverage = 128
        blueRange = 0
        redValue = 0
        greenValue = 0 
        blueValue = 0
        width = 0
        height = 0
        failed = False
        num_clusters = 1
        RGB = []
        self.executeDetect.setCheckState(0)
        self.window.hide()
        self.window2.hide()
        
    def color_detect(self, redMin, redMax, greenMin, greenMax, blueMin, blueMax):
        """
        Show the image color if the color is in the range that the user wants to see
        If it is not, it will show as black
        At the same time, it will save a new Image called "Detection.png" to see the results without running the program for future usage
        """
        global filePath, width, height
        img = cv2.imread(filePath)
        Lower = np.array([blueMin, greenMin, redMin], dtype = "uint8")
        Upper = np.array([blueMax, greenMax, redMax], dtype = "uint8")
        mask = cv2.inRange(img, Lower, Upper)
        output = cv2.bitwise_and(img, img, mask = mask)
        cv2.imwrite("Detection.png", output)
        fileName = "Detection.png"
        pixmap = QtGui.QPixmap(fileName)
        self.window = QtWidgets.QMainWindow()
        self.ui = Image()
        self.ui.setupUi(self.window, width, height)
        self.ui.imgLbl.setPixmap(pixmap)
        self.ui.imgLbl.setAlignment(QtCore.Qt.AlignLeft)
        self.window.show()
    
    def colorDetect(self):
        """
        Condition checking if everything that the user has selected it valid
        If it failes, then it will return a warning message and automatically uncheck the checkbox
        At the same time, if the user want to see the original image, simply unchecking the checkbox will show the original image
        """
        global filePath, redAverage, redRange, greenAverage, greenRange, blueAverage, blueRange, failed, width, height
        
        redMin = redAverage - redRange
        if (redMin < 0):
            redMin = 0
        redMax = redAverage + redRange
        if (redMax > 255):
            redMax = 255
        greenMin = greenAverage - greenRange
        if (greenMin < 0):
            greenMin = 0
        greenMax = greenAverage + greenRange
        if (greenMax > 255):
            greenMax = 255
        blueMin = blueAverage - blueRange
        if (blueMin < 0):
            blueMin = 0
        blueMax = blueAverage + blueRange
        if (blueMax > 255):
            blueMax = 255
        
        if ((filePath == "No_Path") and (self.executeDetect.isChecked() == True)):
            failed = True
            self.error1()
            self.executeDetect.setCheckState(0)

        elif(self.executeDetect.isChecked()):
            
            self.color_detect(redMin, redMax, greenMin, greenMax, blueMin, blueMax)

        elif((self.executeDetect.checkState() == 0) and (failed == True)):
            failed = False
        
        elif((self.executeDetect.checkState() == 0)):
            pixmap = QtGui.QPixmap(filePath)
            self.window = QtWidgets.QMainWindow()
            self.ui = Image()
            self.ui.setupUi(self.window, width, height)
            self.ui.imgLbl.setPixmap(pixmap)
            self.ui.imgLbl.setAlignment(QtCore.Qt.AlignLeft)
            self.window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.analyzeBtn.setText(_translate("MainWindow", "Analyze"))
        self.yText.setText(_translate("MainWindow", "Y"))
        self.imgBtn.setText(_translate("MainWindow", "Select Image"))
        self.colorChangeText.setText(_translate("MainWindow", "Color Pixel Changer"))
        self.greenText.setText(_translate("MainWindow", "Green"))
        self.redText.setText(_translate("MainWindow", "Red"))
        self.xText.setText(_translate("MainWindow", "X"))
        self.redRangeText.setText(_translate("MainWindow", "Red Range"))
        self.author.setText(_translate("MainWindow", "Created by Kenneth Kang"))
        self.descriptionBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Before you do anything, please select an Image first by clicking the button &quot;Select Image&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">In this program, you can change the range of color detection in the Color Range Detection Side and clicking Execute Color Detection checkbox.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">At the same time, you can also change certain pixel color value by clicking the image location and changing it on the Color Pixel Changer Side.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Last, you can get the most common colors in the image by entering how many as integer and click Analyze.</p></body></html>"))
        self.questionText.setText(_translate("MainWindow", "How many top common colors you want to find?"))
        self.blueRangeText.setText(_translate("MainWindow", "Blue Range"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.greenAverageText.setText(_translate("MainWindow", "Green Average"))
        self.blueText.setText(_translate("MainWindow", "Blue"))
        self.changeColorBtn.setText(_translate("MainWindow", "Change Color"))
        self.colorPreviewText.setText(_translate("MainWindow", "Color Preview"))
        self.redAverageText.setText(_translate("MainWindow", "Red Average"))
        self.blueAverageText.setText(_translate("MainWindow", "Blue Average"))
        self.colorRangeText.setText(_translate("MainWindow", "Color Range Detection"))
        self.executeDetect.setText(_translate("MainWindow", "Execute Color Detection"))
        self.title.setText(_translate("MainWindow", "URSA 2020~2021 Explanable Computer Vision Settings"))
        self.greenRangeText.setText(_translate("MainWindow", "Green Range"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
