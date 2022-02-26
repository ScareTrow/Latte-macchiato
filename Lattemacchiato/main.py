import sys
import sqlite3

from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(457, 290)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ID_input = QtWidgets.QLineEdit(Form)
        self.ID_input.setObjectName("ID_input")
        self.horizontalLayout.addWidget(self.ID_input)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sort_type = QtWidgets.QLineEdit(Form)
        self.sort_type.setObjectName("sort_type")
        self.horizontalLayout_2.addWidget(self.sort_type)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.roast_text = QtWidgets.QLineEdit(Form)
        self.roast_text.setObjectName("roast_text")
        self.horizontalLayout_3.addWidget(self.roast_text)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.consistency_text = QtWidgets.QLineEdit(Form)
        self.consistency_text.setObjectName("consistency_text")
        self.horizontalLayout_4.addWidget(self.consistency_text)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.description_text = QtWidgets.QLineEdit(Form)
        self.description_text.setObjectName("description_text")
        self.horizontalLayout_7.addWidget(self.description_text)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.price_text = QtWidgets.QLineEdit(Form)
        self.price_text.setObjectName("price_text")
        self.horizontalLayout_6.addWidget(self.price_text)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.volume_text = QtWidgets.QLineEdit(Form)
        self.volume_text.setObjectName("volume_text")
        self.horizontalLayout_5.addWidget(self.volume_text)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.update_button = QtWidgets.QPushButton(Form)
        self.update_button.setObjectName("update_button")
        self.horizontalLayout_9.addWidget(self.update_button)
        self.add_entry_button = QtWidgets.QPushButton(Form)
        self.add_entry_button.setObjectName("add_entry_button")
        self.horizontalLayout_9.addWidget(self.add_entry_button)
        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ID:"))
        self.label_2.setText(_translate("Form", "Sort Name:"))
        self.label_3.setText(_translate("Form", "Degree of roast:"))
        self.label_4.setText(_translate("Form", "Ground/In grains:"))
        self.label_7.setText(_translate("Form", "Description:"))
        self.label_5.setText(_translate("Form", "Price:"))
        self.label_6.setText(_translate("Form", "Volume package:"))
        self.update_button.setText(_translate("Form", "Update"))
        self.add_entry_button.setText(_translate("Form", "Add"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        global self_programm
        self_programm = self
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.db")
        self.write_to_table()
        self.createEntry.clicked.connect(self.create_entry)
        self.refreshButton.clicked.connect(self.write_to_table)

    def create_entry(self):
        self.form = Window()
        self.form.show()

    def write_to_table(self):
        cur = self.con.cursor()
        result = cur.execute(f"""SELECT * FROM information
                             ORDER BY ID""").fetchall()

        self.tableWidget.setRowCount(len(result))

        if not result:
            return
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        header = self.tableWidget.horizontalHeader()
        title = ["ID", "sorts_name", "degree_of_roast", "ground_or_grains",
                 "flavor_description", "price", "packing_volume"]

        self.tableWidget.setHorizontalHeaderLabels(title)
        self.result = list()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        for i in range(1, len(title)):
            header.setSectionResizeMode(
                i, QtWidgets.QHeaderView.ResizeToContents)


class Window(QWidget, Ui_Form):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.update_button.clicked.connect(self.update)
        self.add_entry_button.clicked.connect(self.add)

    def update(self):
        ID = self.ID_input.text()
        sorts_name = self.sort_type.text()
        degree_of_roast = self.roast_text.text()
        consistency = self.consistency_text.text()
        description = self.description_text.text()
        price = self.price_text.text()
        volume = self.volume_text.text()

        con = sqlite3.connect("data/coffee.db")
        cur = con.cursor()

        if sorts_name != "":
            cur.execute(f'''UPDATE information SET sorts_name = "{sorts_name}"
                            WHERE ID = "{ID}"''')
        if degree_of_roast != "":
            cur.execute(f'''UPDATE information SET degree_of_roast = "{degree_of_roast}"
                            WHERE ID = "{ID}"''')
        if consistency != "":
            cur.execute(f'''UPDATE information SET ground_or_grains = "{consistency}"
                            WHERE ID = "{ID}"''')
        if description != "":
            cur.execute(f'''UPDATE information SET flavor_description = "{description}"
                            WHERE ID = "{ID}"''')
        if price != "":
            cur.execute(f'''UPDATE information SET price = "{price}"
                            WHERE ID = "{ID}"''')
        if volume != "":
            cur.execute(f'''UPDATE information SET packing_volume = "{volume}"
                            WHERE ID = "{ID}"''')
        con.commit()
        self_programm.form.close()
        self_programm.write_to_table()

    def add(self):
        try:
            ID = self.ID_input.text()
            sorts_name = self.sort_type.text()
            degree_of_roast = self.roast_text.text()
            consistency = self.consistency_text.text()
            description = self.description_text.text()
            price = self.price_text.text()
            volume = self.volume_text.text()

            con = sqlite3.connect("data/coffee.db")
            cur = con.cursor()
            cur.execute(f"INSERT OR IGNORE INTO information VALUES ('{ID}', '{sorts_name}', '{degree_of_roast}',"
                        f" '{consistency}', '{description}', '{price}', '{volume}')")
            con.commit()
            self_programm.form.close()
            self_programm.write_to_table()
        except sqlite3.IntegrityError:
            print("Введите значения")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
