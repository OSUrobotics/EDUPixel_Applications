###########################################################################################################################
## Author: Kenneth Kang                                                                                                  ##
## Purpose: This program is updated version that able to do with multiple pictures. While majority of the features are   ##
## the same, but there were modifications since the last version. For the people who do not know about the previous      ##
## version, here is the list below about its feature and where to find it.                                               ##          
##                                                                                                                       ##
##      1. User can select a certain max and min for RGB and see if any of the pixels is within that range for a image   ##
##      2. User were able to modify the image by changing the RGB value for a certian location                           ##
##      3. User can get the most top 7 common color on a certain image                                                   ##
##      4. User can get the RGB when the user select any location on the image with its x and y value as well            ##
##                                                                                                                       ##
## Now here are the updates since that version. If you want old versions, you can check the previous versions            ##
##                                                                                                                       ##
##      1. The slider has changed from max/min to average/range to see dramatic differences                              ##
##      2. Removed the feature of changing RGB values of the image                                                       ##
##      3. Able to do color detect feature with multiple pictures by iterating with other images                         ##
##      4. Reduce the complie time unless it is the first time loading(pickle package will support this feature)         ##
##      5. Reduce the max number of common colors to 5 from 7                                                            ##
##      6. Change the layout of the design with the updates                                                              ##
##      7. Remove multiple GUI for each display: everything is happening within one GUI                                  ##
##      8. Change the Top Common Color Display with Proportion and vertical shape                                        ## 
##                                                                                                                       ##
## Dependencies: PyQt5, Numpy, cv2, sklearn, sys, os, pickle                                                             ##
##                                                                                                                       ##
## Other software Usage: Designer.exe for PyQt5(That can be found in .ui file)                                           ##
###########################################################################################################################
#TODO: Need to update the blub above

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import numpy as np
import cv2
from sklearn.cluster import KMeans
import pickle

