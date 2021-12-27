import os, sys
from PyQt5 import QtWidgets
import page1,page2,main

#I wrote the following code to hide the warnings coming to the console every time the program is started. I stole :)
os.environ["QT_DEVICE_PIXEL_RATIO"] = "0"
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
os.environ["QT_SCREEN_SCALE_FACTORS"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1"

app = QtWidgets.QApplication(sys.argv)

PAGE1 = QtWidgets.QMainWindow()
PAGE2 = QtWidgets.QMainWindow()

def a(x):
    if(__name__ == "__main__"):
        main.a(x)#I found this method by trial and error. I don't know how or why it works :)
    else:
        if(x==1): 
            uip1 = page1.Ui_Page1()
            uip1.setupUi(PAGE1)
            uip1.fillElements()#this function to fill the content before the page is opened (example: changing the text of pushButton etc.)
            PAGE2.hide()
            PAGE1.show()
        elif(x==2):
            uip2 = page2.Ui_Page2()
            uip2.setupUi(PAGE2)
            uip2.fillElements()
            PAGE1.hide()
            PAGE2.show()


if __name__ == "__main__":
    a(1)#Here you can extract data from another place and open the login screen or the main screen according to the incoming data.
    os._exit(app.exec_())