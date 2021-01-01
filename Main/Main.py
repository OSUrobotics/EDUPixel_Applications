###########################################################################################################################
## Author: Kenneth Kang                                                                                                  ##
## Purpose: This program is a combination between Color Code Picker.py and Picture Color Detector.py while it also       ##
## contains an analysis system to detect what are the most common color in a user selected image. It still serves the    ##
## same purpose of education each individuals of the lack of computer vision and Artifical Intelligence.                 ##
##                                                                                                                       ##
## Dependencies: PyQt5, Numpy, cv2, OS, sklearn                                                                          ##
##                                                                                                                       ##
## Other software Usage: Designer.exe for PyQt5(That can be found in .ui file)                                           ##
###########################################################################################################################

# https://realpython.com/documenting-python-code/ Need to Document the entire code when I complete it

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import cv2
from sklearn.cluster import KMeans
import os

# Global Variables Between Two Classes
filePath = "No_Path"
xValue = 0
yValue = 0
redMin = 0
redMax = 255
greenMin = 0
greenMax = 255
blueMin = 0
blueMax = 255
redValue = 0
greenValue = 0 
blueValue = 0
width = 0
height = 0
failed = False
num_clusters = 7


class Image(object):
    """
    This class is for the child GUI for displaying the image for user selection. 
    """
    def setupUi(self, MainWindow, width, height):
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image"))

    def captureIt(self, event):
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
    . 
    """
    def setupUi(self, MainWindow, width):
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


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f'Top {num_clusters} Most Common Colors with Color Code'))

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):

        # Global Variables
        global filePath, xValue, yValue, redValue, greenValue, blueValue, redMin, redMax, greenMin, greenMax, blueMin, blueMax 
       
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1184, 744)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.blueText = QtWidgets.QLabel(self.centralwidget)
        self.blueText.setGeometry(QtCore.QRect(820, 240, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueText.setFont(font)
        self.blueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueText.setObjectName("blueText")

        self.redValueText = QtWidgets.QLabel(self.centralwidget)
        self.redValueText.setGeometry(QtCore.QRect(1090, 140, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redValueText.setFont(font)
        self.redValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.redValueText.setNum(redValue)
        self.redValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.redValueText.setObjectName("redValueText")

        self.greenValueText = QtWidgets.QLabel(self.centralwidget)
        self.greenValueText.setGeometry(QtCore.QRect(1090, 200, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenValueText.setFont(font)
        self.greenValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.greenValueText.setNum(0)
        self.greenValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenValueText.setObjectName("greenValueText")

        self.redText = QtWidgets.QLabel(self.centralwidget)
        self.redText.setGeometry(QtCore.QRect(820, 110, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redText.setFont(font)
        self.redText.setAlignment(QtCore.Qt.AlignCenter)
        self.redText.setObjectName("redText")

        self.blueValueText = QtWidgets.QLabel(self.centralwidget)
        self.blueValueText.setGeometry(QtCore.QRect(1090, 260, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueValueText.setFont(font)
        self.blueValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.blueValueText.setNum(blueValue)
        self.blueValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueValueText.setObjectName("blueValueText")

        self.greenSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenSlider.setGeometry(QtCore.QRect(570, 200, 510, 22))
        self.greenSlider.setMaximum(255)
        self.greenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenSlider.setObjectName("greenSlider")

        self.redSlider = QtWidgets.QSlider(self.centralwidget)
        self.redSlider.setGeometry(QtCore.QRect(570, 140, 510, 22))
        self.redSlider.setMaximum(255)
        self.redSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redSlider.setObjectName("redSlider")

        self.greenText = QtWidgets.QLabel(self.centralwidget)
        self.greenText.setGeometry(QtCore.QRect(820, 180, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenText.setFont(font)
        self.greenText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenText.setObjectName("greenText")

        self.blueSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueSlider.setGeometry(QtCore.QRect(570, 260, 510, 22))
        self.blueSlider.setMaximum(255)
        self.blueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueSlider.setObjectName("blueSlider")

        self.colorPreview = QtWidgets.QLabel(self.centralwidget)
        self.colorPreview.setGeometry(QtCore.QRect(860, 330, 130, 50))
        self.colorPreview.setFrameShape(QtWidgets.QFrame.Box)
        self.colorPreview.setText("")
        self.colorPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreview.setObjectName("colorPreview")

        self.colorPreviewText = QtWidgets.QLabel(self.centralwidget)
        self.colorPreviewText.setGeometry(QtCore.QRect(860, 300, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.colorPreviewText.setFont(font)
        self.colorPreviewText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreviewText.setObjectName("colorPreviewText")

        self.changeColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.changeColorBtn.setGeometry(QtCore.QRect(1010, 340, 130, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.changeColorBtn.setFont(font)
        self.changeColorBtn.setObjectName("changeColorBtn")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 0, 1141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.blueMinText = QtWidgets.QLabel(self.centralwidget)
        self.blueMinText.setGeometry(QtCore.QRect(170, 520, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueMinText.setFont(font)
        self.blueMinText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueMinText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueMinText.setObjectName("blueMinText")

        self.blueMinValue = QtWidgets.QLabel(self.centralwidget)
        self.blueMinValue.setGeometry(QtCore.QRect(400, 560, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueMinValue.setFont(font)
        self.blueMinValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueMinValue.setNum(blueMin)
        self.blueMinValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueMinValue.setObjectName("blueMinValue")

        self.greenMaxSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenMaxSlider.setGeometry(QtCore.QRect(30, 422, 351, 20))
        self.greenMaxSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.greenMaxSlider.setMaximum(255)
        self.greenMaxSlider.setSliderPosition(255)
        self.greenMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenMaxSlider.setObjectName("greenMaxSlider")

        self.redMinValue = QtWidgets.QLabel(self.centralwidget)
        self.redMinValue.setGeometry(QtCore.QRect(400, 130, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redMinValue.setFont(font)
        self.redMinValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redMinValue.setNum(redMin)
        self.redMinValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redMinValue.setObjectName("redMinValue")

        self.redMaxValue = QtWidgets.QLabel(self.centralwidget)
        self.redMaxValue.setGeometry(QtCore.QRect(400, 210, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redMaxValue.setFont(font)
        self.redMaxValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redMaxValue.setNum(redMax)
        self.redMaxValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redMaxValue.setObjectName("redMaxValue")

        self.redMaxText = QtWidgets.QLabel(self.centralwidget)
        self.redMaxText.setGeometry(QtCore.QRect(170, 180, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redMaxText.setFont(font)
        self.redMaxText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redMaxText.setAlignment(QtCore.Qt.AlignCenter)
        self.redMaxText.setObjectName("redMaxText")

        self.redMaxSlider = QtWidgets.QSlider(self.centralwidget)
        self.redMaxSlider.setGeometry(QtCore.QRect(30, 210, 351, 22))
        self.redMaxSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.redMaxSlider.setMaximum(255)
        self.redMaxSlider.setSliderPosition(255)
        self.redMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redMaxSlider.setObjectName("redMaxSlider")

        self.redMinText = QtWidgets.QLabel(self.centralwidget)
        self.redMinText.setGeometry(QtCore.QRect(170, 100, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redMinText.setFont(font)
        self.redMinText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redMinText.setAlignment(QtCore.Qt.AlignCenter)
        self.redMinText.setObjectName("redMinText")

        self.blueMaxValue = QtWidgets.QLabel(self.centralwidget)
        self.blueMaxValue.setGeometry(QtCore.QRect(400, 640, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueMaxValue.setFont(font)
        self.blueMaxValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueMaxValue.setNum(blueMax)
        self.blueMaxValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueMaxValue.setObjectName("blueMaxValue")

        self.greenMinText = QtWidgets.QLabel(self.centralwidget)
        self.greenMinText.setGeometry(QtCore.QRect(170, 310, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.greenMinText.setFont(font)
        self.greenMinText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenMinText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenMinText.setObjectName("greenMinText")

        self.greenMaxText = QtWidgets.QLabel(self.centralwidget)
        self.greenMaxText.setGeometry(QtCore.QRect(170, 390, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.greenMaxText.setFont(font)
        self.greenMaxText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenMaxText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenMaxText.setObjectName("greenMaxText")

        self.greenMaxValue = QtWidgets.QLabel(self.centralwidget)
        self.greenMaxValue.setGeometry(QtCore.QRect(400, 420, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenMaxValue.setFont(font)
        self.greenMaxValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenMaxValue.setNum(greenMax)
        self.greenMaxValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenMaxValue.setObjectName("greenMaxValue")

        self.blueMinSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueMinSlider.setGeometry(QtCore.QRect(30, 560, 351, 22))
        self.blueMinSlider.setMaximum(255)
        self.blueMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueMinSlider.setObjectName("blueMinSlider")

        self.greenMinSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenMinSlider.setGeometry(QtCore.QRect(30, 340, 351, 22))
        self.greenMinSlider.setMaximum(255)
        self.greenMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenMinSlider.setObjectName("greenMinSlider")

        self.blueMaxSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueMaxSlider.setGeometry(QtCore.QRect(30, 640, 351, 22))
        self.blueMaxSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blueMaxSlider.setMaximum(255)
        self.blueMaxSlider.setSliderPosition(255)
        self.blueMaxSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueMaxSlider.setObjectName("blueMaxSlider")

        self.redMinSlider = QtWidgets.QSlider(self.centralwidget)
        self.redMinSlider.setGeometry(QtCore.QRect(30, 130, 351, 22))
        self.redMinSlider.setMaximum(255)
        self.redMinSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redMinSlider.setObjectName("redMinSlider")

        self.blueMaxText = QtWidgets.QLabel(self.centralwidget)
        self.blueMaxText.setGeometry(QtCore.QRect(170, 600, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueMaxText.setFont(font)
        self.blueMaxText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueMaxText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueMaxText.setObjectName("blueMaxText")

        self.colorRangeText = QtWidgets.QLabel(self.centralwidget)
        self.colorRangeText.setGeometry(QtCore.QRect(120, 60, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.colorRangeText.setFont(font)
        self.colorRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.colorRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorRangeText.setObjectName("colorRangeText")

        self.greenMinValue = QtWidgets.QLabel(self.centralwidget)
        self.greenMinValue.setGeometry(QtCore.QRect(400, 340, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenMinValue.setFont(font)
        self.greenMinValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenMinValue.setNum(greenMin)
        self.greenMinValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenMinValue.setObjectName("greenMinValue")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(480, 50, 20, 651))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.colorChangeText = QtWidgets.QLabel(self.centralwidget)
        self.colorChangeText.setGeometry(QtCore.QRect(750, 60, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.colorChangeText.setFont(font)
        self.colorChangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.colorChangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorChangeText.setObjectName("colorChangeText")

        self.borderLineWithGB = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithGB.setGeometry(QtCore.QRect(-20, 490, 511, 20))
        self.borderLineWithGB.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithGB.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithGB.setObjectName("borderLineWithGB")

        self.borderLineWithRG = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithRG.setGeometry(QtCore.QRect(-20, 280, 511, 20))
        self.borderLineWithRG.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithRG.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithRG.setObjectName("borderLineWithRG")

        self.borderLineWithImg = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithImg.setGeometry(QtCore.QRect(490, 390, 691, 20))
        self.borderLineWithImg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithImg.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithImg.setObjectName("borderLineWithImg")

        self.imgBtn = QtWidgets.QPushButton(self.centralwidget)
        self.imgBtn.setGeometry(QtCore.QRect(540, 410, 280, 90))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(26)
        self.imgBtn.setFont(font)
        self.imgBtn.setObjectName("imgBtn")

        self.executeDetect = QtWidgets.QCheckBox(self.centralwidget)
        self.executeDetect.setGeometry(QtCore.QRect(540, 510, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.executeDetect.setFont(font)
        self.executeDetect.setObjectName("executeDetect")

        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(520, 610, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.resetBtn.setFont(font)
        self.resetBtn.setObjectName("resetBtn")

        self.descriptionBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.descriptionBox.setGeometry(QtCore.QRect(860, 410, 311, 261))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.descriptionBox.setFont(font)
        self.descriptionBox.setObjectName("descriptionBox")

        self.yValueText = QtWidgets.QLabel(self.centralwidget)
        self.yValueText.setGeometry(QtCore.QRect(710, 350, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yValueText.setFont(font)
        self.yValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.yValueText.setNum(yValue)
        self.yValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.yValueText.setObjectName("yValueText")

        self.xText = QtWidgets.QLabel(self.centralwidget)
        self.xText.setGeometry(QtCore.QRect(600, 310, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xText.setFont(font)
        self.xText.setAlignment(QtCore.Qt.AlignCenter)
        self.xText.setObjectName("xText")

        self.xValueText = QtWidgets.QLabel(self.centralwidget)
        self.xValueText.setGeometry(QtCore.QRect(600, 350, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xValueText.setFont(font)
        self.xValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.xValueText.setNum(xValue)
        self.xValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.xValueText.setObjectName("xValueText")

        self.yText = QtWidgets.QLabel(self.centralwidget)
        self.yText.setGeometry(QtCore.QRect(710, 310, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yText.setFont(font)
        self.yText.setAlignment(QtCore.Qt.AlignCenter)
        self.yText.setObjectName("yText")

        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setGeometry(QtCore.QRect(1030, 680, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.author.setFont(font)
        self.author.setObjectName("label")

        self.analyzeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.analyzeBtn.setGeometry(QtCore.QRect(690, 600, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.analyzeBtn.setFont(font)
        self.analyzeBtn.setObjectName("analyzeBtn")


        self.numClusterInput = QtWidgets.QLineEdit(self.centralwidget)
        self.numClusterInput.setGeometry(QtCore.QRect(800, 570, 41, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.numClusterInput.setFont(font)
        self.numClusterInput.setText("7")
        self.numClusterInput.setAlignment(QtCore.Qt.AlignCenter)
        self.numClusterInput.setObjectName("numClusterInput")

        self.questionText = QtWidgets.QLabel(self.centralwidget)
        self.questionText.setGeometry(QtCore.QRect(500, 570, 301, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.questionText.setFont(font)
        self.questionText.setObjectName("questionText")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()
        

        #Functions for each Features
        
        #Timer
        self.timer.timeout.connect(self.updateValue)
        self.timer.start(10)

        # Button
        self.imgBtn.clicked.connect(self.openWindow)
        self.changeColorBtn.clicked.connect(self.changePixel)
        self.resetBtn.clicked.connect(self.resetAll)
        self.analyzeBtn.clicked.connect(self.openAnalyze)

        # CheckBox
        self.executeDetect.stateChanged.connect(self.colorDetect)

        # Slider
        self.redSlider.valueChanged[int].connect(self.colorChangeRed)
        self.greenSlider.valueChanged[int].connect(self.colorChangeGreen)
        self.blueSlider.valueChanged[int].connect(self.colorChangeBlue)
        self.redMinSlider.valueChanged.connect(self.redMinUpdate)
        self.redMaxSlider.valueChanged.connect(self.redMaxUpdate)
        self.greenMinSlider.valueChanged.connect(self.greenMinUpdate)
        self.greenMaxSlider.valueChanged.connect(self.greenMaxUpdate)
        self.blueMinSlider.valueChanged.connect(self.blueMinUpdate)
        self.blueMaxSlider.valueChanged.connect(self.blueMaxUpdate)

    def openWindow(self):
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

    def make_histogram(self,cluster):
    # """
    # Count the number of pixels in each cluster
    # :param: KMeans cluster
    # :return: numpy histogram
    # """
        numLabels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
        hist, _ = np.histogram(cluster.labels_, bins=numLabels)
        hist = hist.astype('float32')
        hist /= hist.sum()
        return hist


    def make_bar(self,height, width, color):
    # """
    # Create an image of a given color
    # :param: height of the image
    # :param: width of the image
    # :param: BGR pixel values of the color
    # :return: tuple of bar, rgb values, and hsv values
    # """
        bar = np.zeros((height, width, 3), np.uint8)
        bar[:] = color
        red, green, blue = int(color[2]), int(color[1]), int(color[0])
        hsv_bar = cv2.cvtColor(bar, cv2.COLOR_BGR2HSV)
        hue, sat, val = hsv_bar[0][0]
        return bar, (red, green, blue), (hue, sat, val)

    def openAnalyze(self):
        global filePath, num_clusters

        if (self.numClusterInput.text()):
            num_clusters = int(self.numClusterInput.text())

        if filePath == "No_Path":
            self.error1()
        else:
            img = cv2.imread(filePath)
            height, width, _ = np.shape(img)
            image = img.reshape((height * width, 3))
            clusters = KMeans(n_clusters=num_clusters)
            clusters.fit(image)
            histogram = self.make_histogram(clusters)
            combined = zip(histogram, clusters.cluster_centers_)
            combined = sorted(combined, key = lambda x: x[0], reverse= True)
            bars = []
            RGB = []
            for index, rows in enumerate(combined):
                bar, rgb, hsx = self.make_bar(200,200, rows[1])
                RGB.append(str(rgb))
                bars.append(bar)
            img = np.hstack(bars)
            for i in range (len(RGB)):
                img = cv2.putText(img, RGB[i], (5 + (i * 200), 20), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
            cv2.imwrite("Common_Colors.png", img)
            fileName = "Common_Colors.png"
            pixmap = QtGui.QPixmap(fileName)
            self.window2 = QtWidgets.QMainWindow()
            self.ui2 = AnalyzeColor()
            self.ui2.setupUi(self.window2, 200 * num_clusters)
            self.ui2.anzLbl.setPixmap(pixmap)
            self.ui2.anzLbl.setAlignment(QtCore.Qt.AlignLeft)
            self.window2.show()

    def updateValue(self):
        global xValue, yValue, redValue, greenValue, blueValue, redMin, redMax, greenMin, greenMax, blueMin, blueMax
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
        self.redMinValue.setNum(redMin)
        self.redMaxValue.setNum(redMax)
        self.greenMinValue.setNum(greenMin)
        self.greenMaxValue.setNum(greenMax)
        self.blueMinValue.setNum(blueMin)
        self.blueMaxValue.setNum(blueMax)
        self.redMinSlider.setSliderPosition(redMin)
        self.redMaxSlider.setSliderPosition(redMax)
        self.greenMinSlider.setSliderPosition(greenMin)
        self.greenMaxSlider.setSliderPosition(greenMax)
        self.blueMinSlider.setSliderPosition(blueMin)
        self.blueMaxSlider.setSliderPosition(blueMax)

    def colorChangeRed(self, value):
        global redValue
        redValue = value

    def colorChangeGreen(self, value):
        global greenValue
        greenValue = value

    def colorChangeBlue(self, value):
        global blueValue
        blueValue = value
         
    def changePixel(self):
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
        
    def redMinUpdate(self):
        global redMin
        redMin = self.redMinSlider.sliderPosition()
    
    def redMaxUpdate(self):
        global redMax
        redMax = self.redMaxSlider.sliderPosition()

    def greenMinUpdate(self):
        global greenMin
        greenMin = self.greenMinSlider.sliderPosition()

    def greenMaxUpdate(self):
        global greenMax
        greenMax = self.greenMaxSlider.sliderPosition()

    def blueMinUpdate(self):
        global blueMin
        blueMin = self.blueMinSlider.sliderPosition()

    def blueMaxUpdate(self):
        global blueMax
        blueMax = self.blueMaxSlider.sliderPosition()

    def error1(self):
        errorMessage1 = QtWidgets.QMessageBox()
        errorMessage1.setWindowTitle("Error")
        errorMessage1.setText("Please Select an Image File!")
        errorMessage1.setIcon(QtWidgets.QMessageBox.Critical)
        x = errorMessage1.exec_()

    def error2(self):
        errorMessage2 = QtWidgets.QMessageBox()
        errorMessage2.setWindowTitle("Error")
        errorMessage2.setText("One or more has Invalid Color Range!")
        errorMessage2.setIcon(QtWidgets.QMessageBox.Critical)
        x = errorMessage2.exec_()

    def colorDetect(self):
        global filePath, redMin, redMax, greenMin, greenMax, blueMin, blueMax, failed, width, height
        
        if ((filePath == "No_Path") and (self.executeDetect.isChecked() == True)):
            failed = True
            self.error1()
            self.executeDetect.setCheckState(0)
            
        elif((redMin > redMax) or (greenMin > greenMax) or (blueMin > blueMax)):
            failed = True
            self.error2()
            self.executeDetect.setCheckState(0)
        
        elif(self.executeDetect.isChecked()):
            self.color_detect()

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

    def color_detect(self):
        global filePath, redMin, redMax, greenMin, greenMax, blueMin, blueMax, width, height
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
        os.remove(fileName)
        self.window.show()
        
    def resetAll(self):
        global filePath, xValue, yValue, redMin, redMax, greenMin, greenMax, blueMin, blueMax, redValue, greenValue, blueValue, failed, width, height, num_clusters
        filePath = "No_Path"
        xValue = 0
        yValue = 0
        redMin = 0
        redMax = 255
        greenMin = 0
        greenMax = 255
        blueMin = 0
        blueMax = 255
        redValue = 0
        greenValue = 0 
        blueValue = 0
        failed = False
        width = 0
        height = 0
        num_clusters = 7
        self.executeDetect.setCheckState(0)
        self.numClusterInput.setText("7")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.blueText.setText(_translate("MainWindow", "Blue"))
        self.redText.setText(_translate("MainWindow", "Red"))
        self.greenText.setText(_translate("MainWindow", "Green"))
        self.colorPreviewText.setText(_translate("MainWindow", "Color Preview"))
        self.changeColorBtn.setText(_translate("MainWindow", "Change Color"))
        self.title.setText(_translate("MainWindow", "URSA 2020~2021 Explanable Computer Vision Settings"))
        self.blueMinText.setText(_translate("MainWindow", "Blue Min"))
        self.redMaxText.setText(_translate("MainWindow", "Red Max"))
        self.redMinText.setText(_translate("MainWindow", "Red Min"))
        self.greenMinText.setText(_translate("MainWindow", "Green Min"))
        self.greenMaxText.setText(_translate("MainWindow", "Green Max"))
        self.blueMaxText.setText(_translate("MainWindow", "Blue Max"))
        self.colorRangeText.setText(_translate("MainWindow", "Color Range Detection"))
        self.colorChangeText.setText(_translate("MainWindow", "Color Pixel Changer"))
        self.imgBtn.setText(_translate("MainWindow", "Select Image"))
        self.executeDetect.setText(_translate("MainWindow", "Execute Color Detection"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
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
        self.xText.setText(_translate("MainWindow", "X"))
        self.yText.setText(_translate("MainWindow", "Y"))
        self.author.setText(_translate("MainWindow", "Created by Kenneth Kang"))
        self.analyzeBtn.setText(_translate("MainWindow", "Analyze"))
        self.questionText.setText(_translate("MainWindow", "How many top common colors you want to find?"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
