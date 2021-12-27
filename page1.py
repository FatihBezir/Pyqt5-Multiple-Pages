from PyQt5 import QtCore, QtWidgets
import main

class Ui_Page1(object):
    def setupUi(self, Page1):
        Page1.setObjectName("Page1")
        Page1.resize(291, 122)
        self.centralwidget = QtWidgets.QWidget(Page1)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        Page1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Page1)
        QtCore.QMetaObject.connectSlotsByName(Page1)

    def retranslateUi(self, Page1):
        _translate = QtCore.QCoreApplication.translate
        Page1.setWindowTitle(_translate("Page1", "Page1"))
        self.pushButton.setText(_translate("Page1", "Page2 Show"))
        self.pushButton.clicked.connect(lambda:self.showP2())

    def fillElements(self):
        self.pushButton.setText(("P2 SHOW"))

    def showP2(self):
        main.a(2)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Page1 = QtWidgets.QMainWindow()
#     ui = Ui_Page1()
#     ui.setupUi(Page1)
#     Page1.show()
#     sys.exit(app.exec_())