# Global Variables
pictures = []
index = 0
redAverage = 128
redRange = 15
greenAverage = 128
greenRange = 15
blueAverage = 128
blueRange = 15
redValue = 0
greenValue = 0
blueValue = 0
xValue = 0
yValue = 0
num = 1


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
            
            Button: By pressing the button will trigger certain function
               nextBtn: nextImage function
               previousBtn: previousImage

            Slider: By changing the position of the slider will trigger certain function
                redAverageSlider: redAverageUpdate function
                redRangeSlider: redRangeUpdate function
                greenAverageSlider: greenAverageUpdate function
                greenRangeSlider: greenRangeUpdate function
                blueAverageSlider: blueAverageUpdate function
                blueRangeSlider: blueRangeUpdate function 
            
            Mouse: By clicking certain location with the mouse, it will trigger certain function
                ogImgLbl event: captureIt function
                commonColorLbl event: captureCommon function
        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 975)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ogImgLbl = QtWidgets.QLabel(self.centralwidget)
        self.ogImgLbl.setGeometry(QtCore.QRect(20, 90, 400, 400))
        self.ogImgLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImgLbl.setCursor(QtCore.Qt.CrossCursor)
        self.ogImgLbl.setText("")
        self.ogImgLbl.setObjectName("ogImgLbl")

        self.executeImgLbl = QtWidgets.QLabel(self.centralwidget)
        self.executeImgLbl.setGeometry(QtCore.QRect(20, 530, 400, 400))
        self.executeImgLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.executeImgLbl.setText("")
        self.executeImgLbl.setObjectName("executeImgLbl")

        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nextBtn.setGeometry(QtCore.QRect(260, 500, 75, 20))
        self.nextBtn.setObjectName("nextBtn")

        self.previousBtn = QtWidgets.QPushButton(self.centralwidget)
        self.previousBtn.setGeometry(QtCore.QRect(90, 500, 75, 20))
        self.previousBtn.setObjectName("previousBtn")

        self.greenAverageText = QtWidgets.QLabel(self.centralwidget)
        self.greenAverageText.setGeometry(QtCore.QRect(620, 360, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.greenAverageText.setFont(font)
        self.greenAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenAverageText.setObjectName("greenAverageText")

        self.redRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.redRangeValue.setGeometry(QtCore.QRect(860, 260, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redRangeValue.setFont(font)
        self.redRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redRangeValue.setText("")
        self.redRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redRangeValue.setObjectName("redRangeValue")

        self.greenRangeText = QtWidgets.QLabel(self.centralwidget)
        self.greenRangeText.setGeometry(QtCore.QRect(630, 440, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.greenRangeText.setFont(font)
        self.greenRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenRangeText.setObjectName("greenRangeText")

        self.greenAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenAverageSlider.setGeometry(QtCore.QRect(490, 390, 351, 22))
        self.greenAverageSlider.setMaximum(255)
        self.greenAverageSlider.setProperty("value", 128)
        self.greenAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenAverageSlider.setObjectName("greenAverageSlider")

        self.greenRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenRangeSlider.setGeometry(QtCore.QRect(490, 472, 351, 20))
        self.greenRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.greenRangeSlider.setMaximum(127)
        self.greenRangeSlider.setProperty("value", 0)
        self.greenRangeSlider.setSliderPosition(0)
        self.greenRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenRangeSlider.setObjectName("greenRangeSlider")

        self.blueAverageText = QtWidgets.QLabel(self.centralwidget)
        self.blueAverageText.setGeometry(QtCore.QRect(630, 570, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueAverageText.setFont(font)
        self.blueAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueAverageText.setObjectName("blueAverageText")
        
        self.redRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.redRangeSlider.setGeometry(QtCore.QRect(490, 260, 351, 22))
        self.redRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.redRangeSlider.setMaximum(127)
        self.redRangeSlider.setProperty("value", 0)
        self.redRangeSlider.setSliderPosition(0)
        self.redRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redRangeSlider.setObjectName("redRangeSlider")

        self.blueRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueRangeSlider.setGeometry(QtCore.QRect(490, 690, 351, 22))
        self.blueRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blueRangeSlider.setMaximum(127)
        self.blueRangeSlider.setSliderPosition(0)
        self.blueRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueRangeSlider.setObjectName("blueRangeSlider")

        self.blueAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueAverageSlider.setGeometry(QtCore.QRect(490, 610, 351, 22))
        self.blueAverageSlider.setMaximum(255)
        self.blueAverageSlider.setProperty("value", 128)
        self.blueAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueAverageSlider.setObjectName("blueAverageSlider")

        self.borderLineWithGB = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithGB.setGeometry(QtCore.QRect(440, 540, 511, 20))
        self.borderLineWithGB.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithGB.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithGB.setObjectName("borderLineWithGB")

        self.blueRangeText = QtWidgets.QLabel(self.centralwidget)
        self.blueRangeText.setGeometry(QtCore.QRect(630, 650, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueRangeText.setFont(font)
        self.blueRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueRangeText.setObjectName("blueRangeText")

        self.redRangeText = QtWidgets.QLabel(self.centralwidget)
        self.redRangeText.setGeometry(QtCore.QRect(630, 230, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redRangeText.setFont(font)
        self.redRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.redRangeText.setObjectName("redRangeText")

        self.redAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.redAverageSlider.setGeometry(QtCore.QRect(490, 180, 351, 22))
        self.redAverageSlider.setMaximum(255)
        self.redAverageSlider.setSliderPosition(128)
        self.redAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redAverageSlider.setObjectName("redAverageSlider")

        self.blueAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.blueAverageValue.setGeometry(QtCore.QRect(860, 610, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueAverageValue.setFont(font)
        self.blueAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueAverageValue.setText("")
        self.blueAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueAverageValue.setObjectName("blueAverageValue")

        self.blueRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.blueRangeValue.setGeometry(QtCore.QRect(860, 690, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueRangeValue.setFont(font)
        self.blueRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueRangeValue.setText("")
        self.blueRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueRangeValue.setObjectName("blueRangeValue")

        self.redAverageText = QtWidgets.QLabel(self.centralwidget)
        self.redAverageText.setGeometry(QtCore.QRect(630, 150, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redAverageText.setFont(font)
        self.redAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.redAverageText.setObjectName("redAverageText")

        self.redAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.redAverageValue.setGeometry(QtCore.QRect(860, 180, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redAverageValue.setFont(font)
        self.redAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redAverageValue.setText("")
        self.redAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redAverageValue.setObjectName("redAverageValue")

        self.colorRangeText = QtWidgets.QLabel(self.centralwidget)
        self.colorRangeText.setGeometry(QtCore.QRect(580, 110, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.colorRangeText.setFont(font)
        self.colorRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.colorRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorRangeText.setObjectName("colorRangeText")

        self.greenAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.greenAverageValue.setGeometry(QtCore.QRect(860, 390, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenAverageValue.setFont(font)
        self.greenAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenAverageValue.setText("")
        self.greenAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenAverageValue.setObjectName("greenAverageValue")

        self.borderLineWithRG = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithRG.setGeometry(QtCore.QRect(440, 330, 511, 20))
        self.borderLineWithRG.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithRG.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithRG.setObjectName("borderLineWithRG")

        self.greenRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.greenRangeValue.setGeometry(QtCore.QRect(860, 470, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenRangeValue.setFont(font)
        self.greenRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenRangeValue.setText("")
        self.greenRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenRangeValue.setObjectName("greenRangeValue")

        self.borderLineWithGB_2 = QtWidgets.QFrame(self.centralwidget)
        self.borderLineWithGB_2.setGeometry(QtCore.QRect(440, 750, 511, 20))
        self.borderLineWithGB_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.borderLineWithGB_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.borderLineWithGB_2.setObjectName("borderLineWithGB_2")

        self.yText = QtWidgets.QLabel(self.centralwidget)
        self.yText.setGeometry(QtCore.QRect(680, 770, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yText.setFont(font)
        self.yText.setAlignment(QtCore.Qt.AlignCenter)
        self.yText.setObjectName("yText")

        self.xText = QtWidgets.QLabel(self.centralwidget)
        self.xText.setGeometry(QtCore.QRect(570, 770, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xText.setFont(font)
        self.xText.setAlignment(QtCore.Qt.AlignCenter)
        self.xText.setObjectName("xText")

        self.xValueText = QtWidgets.QLabel(self.centralwidget)
        self.xValueText.setGeometry(QtCore.QRect(570, 810, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.xValueText.setFont(font)
        self.xValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.xValueText.setText("")
        self.xValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.xValueText.setObjectName("xValueText")

        self.colorPreviewText = QtWidgets.QLabel(self.centralwidget)
        self.colorPreviewText.setGeometry(QtCore.QRect(790, 830, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.colorPreviewText.setFont(font)
        self.colorPreviewText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreviewText.setObjectName("colorPreviewText")

        self.colorPreview = QtWidgets.QLabel(self.centralwidget)
        self.colorPreview.setGeometry(QtCore.QRect(790, 860, 130, 50))
        self.colorPreview.setFrameShape(QtWidgets.QFrame.Box)
        self.colorPreview.setText("")
        self.colorPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreview.setObjectName("colorPreview")

        self.yValueText = QtWidgets.QLabel(self.centralwidget)
        self.yValueText.setGeometry(QtCore.QRect(680, 810, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.yValueText.setFont(font)
        self.yValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.yValueText.setText("")
        self.yValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.yValueText.setObjectName("yValueText")

        self.redValueText = QtWidgets.QLabel(self.centralwidget)
        self.redValueText.setGeometry(QtCore.QRect(460, 890, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redValueText.setFont(font)
        self.redValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.redValueText.setText("")
        self.redValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.redValueText.setObjectName("redValueText")

        self.greenValueText = QtWidgets.QLabel(self.centralwidget)
        self.greenValueText.setGeometry(QtCore.QRect(570, 890, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenValueText.setFont(font)
        self.greenValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.greenValueText.setText("")
        self.greenValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenValueText.setObjectName("greenValueText")

        self.blueValueText = QtWidgets.QLabel(self.centralwidget)
        self.blueValueText.setGeometry(QtCore.QRect(680, 890, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueValueText.setFont(font)
        self.blueValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.blueValueText.setText("")
        self.blueValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueValueText.setObjectName("blueValueText")

        self.redText = QtWidgets.QLabel(self.centralwidget)
        self.redText.setGeometry(QtCore.QRect(460, 870, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redText.setFont(font)
        self.redText.setAlignment(QtCore.Qt.AlignCenter)
        self.redText.setObjectName("redText")

        self.greenText = QtWidgets.QLabel(self.centralwidget)
        self.greenText.setGeometry(QtCore.QRect(570, 870, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenText.setFont(font)
        self.greenText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenText.setObjectName("greenText")

        self.blueText = QtWidgets.QLabel(self.centralwidget)
        self.blueText.setGeometry(QtCore.QRect(680, 870, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueText.setFont(font)
        self.blueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueText.setObjectName("blueText")

        self.commonColorLbl = QtWidgets.QLabel(self.centralwidget)
        self.commonColorLbl.setGeometry(QtCore.QRect(980, 120, 200, 800))
        self.commonColorLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.commonColorLbl.setObjectName("commonColorLbl")

        self.commonColorSlider = QtWidgets.QSlider(self.centralwidget)
        self.commonColorSlider.setGeometry(QtCore.QRect(1220, 460, 50, 160))
        self.commonColorSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commonColorSlider.setMaximum(5)
        self.commonColorSlider.setMinimum(1)
        self.commonColorSlider.setSliderPosition(1)
        self.commonColorSlider.setOrientation(QtCore.Qt.Vertical)
        self.commonColorSlider.setInvertedAppearance(False)
        self.commonColorSlider.setInvertedControls(False)
        self.commonColorSlider.setObjectName("commonColorSlider")

        self.commonColorValue = QtWidgets.QLabel(self.centralwidget)
        self.commonColorValue.setGeometry(QtCore.QRect(1220, 420, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.commonColorValue.setFont(font)
        self.commonColorValue.setFrameShape(QtWidgets.QFrame.Box)
        self.commonColorValue.setText("")
        self.commonColorValue.setAlignment(QtCore.Qt.AlignCenter)
        self.commonColorValue.setObjectName("commonColorValue")

        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setGeometry(QtCore.QRect(1190, 940, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.author.setFont(font)
        self.author.setObjectName("author")
        
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 10, 1141, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()

        self.readFile()
        
        # Timer 
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        # Button
        self.nextBtn.clicked.connect(self.nextImage)
        self.previousBtn.clicked.connect(self.previousImage)

        # Mouse
        self.ogImgLbl.mousePressEvent = self.captureIt
        self.commonColorLbl.mousePressEvent = self.captureCommon

        # Slider
        self.redAverageSlider.valueChanged.connect(self.redAverageUpdate)
        self.redRangeSlider.valueChanged.connect(self.redRangeUpdate)
        self.greenAverageSlider.valueChanged.connect(self.greenAverageUpdate)
        self.greenRangeSlider.valueChanged.connect(self.greenRangeUpdate)
        self.blueAverageSlider.valueChanged.connect(self.blueAverageUpdate)
        self.blueRangeSlider.valueChanged.connect(self.blueRangeUpdate)
        self.commonColorSlider.valueChanged.connect(self.commonColorNumUpdate)

    def readFile(self):
        """ 
        Before the whole GUI is launch, this function will be triggered. 
        This will read every single image file that is contained inside the OG folder. 
        Then save it with the size of 400 width and 400 height inside the image folder. 
        After that, it will calculate common top 5 colors and proportion. 
        Throughout the function, all the data will be saved inside pictures global variable. 
        Once everydata is complete, it will be saved into pickle file so that reduce the complie time for next run. 
        Last, when the image is added or removed, it will automatically do itself. 

        Related Function:
            analyzeColor(filePath, ind)
        """
        global pictures
        new = False
        removed = 0
        removedPic = []
        fileNum = 0
        j = 0
        path = os.path.abspath(os.getcwd()) + "\OG"
        # If these folder/file do not exists, create one
        if not os.path.exists('images'):
            os.makedirs('images')
        if not os.path.exists('Pic.pickle'):
            f = open("Pic.pickle", "x")
            new = True
        else:
        # if the file exists, open it and call the data 
            old_file = open("Pic.pickle", 'rb')
            pictures = pickle.load(old_file)
            old_file.close()

        # Count how many images are inside the OG folder
        fileNum = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
        
        #TODO: There is a bug of the remove process: I don't know how to solve it

        # If this was first run, then ignore the remove since there is nothing to remove
        if new == False:
            
            # If the length of list is long than the number of images or same, then we know something removed or changed
            if fileNum <= len(pictures):
                
                # Find each index what has changed and save it in a different list
                for i, filename in enumerate(os.listdir(path)):
                    if pictures[j][0] != (path + "\\"+  filename):
                        removedPic.append(i)
                        removed += 1
                        j += 1
                    j += 1

                # By each index we saved, remove from the back side
                for i in range(removed):
                    index = removedPic.pop()
                    os.remove(pictures[index][1])
                    del pictures[index]
                
                # If the list is still longer than number of images, then remove the end values of the list until it matchs the number of images
                if fileNum < len(pictures):
                    difference = len(pictures) - fileNum
                    for i in range (difference):
                        removePicList = pictures.pop()
                        os.remove(removePicList[1])
                        print(pictures)        


        for i, filename in enumerate(os.listdir(path)):
            # only run first cold start with no data
            if new:
                img = cv2.imread(os.path.join(path, filename))
                imgPath = os.path.abspath(os.getcwd()) + f"\images\{filename + str(i)}.png"
                dsize = (400,400)
                output = cv2.resize(img, dsize)
                cv2.imwrite(imgPath, output)
                pictures.append([])
                pictures[i].append(os.path.join(path, filename))
                pictures[i].append(imgPath)
                self.analyzeColor(imgPath, i)

            # If image is added, it will add at the end or in between: this will add at the last
            elif len(pictures) <= i:
                img = cv2.imread(os.path.join(path, filename))
                imgPath = os.path.abspath(os.getcwd()) + f"\images\{filename + str(i)}.png"
                dsize = (400,400)
                output = cv2.resize(img, dsize)
                cv2.imwrite(imgPath, output)
                pictures.append([])
                pictures[i].append(os.path.join(path, filename))
                pictures[i].append(imgPath)
                self.analyzeColor(imgPath, i)
            
            # This will add in-between the list 
            elif pictures[i][0] != os.path.join(path, filename):
                img = cv2.imread(os.path.join(path, filename))
                imgPath = os.path.abspath(os.getcwd()) + f"\images\{filename + str(i)}.png"
                dsize = (400,400)
                output = cv2.resize(img, dsize)
                cv2.imwrite(imgPath, output)
                pictures.insert(i, [])
                pictures[i].append(os.path.join(path, filename))
                pictures[i].append(imgPath)
                self.analyzeColor(imgPath, i)

        # Save the updated data into pickle
        old_file = open("Pic.pickle", 'wb')
        pickle.dump(pictures, old_file)
        old_file.close()

        # Display the first image on the GUI
        pixmap = QtGui.QPixmap(pictures[0][1])
        self.ogImgLbl.setPixmap(pixmap)
        self.ogImgLbl.setAlignment(QtCore.Qt.AlignLeft)

    def analyzeColor(self, filePath, ind):
        """
        This will analyze the top 5 common color for a certain image
        It will store the values of proportion of color and color code inside the global variable of pictures.

        Args:
            filePath: the directory of the image file, String
            ind: index of the pictures list, Int

        Related Functions:
            make_histogram(cluster) 
        """
        global pictures
        # read the image
        img = cv2.imread(filePath)

        # Change the image display to a single line-ish
        height, width, _ = np.shape(img)
        image = img.reshape((height * width, 3))

        # Set the cluster to 5 since we are calculating 5 of them
        clusters = KMeans(n_clusters=5)

        # Find the mid points of each nearest cluster point
        clusters.fit(image)

        # Count the frequencies/proportion of each color
        histogram = self.make_histogram(clusters)

        # Combine and sort with the most to least according to the frequency count
        ordered = zip(histogram, clusters.cluster_centers_)
        ordered = sorted(ordered, key=lambda x: x[0], reverse = True)

        # Append two empty list that will be store the colors and proportion values
        pictures[ind].append([])
        pictures[ind].append([])

        # Add the colors and proportion values to each new appended list
        for index, row in enumerate(ordered):
            pictures[ind][2].append((int(row[1][2]), int(row[1][1]), int(row[1][0])))
            pictures[ind][3].append('%.2f'%(row[0] * 100))

    def make_bar(self, color):
        """
        Create an image of a given color

        Args:
            color: BRG pixel values of the color from cv2, (B, G, R)

        Returns:
            tuple of bar, rgb values, and hsv values
        """
        bar = np.zeros((160, 200, 3), np.uint8)
        bar[:] = [color[2], color[1], color[0]]
        return bar

    def make_histogram(self, clusters):
        """
        Count the number of pixels in each cluster

        Args:
            cluster: The KMeans cluster

        Returns:
            A numpy Histogram
        """
        numLabels = np.arange(0, len(np.unique(clusters.labels_)) + 1)
        hist, _ = np.histogram(clusters.labels_, bins = numLabels)
        hist = hist.astype('float32')
        hist /= hist.sum()
        return hist

    def nextImage(self):
        """
        When this function is triggered, it will iterate the next image
        according to the order from the OG image order.
        This will raise an error message when it hits the end/right end

        Related Function:
            error() 
        """
        global pictures, index
        # If the list is at the end, raise an error to the user
        if (index  == len(pictures) - 1):
            self.error()
            return False
        
        # Otherwise, update the index by adding 1
        index += 1

        # As the index updates, update the image display on the GUI
        pixmap = QtGui.QPixmap(pictures[index][1])
        self.ogImgLbl.setPixmap(pixmap)
        self.ogImgLbl.setAlignment(QtCore.Qt.AlignLeft)

    def previousImage(self):
        """
        When this function is triggered, it will iterate the previous image
        according to the order from the OG image order.
        This will raise an error message when it hits the end/left end

        Related Function:
            error() 
        """
        global index, pictures
        # If the index value is 0, since that is the end of the list, it will raise an error to the user
        if (index  == 0):
            self.error()
            return False

        # Otherwise, reduce the index value by 1
        index -= 1

        # As the index value updates, update the display accordingly
        pixmap = QtGui.QPixmap(pictures[index][1])
        self.ogImgLbl.setPixmap(pixmap)
        self.ogImgLbl.setAlignment(QtCore.Qt.AlignLeft) 

    def error(self):
        """
        This function will be triggered if the user reach the end of the list of images
        """
        errorMessage = QtWidgets.QMessageBox()
        errorMessage.setWindowTitle("Error")
        errorMessage.setText("Out of Range")
        errorMessage.setIcon(QtWidgets.QMessageBox.Critical)
        x = errorMessage.exec_()

    def commonColorNumUpdate(self):
        """
        This function will update the value of num when the commonColorSlider is moved.
        """
        global num
        num = self.commonColorSlider.sliderPosition()
    
    def redRangeUpdate(self):
        """
        This function will update the value of redRange when the redRangeSlider is moved
        """
        global redRange
        redRange = self.redRangeSlider.sliderPosition()

    def redAverageUpdate(self):
        """
        This function will update the value of redAverage when the redAverageSlider is moved
        """
        global redAverage
        redAverage = self.redAverageSlider.sliderPosition()

    def greenRangeUpdate(self):
        """
        This function will update the value of greenRange when the greenRangeSlider is moved
        """
        global greenRange
        greenRange = self.greenRangeSlider.sliderPosition()

    def greenAverageUpdate(self):
        """
        This function will update the value of greenAverage when the greenAverageSlider is moved
        """
        global greenAverage
        greenAverage = self.greenAverageSlider.sliderPosition()

    def blueRangeUpdate(self):
        """
        This function will update the value of blueRange when the blueRangeSlider is moved
        """
        global blueRange
        blueRange = self.blueRangeSlider.sliderPosition()

    def blueAverageUpdate(self):
        """
        This function will update the value of blueAverage when the blueAverageSlider is moved
        """
        global blueAverage
        blueAverage = self.blueAverageSlider.sliderPosition()
    
    def update(self):
        """
        This function will be (almost) continuously running when the GUI is up.
        When the user change any values, it will automatically update text value or functions that uses those values.
        Or it will update the preview color when the user select certain location on an image

        Related Functions:
            colorDetect()
            showCommonColor()
        """
        
        global redAverage, redRange, greenAverage, greenRange, blueAverage, blueRange, redValue, greenValue, blueValue, xValue, yValue, num

        # Update the Text Value
        self.redAverageValue.setNum(redAverage)
        self.redRangeValue.setNum(redRange)
        self.greenAverageValue.setNum(greenAverage)
        self.greenRangeValue.setNum(greenRange)
        self.blueAverageValue.setNum(blueAverage)
        self.blueRangeValue.setNum(blueRange)
        self.xValueText.setNum(xValue)
        self.yValueText.setNum(yValue)
        self.redValueText.setNum(redValue)
        self.greenValueText.setNum(greenValue)
        self.blueValueText.setNum(blueValue)
        self.commonColorValue.setNum(num)

        # Update the Slider Position
        self.redAverageSlider.setSliderPosition(redAverage)
        self.redRangeSlider.setSliderPosition(redRange)
        self.greenAverageSlider.setSliderPosition(greenAverage)
        self.greenRangeSlider.setSliderPosition(greenRange)
        self.blueAverageSlider.setSliderPosition(blueAverage)
        self.blueRangeSlider.setSliderPosition(blueRange)

        # Update the Preview Color 
        hexColor = '#'+'%02x%02x%02x' % (redValue, greenValue, blueValue)
        self.colorPreview.setStyleSheet(f'background-color: {hexColor}')
        
        # Run the functions
        self.colorDetect()
        self.showCommonColor()

    def colorDetect(self):
        """
        Calculate the min and max for RGB with Average and Range values.
        At the same time, if the user hits a limit, it will adjust to the max or min value.
        Also, when the user selects 128 for average value and range for 127, it will automatically switch min value to 0 even though it is techically 1
        Once the calculations are complete, it will trigger the color_detect function.
        
        Related Function:
            color_detect(redMin, redMax, greenMin, greenMax, blueMin, blueMax)
        """
        global redAverage, redRange, greenAverage, greenRange, blueAverage, blueRange
        
        redMin = redAverage - redRange
        if (redMin < 0) or (redAverage == 128 and redRange == 127):
            redMin = 0
        redMax = redAverage + redRange
        if (redMax > 255):
            redMax = 255
        greenMin = greenAverage - greenRange
        if (greenMin < 0) or (greenAverage == 128 and greenRange == 127):
            greenMin = 0
        greenMax = greenAverage + greenRange
        if (greenMax > 255):
            greenMax = 255
        blueMin = blueAverage - blueRange
        if (blueMin < 0) or (blueAverage == 128 and blueRange == 127):
            blueMin = 0
        blueMax = blueAverage + blueRange
        if (blueMax > 255):
            blueMax = 255

        self.color_detect(redMin, redMax, greenMin, greenMax, blueMin, blueMax)

    def color_detect(self, redMin, redMax, greenMin, greenMax, blueMin, blueMax):
        """
        Show the image color if the color is in the range that the user wants to see
        If it is not, it will show as (0,255,255): skyblue
        
        Args:
            redMin: Red Min value from Red Average - Red Range, Int
            redMax: Red Max value from Red Average + Red Range, Int
            greenMin: Green Min value from Green Average - Green Range, Int
            greenMax: Green Max value from Green Average + Green Range, Int
            blueMin: Blue Min value from Blue Average - Blue Range, Int
            blueMax: Blue Max value from Blue Average + Blue Range, Int
        
        """
        global pictures, index
        # Read the Image
        img = cv2.imread(pictures[index][1])

        # Set an Array from Numpy for Lower and Upper bounds
        Lower = np.array([blueMin, greenMin, redMin], dtype = "uint8")
        Upper = np.array([blueMax, greenMax, redMax], dtype = "uint8")
        
        # If the color pixel is in range, then remain the color, otherwise change it to black
        mask = cv2.inRange(img, Lower, Upper)
        output = cv2.bitwise_and(img, img, mask = mask)

        # Copy the result of the image
        newBackground = img.copy()

        # Change the background color (255,255,0)  == (B,G,R) for custom color
        newBackground[mask == 0] = (255,255,0)
        
        # Make the Image file for temporary
        cv2.imwrite("Detection.png", newBackground)
        fileName = "Detection.png"

        # Display the Image file on the GUI
        pixmap = QtGui.QPixmap(fileName)
        self.executeImgLbl.setPixmap(pixmap)
        self.executeImgLbl.setAlignment(QtCore.Qt.AlignLeft)

        # Remove the Image file
        os.remove("Detection.png")

    def captureIt(self, event):
        """
        This function will capture the RGB and x and y value for the Original Image and update the values as corresponding

        Args:
            event: event variable to capture the x and y values

        """
        global xValue, yValue, redValue, greenValue, blueValue, pictures, index
        # Get the x and y coordinates from the event input
        xValue = event.pos().x()
        yValue = event.pos().y()

        # Get the color as an list from PyQt5 dependency from the image path
        qImg = QtGui.QImage(pictures[index][1])
        c = qImg.pixel(xValue, yValue)
        colors = QtGui.QColor(c).getRgb()

        # Store the colors as global varialbes
        redValue = colors[0]
        greenValue = colors[1]
        blueValue = colors[2]

    def captureCommon(self, event):
        """
        Same idea with the captureIt function but instead it is for common color Image.
        Also, it will not remember the x and y value since it is not important.

        Args:
            event: event variable to capture the x and y values

        """
        global redAverage, blueAverage, greenAverage
        # Get the x and y coordinates from the event input
        xValue = event.pos().x()
        yValue = event.pos().y()

        # Get the color as an list from PyQt5 dependency from the common_colors
        qImg = QtGui.QImage("common\Common_Colors.png")
        c = qImg.pixel(xValue, yValue)
        colors = QtGui.QColor(c).getRgb()

        # Store the colors as global varialbes
        redAverage = colors[0]
        greenAverage = colors[1]
        blueAverage = colors[2]

    def showCommonColor(self):
        """
        Display the common colors for the image that is currently display.
        """
        global pictures, index, num
        # Create an empy list
        bars = []

        for i in range(num):
            # Create a bar and append it to the bars list
            bar = self.make_bar(pictures[index][2][i])
            bars.append(bar)

        # Make an image in a vertical stack of bars that was appened into the bars list
        img = np.vstack(bars)
        
        for j in range(num):
            # If the color is too dark (a.k.a black), display the text color as white, otherwise black
            if (pictures[index][2][j][0] <= 100) and (pictures[index][2][j][1] <= 100)  and (pictures[index][2][j][2] <= 100):
                textColor = (255, 255, 255)
            else:
                textColor = (0,0,0) 
            
            # Add the color code on the first line of each bar and Percentage of the color on the second line
            img = cv2.putText(img, str(pictures[index][2][j]), (5, 20 + (j * 160)), cv2.FONT_HERSHEY_TRIPLEX, 0.5, textColor, 1, cv2.LINE_AA)
            img = cv2.putText(img, str(pictures[index][3][j]) + "%", (5, 40 + (j * 160)), cv2.FONT_HERSHEY_TRIPLEX, 0.5, textColor, 1, cv2.LINE_AA)
        
        # If the folder common does not exists, create one
        if not os.path.exists('common'):
            os.makedirs('common')
        
        # Create an image file with the common color 
        cv2.imwrite("common\Common_Colors.png", img)
        fileName = "common\Common_Colors.png"

        # Display the common color on the GUI
        pixmap = QtGui.QPixmap(fileName)
        self.commonColorLbl.setPixmap(pixmap)
        self.commonColorLbl.setAlignment(QtCore.Qt.AlignLeft)

    def retranslateUi(self, MainWindow):
        """
        Replaces the name of the object when it displayes to the user

        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextBtn.setText(_translate("MainWindow", "Next"))
        self.previousBtn.setText(_translate("MainWindow", "Previous"))
        self.greenAverageText.setText(_translate("MainWindow", "Green Average"))
        self.greenRangeText.setText(_translate("MainWindow", "Green Range"))
        self.blueAverageText.setText(_translate("MainWindow", "Blue Average"))
        self.blueRangeText.setText(_translate("MainWindow", "Blue Range"))
        self.redRangeText.setText(_translate("MainWindow", "Red Range"))
        self.redAverageText.setText(_translate("MainWindow", "Red Average"))
        self.colorRangeText.setText(_translate("MainWindow", "Color Range Detection"))
        self.yText.setText(_translate("MainWindow", "Y"))
        self.xText.setText(_translate("MainWindow", "X"))
        self.colorPreviewText.setText(_translate("MainWindow", "Color Preview"))
        self.redText.setText(_translate("MainWindow", "Red"))
        self.greenText.setText(_translate("MainWindow", "Green"))
        self.blueText.setText(_translate("MainWindow", "Blue"))
        self.commonColorLbl.setText(_translate("MainWindow", "TextLabel"))
        self.author.setText(_translate("MainWindow", "By Kenneth Kang"))
        self.title.setText(_translate("MainWindow", "URSA 2020~2021 Explanable Computer Vision Settings"))

# Basic functions and statements to call the Main GUI to run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
