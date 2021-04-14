###########################################################################################################################
## Author: Kenneth Kang                                                                                                  ##
## Purpose: This program will be an updated version/modifed version from the previous lesson code with update list below ##
##                                                                                                                       ##
##      1. The user can see all the image without iterating each image                                                   ##
##      2. The user can change the range of RGB average and range value to be detected in the other image box.           ##
##          for all the images.                                                                                          ##
##          -- The skyblue background box indicates what the computer will see as                                        ##
##                                                                                                                       ##
## The full explaination of the course lecture can be found the following link                                           ##
## https://sites.google.com/view/edupixel/home                                                                           ##
##                                                                                                                       ##
## If you want to add your own images, then remove all images from the OG and images folder,                             ##
## and add images only inside the OG folder.                                                                             ##
##                                                                                                                       ##
## Dependencies: PyQt5, cv2, numpy, sklearn, pickle                                                                      ##
##                                                                                                                       ##
## Other software Usage: Designer.exe for PyQt5(That can be found in .ui file)                                           ##
###########################################################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import numpy as np
import cv2
from sklearn.cluster import KMeans
import pickle

# Global Variables
pictures = []
redAverage = 128
redRange = 15
greenAverage = 128
greenRange = 15
blueAverage = 128
blueRange = 15
num = 1
index = 0



