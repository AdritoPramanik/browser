import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar  = QToolBar()
        self.addToolBar(navbar)

        backbtn = QAction(QIcon('back.png'),'back', self)
        backbtn.triggered.connect(self.browser.back)
        navbar.addAction(backbtn)

        forwardbtn = QAction(QIcon('forward.png'),'Forward', self)
        forwardbtn.triggered.connect(self.browser.forward)
        navbar.addAction(forwardbtn)

        reloadbtn = QAction(QIcon('reload.png'),'Reload', self)
        reloadbtn.triggered.connect(self.browser.reload)
        navbar.addAction(reloadbtn)

        homebtn = QAction(QIcon('home.png'),'home', self)
        homebtn.triggered.connect(self.navigate_home)
        navbar.addAction(homebtn)

        self.urlBar = QLineEdit()
        self.urlBar.returnPressed.connect(self.navigateToUrl)
        navbar.addWidget(self.urlBar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigateToUrl(self):
        url = self.urlBar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.urlBar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Adi's Browser")
window  = MainWindow()
app.exec_()