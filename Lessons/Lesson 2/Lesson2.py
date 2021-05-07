###########################################################################################################################
## Author: Kenneth Kang                                                                                                  ##
## Purpose: This program will do the following task below.                                                               ##
##                                                                                                                       ##
##      1. The user can select any pictures in their machine to play around with.                                        ##
##      2. The user can select any location/pixel on the image and see the RGB, x location, and y location values.       ##
##      3. The user can modify the color by moving the slider of RGB and selcting Change Color.                          ##
##          -- The modified photo will be saved in the folder where this code is located as NewImage.png                 ##
##                                                                                                                       ##
## The full explaination of the course lecture can be found the following link                                           ##
## https://sites.google.com/view/edupixel/home                                                                           ##
##                                                                                                                       ##
## Dependencies: PyQt5, cv2                                                                                              ##
##                                                                                                                       ##
## Other software Usage: Designer.exe for PyQt5(That can be found in .ui file)                                           ##
###########################################################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


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
               imgSelectBtn: setImage function
               changeColorBtn: changePixel

            Slider: By changing the position of the slider will trigger certain function
                redSlider: colorChangeRed function
                greenSlider: colorChangeGreen function
                blueSlider: colorChangeBlue function
            
            Mouse: By clicking certain location with the mouse, it will trigger certain function
                imgLbl event: captureIt function
        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        # Global Variables        
        self.filePath = "No_Path"
        self.xValue = 0
        self.yValue = 0
        self.redValue = 0
        self.greenValue = 0
        self.blueValue = 0
 

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1218, 876)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.imgLbl = QtWidgets.QLabel(self.centralwidget)
        self.imgLbl.setGeometry(QtCore.QRect(10, 10, 1200, 675))
        self.imgLbl.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLbl.setCursor(QtCore.Qt.CrossCursor)
        self.imgLbl.setObjectName("imgLbl")

        self.xValueText = QtWidgets.QLabel(self.centralwidget)
        self.xValueText.setGeometry(QtCore.QRect(40, 750, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.xValueText.setFont(font)
        self.xValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.xValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.xValueText.setObjectName("xValueText")

        self.yValueText = QtWidgets.QLabel(self.centralwidget)
        self.yValueText.setGeometry(QtCore.QRect(40, 830, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.yValueText.setFont(font)
        self.yValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.yValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.yValueText.setObjectName("yValueText")

        self.redSlider = QtWidgets.QSlider(self.centralwidget)
        self.redSlider.setGeometry(QtCore.QRect(240, 720, 510, 22))
        self.redSlider.setMaximum(255)
        self.redSlider.setOrientation(QtCore.Qt.Horizontal)
        self.redSlider.setObjectName("redSlider")

        self.redText = QtWidgets.QLabel(self.centralwidget)
        self.redText.setGeometry(QtCore.QRect(170, 720, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.redText.setFont(font)
        self.redText.setAlignment(QtCore.Qt.AlignCenter)
        self.redText.setObjectName("redText")

        self.imgSelectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.imgSelectBtn.setGeometry(QtCore.QRect(1050, 730, 130, 35))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.imgSelectBtn.setFont(font)
        self.imgSelectBtn.setObjectName("imgSelectBtn")

        self.changeColorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.changeColorBtn.setGeometry(QtCore.QRect(850, 810, 130, 35))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.changeColorBtn.setFont(font)
        self.changeColorBtn.setObjectName("changeColorBtn")

        self.xText = QtWidgets.QLabel(self.centralwidget)
        self.xText.setGeometry(QtCore.QRect(40, 710, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.xText.setFont(font)
        self.xText.setAlignment(QtCore.Qt.AlignCenter)
        self.xText.setObjectName("xText")

        self.yText = QtWidgets.QLabel(self.centralwidget)
        self.yText.setGeometry(QtCore.QRect(40, 790, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.yText.setFont(font)
        self.yText.setAlignment(QtCore.Qt.AlignCenter)
        self.yText.setObjectName("yText")

        self.greenText = QtWidgets.QLabel(self.centralwidget)
        self.greenText.setGeometry(QtCore.QRect(170, 770, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.greenText.setFont(font)
        self.greenText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenText.setObjectName("greenText")

        self.blueText = QtWidgets.QLabel(self.centralwidget)
        self.blueText.setGeometry(QtCore.QRect(170, 820, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.blueText.setFont(font)
        self.blueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueText.setObjectName("blueText")

        self.greenSlider = QtWidgets.QSlider(self.centralwidget)
        self.greenSlider.setGeometry(QtCore.QRect(240, 770, 510, 22))
        self.greenSlider.setMaximum(255)
        self.greenSlider.setOrientation(QtCore.Qt.Horizontal)
        self.greenSlider.setObjectName("greenSlider")

        self.blueSlider = QtWidgets.QSlider(self.centralwidget)
        self.blueSlider.setGeometry(QtCore.QRect(240, 820, 510, 22))
        self.blueSlider.setMaximum(255)
        self.blueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.blueSlider.setObjectName("blueSlider")

        self.redValueText = QtWidgets.QLabel(self.centralwidget)
        self.redValueText.setGeometry(QtCore.QRect(760, 720, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.redValueText.setFont(font)
        self.redValueText.setNum(0)
        self.redValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.redValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.redValueText.setObjectName("redValueText")

        self.greenValueText = QtWidgets.QLabel(self.centralwidget)
        self.greenValueText.setGeometry(QtCore.QRect(760, 770, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.greenValueText.setFont(font)
        self.greenValueText.setNum(0)
        self.greenValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.greenValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.greenValueText.setObjectName("greenValueText")

        self.blueValueText = QtWidgets.QLabel(self.centralwidget)
        self.blueValueText.setGeometry(QtCore.QRect(760, 820, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.blueValueText.setFont(font)
        self.blueValueText.setNum(0)
        self.blueValueText.setFrameShape(QtWidgets.QFrame.Box)
        self.blueValueText.setAlignment(QtCore.Qt.AlignCenter)
        self.blueValueText.setObjectName("blueValueText")

        self.colorPreviewText = QtWidgets.QLabel(self.centralwidget)
        self.colorPreviewText.setGeometry(QtCore.QRect(850, 720, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.colorPreviewText.setFont(font)
        self.colorPreviewText.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreviewText.setObjectName("colorPreviewText")

        self.colorPreview = QtWidgets.QLabel(self.centralwidget)
        self.colorPreview.setGeometry(QtCore.QRect(850, 750, 130, 50))
        self.colorPreview.setFrameShape(QtWidgets.QFrame.Box)
        self.colorPreview.setAlignment(QtCore.Qt.AlignCenter)
        self.colorPreview.setObjectName("colorPreview")

        self.authorText = QtWidgets.QLabel(self.centralwidget)
        self.authorText.setGeometry(QtCore.QRect(1130, 850, 81, 16))
        self.authorText.setObjectName("authorText")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()

        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        # Sliders
        self.redSlider.valueChanged[int].connect(self.colorChangeRed)
        self.greenSlider.valueChanged[int].connect(self.colorChangeGreen)
        self.blueSlider.valueChanged[int].connect(self.colorChangeBlue)

        # Buttons
        self.imgSelectBtn.clicked.connect(self.setImage)
        self.changeColorBtn.clicked.connect(self.changePixel)

        # Mouse Event
        self.imgLbl.mousePressEvent = self.captureIt


    def retranslateUi(self, MainWindow):
        """
        Replaces the name of the object when it displayes to the user

        Args:
            MainWindow: The whole GUI that contains the Widget
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lesson 2"))
        self.redText.setText(_translate("MainWindow", "Red"))
        self.imgSelectBtn.setText(_translate("MainWindow", "Select Image"))
        self.changeColorBtn.setText(_translate("MainWindow", "Change Color"))
        self.xText.setText(_translate("MainWindow", "X"))
        self.yText.setText(_translate("MainWindow", "Y"))
        self.greenText.setText(_translate("MainWindow", "Green"))
        self.blueText.setText(_translate("MainWindow", "Blue"))
        self.colorPreviewText.setText(_translate("MainWindow", "Color Preview"))

    def update(self):
        """
        This function will be (almost) continuously running when the GUI is up.
        When the user change any values, it will automatically update text value or functions that uses those values.
        Or it will update the preview color when the user select certain location on an image.
        """
        self.redValueText.setNum(self.redValue)
        self.redSlider.setSliderPosition(self.redValue)
        self.greenValueText.setNum(self.greenValue)
        self.greenSlider.setSliderPosition(self.greenValue)
        self.blueValueText.setNum(self.blueValue)
        self.blueSlider.setSliderPosition(self.blueValue)
        hexColor = '#'+'%02x%02x%02x' % (self.redValue, self.greenValue, self.blueValue)
        self.colorPreview.setStyleSheet(f'background-color: {hexColor}')
    

    def setImage(self):
        """
        Let the user select an image to work around with. This will open an image select pop-up.
        """
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)") # Ask for file
        if (fileName):
            newImg = cv2.imread(fileName)
            dsize = (1200, 675)
            output = cv2.resize(newImg, dsize)
            cv2.imwrite("NewImage.png", output)
            self.filePath = "NewImage.png"
            fileName = "NewImage.png"
            pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
            self.imgLbl.setPixmap(pixmap) # Set the pixmap onto the label
            self.imgLbl.setAlignment(QtCore.Qt.AlignLeft)


    def colorChangeRed(self, value):
        """
        Change the value of Red when the user move the Red Slider.
        
        Args:
            Value: The red slider current location.
        """
        self.redValue = value
        self.redValueText.setNum(value)

    def colorChangeGreen(self, value):
        """
        Change the value of Green when the user move the Green Slider.
        
        Args:
            Value: The green slider current location.
        """
        self.greenValue = value
        self.greenValueText.setNum(value)

    def colorChangeBlue(self, value):
        """
        Change the value of Blue when the user move the Blue Slider.
        
        Args:
            Value: The blue slider current location.
        """
        self.blueValue = value
        self.blueValueText.setNum(value)

    def captureIt(self, event):
        """
        Update the values of color and location when the user select a certain location of the image.
        
        Args:
            event: capture the x, y, and RGB value of that pixel location.

        """
        self.xValue = event.pos().x()
        self.yValue = event.pos().y()
        self.xValueText.setNum(self.xValue)
        self.yValueText.setNum(self.yValue)
        if self.filePath != "NewImage.png":
            self.error()
        else:
            qImg = QtGui.QImage(self.filePath)
            c = qImg.pixel(self.xValue, self.yValue)
            colors = QtGui.QColor(c).getRgb()
            self.redValue = colors[0]
            self.greenValue = colors[1]
            self.blueValue = colors[2]
            

    def changePixel(self):
        """
        Change the pixel color from user RGB value selection.
        Rather than changing one pixel, it will change 100 pixels (10 by 10) so that it is easily viewed.
        Unless if the location has been selected at the edge, so it will change a different size.
        """
        newImg = cv2.imread(self.filePath)
        newImg[self.yValue: self.yValue+5, self.xValue: self.xValue+5] = (self.blueValue, self.greenValue, self.redValue)
        newImg[self.yValue: self.yValue+5, self.xValue-5: self.xValue] = (self.blueValue, self.greenValue, self.redValue)
        newImg[self.yValue-5: self.yValue, self.xValue: self.xValue+5] = (self.blueValue, self.greenValue, self.redValue)
        newImg[self.yValue-5: self.yValue, self.xValue-5: self.xValue] = (self.blueValue, self.greenValue, self.redValue)
        cv2.imwrite("NewImage.png", newImg)
        fileName = "NewImage.png"
        pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
        self.imgLbl.setPixmap(pixmap) # Set the pixmap onto the label
        self.imgLbl.setAlignment(QtCore.Qt.AlignLeft)

    def error(self):
        """
        This function will be triggered if the user reach the end of the list of images
        """
        errorMessage = QtWidgets.QMessageBox()
        errorMessage.setWindowTitle("Error")
        errorMessage.setText("No Image selected")
        errorMessage.setIcon(QtWidgets.QMessageBox.Critical)
        x = errorMessage.exec_()

        

# Basic functions and statements to call the Main GUI to run
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
