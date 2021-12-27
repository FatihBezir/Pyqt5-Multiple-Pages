from PyQt5 import QtCore, QtWidgets
import main

class Ui_Page2(object):
    def setupUi(self, Page2):
        Page2.setObjectName("Page2")
        Page2.resize(291, 122)
        self.centralwidget = QtWidgets.QWidget(Page2)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        Page2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Page2)
        QtCore.QMetaObject.connectSlotsByName(Page2)

    def retranslateUi(self, Page2):
        _translate = QtCore.QCoreApplication.translate
        Page2.setWindowTitle(_translate("Page2", "Page2"))
        self.pushButton.setText(_translate("Page2", "Page1 Show"))
        self.pushButton.clicked.connect(lambda:self.showP1())

    def fillElements(self):
        self.pushButton.setText(("P1 SHOW"))

    def showP1(self):
        main.a(1)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Page2 = QtWidgets.QMainWindow()
#     ui = Ui_Page2()
#     ui.setupUi(Page2)
#     Page2.show()
#     sys.exit(app.exec_())