class Ui_MainWindow(object):
    """
    This is the parent class of the two child classes for GUI
    In other words, this is the main GUI for this program
    """
    def setupUi(self, MainWindow):
        """
        Initializes the child GUI that only have a QLabel from PyQt5
        At the same time, it also link other functions to each object

        Independent Function:
            readFile: It will read the first 9 images inside the folder of OG

        Connected Functions:
            Format: Description
                Object Name: Function

            Timer: Set a timer for every 0.01 second to trigger updateValue function

            Slider: By changing the position of the slider will trigger certain function
                redAverageSlider: redAverageUpdate function
                redRangeSlider: redRangeUpdate function
                greenAverageSlider: greenAverageUpdate function
                greenRangeSlider: greenRangeUpdate function
                blueAverageSlider: blueAverageUpdate function
                blueRangeSlider: blueRangeUpdate function 
                commonColorSlider: commonColorNumUpdate function
            
            Mouse: By clicking certain location with the mouse, it will trigger certain function
                exImg1 and ogImg1: img1Select function
                exImg2 and ogImg2: img2Select function
                exImg3 and ogImg3: img3Select function
                exImg4 and ogImg4: img4Select function
                exImg5 and ogImg5: img5Select function
                exImg6 and ogImg6: img6Select function
                exImg7 and ogImg7: img7Select function
                exImg8 and ogImg8: img8Select function
                exImg9 and ogImg9: img9Select function
        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.ogImg1 = QtWidgets.QLabel(self.centralwidget)
        self.ogImg1.setGeometry(QtCore.QRect(20, 20, 150, 150))
        self.ogImg1.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImg1.setText("")
        self.ogImg1.setCursor(QtCore.Qt.PointingHandCursor)
        self.ogImg1.setObjectName("ogImg1")

        self.exImg1 = QtWidgets.QLabel(self.centralwidget)
        self.exImg1.setGeometry(QtCore.QRect(190, 20, 150, 150))
        self.exImg1.setFrameShape(QtWidgets.QFrame.Box)
        self.exImg1.setText("")
        self.exImg1.setObjectName("exImg1")

        self.ogImg2 = QtWidgets.QLabel(self.centralwidget)
        self.ogImg2.setGeometry(QtCore.QRect(380, 20, 150, 150))
        self.ogImg2.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImg2.setText("")
        self.ogImg2.setCursor(QtCore.Qt.PointingHandCursor)
        self.ogImg2.setObjectName("ogImg2")

        self.exImg2 = QtWidgets.QLabel(self.centralwidget)
        self.exImg2.setGeometry(QtCore.QRect(550, 20, 150, 150))
        self.exImg2.setFrameShape(QtWidgets.QFrame.Box)
        self.exImg2.setText("")
        self.exImg2.setObjectName("exImg2")

        self.ogImg3 = QtWidgets.QLabel(self.centralwidget)
        self.ogImg3.setGeometry(QtCore.QRect(740, 20, 150, 150))
        self.ogImg3.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImg3.setText("")
        self.ogImg3.setCursor(QtCore.Qt.PointingHandCursor)
        self.ogImg3.setObjectName("ogImg3")

        self.exImg3 = QtWidgets.QLabel(self.centralwidget)
        self.exImg3.setGeometry(QtCore.QRect(910, 20, 150, 150))
        self.exImg3.setFrameShape(QtWidgets.QFrame.Box)
        self.exImg3.setText("")
        self.exImg3.setObjectName("exImg3")

        self.ogImg4 = QtWidgets.QLabel(self.centralwidget)
        self.ogImg4.setGeometry(QtCore.QRect(20, 220, 150, 150))
        self.ogImg4.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImg4.setText("")
        self.ogImg4.setCursor(QtCore.Qt.PointingHandCursor)
        self.ogImg4.setObjectName("ogImg4")

        self.exImg4 = QtWidgets.QLabel(self.centralwidget)
        self.exImg4.setGeometry(QtCore.QRect(190, 220, 150, 150))
        self.exImg4.setFrameShape(QtWidgets.QFrame.Box)
        self.exImg4.setText("")
        self.exImg4.setObjectName("exImg4")

        self.ogImg5 = QtWidgets.QLabel(self.centralwidget)
        self.ogImg5.setGeometry(QtCore.QRect(380, 220, 150, 150))
        self.ogImg5.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImg5.setText("")
        self.ogImg5.setCursor(QtCore.Qt.PointingHandCursor)
        self.ogImg5.setObjectName("ogImg5")

        self.exImg5 = QtWidgets.QLabel(self.centralwidget)
        self.exImg5.setGeometry(QtCore.QRect(550, 220, 150, 150))
        self.exImg5.setFrameShape(QtWidgets.QFrame.Box)
        self.exImg5.setText("")
        self.exImg5.setObjectName("exImg5")

        self.ogImg6 = QtWidgets.QLabel(self.centralwidget)
        self.ogImg6.setGeometry(QtCore.QRect(740, 220, 150, 150))
        self.ogImg6.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImg6.setText("")
        self.ogImg6.setCursor(QtCore.Qt.PointingHandCursor)
        self.ogImg6.setObjectName("ogImg6")

        self.exImg6 = QtWidgets.QLabel(self.centralwidget)
        self.exImg6.setGeometry(QtCore.QRect(910, 220, 150, 150))
        self.exImg6.setFrameShape(QtWidgets.QFrame.Box)
        self.exImg6.setText("")
        self.exImg6.setObjectName("exImg6")

        self.ogImg9 = QtWidgets.QLabel(self.centralwidget)
        self.ogImg9.setGeometry(QtCore.QRect(740, 420, 150, 150))
        self.ogImg9.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImg9.setText("")
        self.ogImg9.setCursor(QtCore.Qt.PointingHandCursor)
        self.ogImg9.setObjectName("ogImg9")

        self.ogImg8 = QtWidgets.QLabel(self.centralwidget)
        self.ogImg8.setGeometry(QtCore.QRect(380, 420, 150, 150))
        self.ogImg8.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImg8.setText("")
        self.ogImg8.setCursor(QtCore.Qt.PointingHandCursor)
        self.ogImg8.setObjectName("ogImg8")

        self.exImg9 = QtWidgets.QLabel(self.centralwidget)
        self.exImg9.setGeometry(QtCore.QRect(910, 420, 150, 150))
        self.exImg9.setFrameShape(QtWidgets.QFrame.Box)
        self.exImg9.setText("")
        self.exImg9.setObjectName("exImg9")

        self.ogImg7 = QtWidgets.QLabel(self.centralwidget)
        self.ogImg7.setGeometry(QtCore.QRect(20, 420, 150, 150))
        self.ogImg7.setFrameShape(QtWidgets.QFrame.Box)
        self.ogImg7.setText("")
        self.ogImg7.setCursor(QtCore.Qt.PointingHandCursor)
        self.ogImg7.setObjectName("ogImg7")

        self.exImg7 = QtWidgets.QLabel(self.centralwidget)
        self.exImg7.setGeometry(QtCore.QRect(190, 420, 150, 150))
        self.exImg7.setFrameShape(QtWidgets.QFrame.Box)
        self.exImg7.setText("")
        self.exImg7.setObjectName("exImg7")

        self.exImg8 = QtWidgets.QLabel(self.centralwidget)
        self.exImg8.setGeometry(QtCore.QRect(550, 420, 150, 150))
        self.exImg8.setFrameShape(QtWidgets.QFrame.Box)
        self.exImg8.setText("")
        self.exImg8.setObjectName("exImg8")

        self.commonColorLbl = QtWidgets.QLabel(self.centralwidget)
        self.commonColorLbl.setGeometry(QtCore.QRect(20, 610, 800, 150))
        self.commonColorLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.commonColorLbl.setText("")
        self.commonColorLbl.setObjectName("commonColorLbl")

        self.commonColorSlider = QtWidgets.QSlider(self.centralwidget)
        self.commonColorSlider.setGeometry(QtCore.QRect(840, 670, 160, 22))
        self.commonColorSlider.setMinimum(1)
        self.commonColorSlider.setMaximum(5)
        self.commonColorSlider.setOrientation(QtCore.Qt.Horizontal)
        self.commonColorSlider.setObjectName("commonColorSlider")

        self.commonColorValue = QtWidgets.QLabel(self.centralwidget)
        self.commonColorValue.setGeometry(QtCore.QRect(1020, 670, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.commonColorValue.setFont(font)
        self.commonColorValue.setFrameShape(QtWidgets.QFrame.Box)
        self.commonColorValue.setText("")
        self.commonColorValue.setAlignment(QtCore.Qt.AlignCenter)
        self.commonColorValue.setObjectName("commonColorValue")

        self.redAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.redAverageValue.setGeometry(QtCore.QRect(280, 810, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redAverageValue.setFont(font)
        self.redAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redAverageValue.setText("")
        self.redAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redAverageValue.setObjectName("redAverageValue")

        self.redRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.redRangeValue.setGeometry(QtCore.QRect(280, 890, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.redRangeValue.setFont(font)
        self.redRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.redRangeValue.setText("")
        self.redRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.redRangeValue.setObjectName("redRangeValue")

        self.redAverageText = QtWidgets.QLabel(self.centralwidget)
        self.redAverageText.setGeometry(QtCore.QRect(100, 780, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redAverageText.setFont(font)
        self.redAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.redAverageText.setObjectName("redAverageText")

        self.redAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.redAverageSlider.setGeometry(QtCore.QRect(20, 810, 241, 22))
        self.redAverageSlider.setMaximum(255)
        self.redAverageSlider.setSliderPosition(128)
        self.redAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redAverageSlider.setObjectName("redAverageSlider")

        self.redRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.redRangeSlider.setGeometry(QtCore.QRect(20, 890, 241, 22))
        self.redRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.redRangeSlider.setMaximum(127)
        self.redRangeSlider.setProperty("value", 0)
        self.redRangeSlider.setSliderPosition(0)
        self.redRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redRangeSlider.setObjectName("redRangeSlider")

        self.redRangeText = QtWidgets.QLabel(self.centralwidget)
        self.redRangeText.setGeometry(QtCore.QRect(90, 860, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.redRangeText.setFont(font)
        self.redRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.redRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.redRangeText.setObjectName("redRangeText")

        self.greenRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.greenRangeValue.setGeometry(QtCore.QRect(630, 888, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenRangeValue.setFont(font)
        self.greenRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenRangeValue.setText("")
        self.greenRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenRangeValue.setObjectName("greenRangeValue")

        self.greenAverageText = QtWidgets.QLabel(self.centralwidget)
        self.greenAverageText.setGeometry(QtCore.QRect(430, 778, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.greenAverageText.setFont(font)
        self.greenAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.greenAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenAverageText.setObjectName("greenAverageText")

        self.greenAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.greenAverageValue.setGeometry(QtCore.QRect(630, 810, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.greenAverageValue.setFont(font)
        self.greenAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.greenAverageValue.setText("")
        self.greenAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.greenAverageValue.setObjectName("greenAverageValue")

        self.greenRangeText = QtWidgets.QLabel(self.centralwidget)
        self.greenRangeText.setGeometry(QtCore.QRect(440, 858, 100, 20))
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
        self.greenAverageSlider.setGeometry(QtCore.QRect(370, 810, 241, 22))
        self.greenAverageSlider.setMaximum(255)
        self.greenAverageSlider.setProperty("value", 128)
        self.greenAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenAverageSlider.setObjectName("greenAverageSlider")

        self.greenRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenRangeSlider.setGeometry(QtCore.QRect(370, 890, 241, 20))
        self.greenRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.greenRangeSlider.setMaximum(127)
        self.greenRangeSlider.setProperty("value", 0)
        self.greenRangeSlider.setSliderPosition(0)
        self.greenRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenRangeSlider.setObjectName("greenRangeSlider")

        self.blueAverageValue = QtWidgets.QLabel(self.centralwidget)
        self.blueAverageValue.setGeometry(QtCore.QRect(970, 810, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueAverageValue.setFont(font)
        self.blueAverageValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueAverageValue.setText("")
        self.blueAverageValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueAverageValue.setObjectName("blueAverageValue")

        self.blueRangeSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueRangeSlider.setGeometry(QtCore.QRect(710, 890, 241, 22))
        self.blueRangeSlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.blueRangeSlider.setMaximum(127)
        self.blueRangeSlider.setSliderPosition(0)
        self.blueRangeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueRangeSlider.setObjectName("blueRangeSlider")

        self.blueAverageSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueAverageSlider.setGeometry(QtCore.QRect(710, 810, 241, 22))
        self.blueAverageSlider.setMaximum(255)
        self.blueAverageSlider.setProperty("value", 128)
        self.blueAverageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueAverageSlider.setObjectName("blueAverageSlider")

        self.blueRangeText = QtWidgets.QLabel(self.centralwidget)
        self.blueRangeText.setGeometry(QtCore.QRect(780, 860, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueRangeText.setFont(font)
        self.blueRangeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueRangeText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueRangeText.setObjectName("blueRangeText")

        self.blueRangeValue = QtWidgets.QLabel(self.centralwidget)
        self.blueRangeValue.setGeometry(QtCore.QRect(970, 890, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.blueRangeValue.setFont(font)
        self.blueRangeValue.setFrameShape(QtWidgets.QFrame.Box)
        self.blueRangeValue.setText("")
        self.blueRangeValue.setAlignment(QtCore.Qt.AlignCenter)
        self.blueRangeValue.setObjectName("blueRangeValue")

        self.blueAverageText = QtWidgets.QLabel(self.centralwidget)
        self.blueAverageText.setGeometry(QtCore.QRect(780, 780, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.blueAverageText.setFont(font)
        self.blueAverageText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.blueAverageText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueAverageText.setObjectName("blueAverageText")

        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setGeometry(QtCore.QRect(1000, 920, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.author.setFont(font)
        self.author.setObjectName("author")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.timer = QtCore.QTimer()

        self.readFile()

        # Timer
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        # Mouse
        self.commonColorLbl.mousePressEvent = self.captureCommon
        
        self.exImg1.mousePressEvent = self.img1Select
        self.ogImg1.mousePressEvent = self.img1Select

        self.exImg2.mousePressEvent = self.img2Select
        self.ogImg2.mousePressEvent = self.img2Select

        self.exImg3.mousePressEvent = self.img3Select
        self.ogImg3.mousePressEvent = self.img3Select

        self.exImg4.mousePressEvent = self.img4Select
        self.ogImg4.mousePressEvent = self.img4Select

        self.exImg5.mousePressEvent = self.img5Select
        self.ogImg5.mousePressEvent = self.img5Select

        self.exImg6.mousePressEvent = self.img6Select
        self.ogImg6.mousePressEvent = self.img6Select

        self.exImg7.mousePressEvent = self.img7Select
        self.ogImg7.mousePressEvent = self.img7Select

        self.exImg8.mousePressEvent = self.img8Select
        self.ogImg8.mousePressEvent = self.img8Select

        self.exImg9.mousePressEvent = self.img9Select
        self.ogImg9.mousePressEvent = self.img9Select

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
        ogObjects = [self.ogImg1, self.ogImg2, self.ogImg3, self.ogImg4, self.ogImg5, self.ogImg6, self.ogImg7, self.ogImg8, self.ogImg9]
        path = os.path.abspath(os.getcwd()) + "\OG"

        # If these folder/file do not exists, create one
        if not os.path.exists('images'):
            os.makedirs('images')
        if not os.path.exists('Pic.pickle'):
            f = open("Pic.pickle", "x")
            new = True
        elif os.path.getsize('Pic.pickle') == 0:
            f = open("Pic.pickle", "w")
            new = True
        else:
        # if the file exists, open it and call the data 
            old_file = open("Pic.pickle", 'rb')
            pictures = pickle.load(old_file)
            old_file.close()

        for i, filename in enumerate(os.listdir(path)):
            # only run first cold start with no data
            if new:
                img = cv2.imread(os.path.join(path, filename))
                imgPath = os.path.abspath(os.getcwd()) + f"\images\{filename + str(i)}.png"
                dsize = (150,150)
                output = cv2.resize(img, dsize)
                cv2.imwrite(imgPath, output)
                pictures.append([])
                pictures[i].append(os.path.join(path, filename))
                pictures[i].append(imgPath)
                self.analyzeColor(imgPath, i)


        # Save the updated data into pickle
        old_file = open("Pic.pickle", 'wb')
        pickle.dump(pictures, old_file)
        old_file.close()

        for j in range (9):
            pixmap = QtGui.QPixmap(pictures[j][1])
            self.widget = ogObjects[j]
            self.widget.setPixmap(pixmap)
            self.widget.setAlignment(QtCore.Qt.AlignLeft)

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
        
        global redAverage, redRange, greenAverage, greenRange, blueAverage, blueRange, num, index

        # Update the Text Value
        self.redAverageValue.setNum(redAverage)
        self.redRangeValue.setNum(redRange)
        self.greenAverageValue.setNum(greenAverage)
        self.greenRangeValue.setNum(greenRange)
        self.blueAverageValue.setNum(blueAverage)
        self.blueRangeValue.setNum(blueRange)
        self.commonColorValue.setNum(num)

        # Update the Slider Position
        self.redAverageSlider.setSliderPosition(redAverage)
        self.redRangeSlider.setSliderPosition(redRange)
        self.greenAverageSlider.setSliderPosition(greenAverage)
        self.greenRangeSlider.setSliderPosition(greenRange)
        self.blueAverageSlider.setSliderPosition(blueAverage)
        self.blueRangeSlider.setSliderPosition(blueRange)

        self.colorDetect()
        self.showCommonColor(index)
        


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


    def make_bar(self, color):
        """
        Create an image of a given color

        Args:
            color: BRG pixel values of the color from cv2, (B, G, R)

        Returns:
            tuple of bar, rgb values, and hsv values
        """
        bar = np.zeros((150, 160, 3), np.uint8)
        bar[:] = [color[2], color[1], color[0]]
        return bar

    def img1Select(self, event):
        """
        This function will update the value of index when the function is triggered
        """
        global index
        index = 0

    def img2Select(self, event):
        """
        This function will update the value of index when the function is triggered
        """
        global index
        index = 1

    def img3Select(self, event):
        """
        This function will update the value of index when the function is triggered
        """
        global index
        index = 2

    def img4Select(self, event):
        """
        This function will update the value of index when the function is triggered
        """
        global index
        index = 3

    def img5Select(self, event):
        """
        This function will update the value of index when the function is triggered
        """
        global index
        index = 4

    def img6Select(self, event):
        """
        This function will update the value of index when the function is triggered
        """
        global index
        index = 5

    def img7Select(self, event):
        """
        This function will update the value of index when the function is triggered
        """
        global index
        index = 6

    def img8Select(self, event):
        """
        This function will update the value of index when the function is triggered
        """
        global index
        index = 7

    def img9Select(self, event):
        """
        This function will update the value of index when the function is triggered
        """
        global index
        index = 8


    def showCommonColor(self, index):
        """
        Display the common colors for the image that is currently display.
        """
        global pictures, num
        # Create an empy list
        bars = []

        for i in range(num):
            # Create a bar and append it to the bars list
            bar = self.make_bar(pictures[index][2][i])
            bars.append(bar)

        # Make an image in a vertical stack of bars that was appened into the bars list
        img = np.hstack(bars)
        
        for j in range(num):
            # If the color is too dark (a.k.a black), display the text color as white, otherwise black
            if (pictures[index][2][j][0] <= 100) and (pictures[index][2][j][1] <= 100)  and (pictures[index][2][j][2] <= 100):
                textColor = (255, 255, 255)
            else:
                textColor = (0,0,0) 
            
            # Add the color code on the first line of each bar and Percentage of the color on the second line
            img = cv2.putText(img, str(pictures[index][2][j]), (5 + (j * 160), 20), cv2.FONT_HERSHEY_TRIPLEX, 0.5, textColor, 1, cv2.LINE_AA)
            img = cv2.putText(img, str(pictures[index][3][j]) + "%", (5+ (j * 160) , 40 ), cv2.FONT_HERSHEY_TRIPLEX, 0.5, textColor, 1, cv2.LINE_AA)
        
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
        global pictures
        exObjects = [self.exImg1, self.exImg2, self.exImg3, self.exImg4, self.exImg5, self.exImg6, self.exImg7, self.exImg8, self.exImg9]
        for i in range (9):
        # Read the Image
            img = cv2.imread(pictures[i][1])

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
            self.executeImgLbl = exObjects[i]
            self.executeImgLbl.setPixmap(pixmap)
            self.executeImgLbl.setAlignment(QtCore.Qt.AlignLeft)

        # Remove the Image file
            os.remove("Detection.png")


    def retranslateUi(self, MainWindow):
        """
        Replaces the name of the object when it displayes to the user

        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lesson 4"))
        self.redAverageText.setText(_translate("MainWindow", "Red Average"))
        self.redRangeText.setText(_translate("MainWindow", "Red Range"))
        self.greenAverageText.setText(_translate("MainWindow", "Green Average"))
        self.greenRangeText.setText(_translate("MainWindow", "Green Range"))
        self.blueRangeText.setText(_translate("MainWindow", "Blue Range"))
        self.blueAverageText.setText(_translate("MainWindow", "Blue Average"))
        self.author.setText(_translate("MainWindow", "By Kenneth Kang"))

# Basic functions and statements to call the Main GUI to run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())