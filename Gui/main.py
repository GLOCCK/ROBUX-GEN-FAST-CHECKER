from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
import sys


class mainWindow(QDialog):
    def __init__(self):
        super(mainWindow, self).__init__()
        loadUi("main.ui", self)
        self.genButton.clicked.connect(self.gotoGen)
        self.checkerButton.clicked.connect(self.gotoChecker)
        self.creditsButton.clicked.connect(self.gotoCredits)

    def gotoGen(self):
        gen = genWindow()
        widget.addWidget(gen)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoChecker(self):
        checker = checkerWindow()
        widget.addWidget(checker)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoCredits(self):
        credits = creditWindow()
        widget.addWidget(credits)
        widget.setCurrentIndex(widget.currentIndex()+1)


class genWindow(QDialog):
    def __init__(self):
        super(genWindow, self).__init__()
        loadUi("gen.ui", self)
        self.startButton.clicked.connect(self.start)
        self.returnButton.clicked.connect(self.gotoMain)

    def start(self):
        pass

    def gotoMain(self):
        main = mainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


class checkerWindow(QDialog):
    def __init__(self):
        super(checkerWindow, self).__init__()
        loadUi("checker.ui", self)
        self.returnButton.clicked.connect(self.gotoMain)

    def gotoMain(self):
        main = mainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


class creditWindow(QDialog):
    def __init__(self):
        super(creditWindow, self).__init__()
        loadUi("credits.ui", self)
        self.returnButton.clicked.connect(self.gotoMain)

    def gotoMain(self):
        main = mainWindow()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


app = QApplication(sys.argv)
main = mainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(main)
widget.setFixedHeight(490)
widget.setFixedWidth(425)
widget.show()

try:
    sys.exit(app.exec_())
except:
    pass
