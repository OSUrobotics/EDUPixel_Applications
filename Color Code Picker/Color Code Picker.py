# https://realpython.com/documenting-python-code/  Need to Document the entire code when I complete it

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.redText.setText(_translate("MainWindow", "Red"))
        self.imgSelectBtn.setText(_translate("MainWindow", "Select Image"))
        self.changeColorBtn.setText(_translate("MainWindow", "Change Color"))
        self.xText.setText(_translate("MainWindow", "X"))
        self.yText.setText(_translate("MainWindow", "Y"))
        self.greenText.setText(_translate("MainWindow", "Green"))
        self.blueText.setText(_translate("MainWindow", "Blue"))
        self.colorPreviewText.setText(_translate("MainWindow", "Color Preview"))
        self.authorText.setText(_translate("MainWindow", "By Kenneth Kang"))
    

    def setImage(self):
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
        self.redValue = value
        self.redValueText.setNum(value)
        hexColor = '#'+'%02x%02x%02x' % (value, self.greenValue, self.blueValue)
        self.colorPreview.setStyleSheet(f'background-color: {hexColor}')

    def colorChangeGreen(self, value):
        self.greenValue = value
        self.greenValueText.setNum(value)
        hexColor = '#'+'%02x%02x%02x' % (self.redValue, value, self.blueValue)
        self.colorPreview.setStyleSheet(f'background-color: {hexColor}')

    def colorChangeBlue(self, value):
        self.blueValue = value
        self.blueValueText.setNum(value)
        hexColor = '#'+'%02x%02x%02x' % (self.redValue, self.greenValue, value)
        self.colorPreview.setStyleSheet(f'background-color: {hexColor}')

    def captureIt(self, event):
        self.xValue = event.pos().x()
        self.yValue = event.pos().y()
        self.xValueText.setNum(self.xValue)
        self.yValueText.setNum(self.yValue)
        # Must need a filepath before you click something on the label
        # TODO: Need some help from Sogol for programming aspect
        qImg = QtGui.QImage(self.filePath)
        c = qImg.pixel(self.xValue, self.yValue)
        colors = QtGui.QColor(c).getRgb()
        self.redValue = colors[0]
        self.blueValue = colors[1]
        self.greenValue = colors[2]
        self.redValueText.setNum(self.redValue)
        self.redSlider.setSliderPosition(self.redValue)
        self.greenValueText.setNum(self.greenValue)
        self.greenSlider.setSliderPosition(self.greenValue)
        self.blueValueText.setNum(self.blueValue)
        self.blueSlider.setSliderPosition(self.blueValue)
        hexColor = '#'+'%02x%02x%02x' % (self.redValue, self.greenValue, self.blueValue)
        self.colorPreview.setStyleSheet(f'background-color: {hexColor}')

    def changePixel(self):
        newImg = cv2.imread(self.filePath)
        newImg[self.yValue: self.yValue+10, self.xValue: self.xValue+5] = (self.blueValue, self.greenValue, self.redValue)
        newImg[self.yValue: self.yValue+10, self.xValue-5: self.xValue] = (self.blueValue, self.greenValue, self.redValue)
        cv2.imwrite("NewImage.png", newImg)
        fileName = "NewImage.png"
        pixmap = QtGui.QPixmap(fileName) # Setup pixmap with the provided image
        self.imgLbl.setPixmap(pixmap) # Set the pixmap onto the label
        self.imgLbl.setAlignment(QtCore.Qt.AlignLeft)

        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
