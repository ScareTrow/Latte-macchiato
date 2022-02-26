class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(762, 505)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 731, 391))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(200, 440, 341, 31))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.createEntry = QtWidgets.QPushButton(self.splitter)
        self.createEntry.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.createEntry.setObjectName("createEntry")
        self.refreshButton = QtWidgets.QPushButton(self.splitter)
        self.refreshButton.setStyleSheet("font: 75 12pt \"Times New Roman\";")
        self.refreshButton.setObjectName("refreshButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Espresso"))
        self.createEntry.setText(_translate("MainWindow", "Сreate entry"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
