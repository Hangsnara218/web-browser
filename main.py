from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class WebBrowser():

    def __init__(self):
        self.window =  QWidget()
        self.window.setWindowTitle("r4pt0r web browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.urlBar = QTextEdit()
        self.urlBar.setMaximumHeight(30)

        self.goBtn = QPushButton("GO")
        self.goBtn.setMinimumHeight(30)

        self.backBtn = QPushButton("<<")
        self.backBtn.setMinimumHeight(30)

        self.forwardBtn = QPushButton(">>")
        self.forwardBtn.setMinimumHeight(30)
        
        self.horizontal.addWidget(self.urlBar)
        self.horizontal.addWidget(self.goBtn)
        self.horizontal.addWidget(self.backBtn)
        self.horizontal.addWidget(self.forwardBtn)
        
        self.browser = QWebEngineView()

        self.goBtn.clicked.connect(lambda: self.navigate(self.urlBar.toPlainText()))
        self.backBtn.clicked.connect(self.browser.back)        
        self.forwardBtn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://flashback.org/"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("https"):
            url = "https://" + url
            self.urlBar.setText(url)
        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = WebBrowser()
app.exec_()
