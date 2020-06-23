import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton

app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle('URSA 2020 Explaniable Vision')
window.setGeometry(2000,2000,2000,2000)
# How to do full Screen Mode
window.move(50,50)




window.show()

sys.exit(app.exec_())