# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\msys64\home\github\bmstu-4sem-cg\lab_07py\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from canvas import Canvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(689, 20, 281, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.QPB_add_section = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QPB_add_section.setFont(font)
        self.QPB_add_section.setObjectName("QPB_add_section")
        self.gridLayout.addWidget(self.QPB_add_section, 13, 0, 1, 4)
        self.QPB_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QPB_clear.setFont(font)
        self.QPB_clear.setObjectName("QPB_clear")
        self.gridLayout.addWidget(self.QPB_clear, 21, 0, 1, 4)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 19, 0, 1, 4)
        self.QRB_section = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QRB_section.setFont(font)
        self.QRB_section.setObjectName("QRB_section")
        self.gridLayout.addWidget(self.QRB_section, 4, 0, 1, 4)
        self.QPB_add_cutter = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QPB_add_cutter.setFont(font)
        self.QPB_add_cutter.setObjectName("QPB_add_cutter")
        self.gridLayout.addWidget(self.QPB_add_cutter, 18, 0, 1, 4)
        self.QCB_color = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QCB_color.setFont(font)
        self.QCB_color.setObjectName("QCB_color")
        self.QCB_color.addItem("")
        self.QCB_color.addItem("")
        self.QCB_color.addItem("")
        self.gridLayout.addWidget(self.QCB_color, 1, 0, 1, 4)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(
            self.label_10, 17, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(
            self.label_8, 15, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(
            self.label_9, 17, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.QSB_section_x_end = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QSB_section_x_end.setFont(font)
        self.QSB_section_x_end.setMaximum(1000)
        self.QSB_section_x_end.setObjectName("QSB_section_x_end")
        self.gridLayout.addWidget(self.QSB_section_x_end, 9, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(
            self.label_3, 0, 0, 1, 4, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(
            self.label_2, 8, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.QSB_cutter_x_end = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QSB_cutter_x_end.setFont(font)
        self.QSB_cutter_x_end.setMaximum(1000)
        self.QSB_cutter_x_end.setObjectName("QSB_cutter_x_end")
        self.gridLayout.addWidget(self.QSB_cutter_x_end, 17, 1, 1, 1)
        self.QSB_cutter_x_start = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QSB_cutter_x_start.setFont(font)
        self.QSB_cutter_x_start.setMaximum(1000)
        self.QSB_cutter_x_start.setObjectName("QSB_cutter_x_start")
        self.gridLayout.addWidget(self.QSB_cutter_x_start, 15, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(
            self.label_11, 15, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.QSB_cutter_y_start = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QSB_cutter_y_start.setFont(font)
        self.QSB_cutter_y_start.setMaximum(1000)
        self.QSB_cutter_y_start.setObjectName("QSB_cutter_y_start")
        self.gridLayout.addWidget(self.QSB_cutter_y_start, 15, 3, 1, 1)
        self.QSB_section_y_start = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QSB_section_y_start.setFont(font)
        self.QSB_section_y_start.setMaximum(1000)
        self.QSB_section_y_start.setObjectName("QSB_section_y_start")
        self.gridLayout.addWidget(self.QSB_section_y_start, 8, 3, 1, 1)
        self.QRB_cutter = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QRB_cutter.setFont(font)
        self.QRB_cutter.setObjectName("QRB_cutter")
        self.gridLayout.addWidget(self.QRB_cutter, 5, 0, 1, 4)
        self.QPB_cut = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QPB_cut.setFont(font)
        self.QPB_cut.setObjectName("QPB_cut")
        self.gridLayout.addWidget(self.QPB_cut, 20, 0, 1, 4)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(
            self.label_5, 7, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(
            self.label_6, 9, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.QSB_section_y_end = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QSB_section_y_end.setFont(font)
        self.QSB_section_y_end.setMaximum(1000)
        self.QSB_section_y_end.setObjectName("QSB_section_y_end")
        self.gridLayout.addWidget(self.QSB_section_y_end, 9, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 14, 0, 1, 4)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(
            self.label_7, 9, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(
            self.label, 8, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.QSB_section_x_start = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QSB_section_x_start.setFont(font)
        self.QSB_section_x_start.setMaximum(1000)
        self.QSB_section_x_start.setObjectName("QSB_section_x_start")
        self.gridLayout.addWidget(self.QSB_section_x_start, 8, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(
            self.label_4, 3, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.QSB_cutter_y_end = QtWidgets.QSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.QSB_cutter_y_end.setFont(font)
        self.QSB_cutter_y_end.setMaximum(1000)
        self.QSB_cutter_y_end.setObjectName("QSB_cutter_y_end")
        self.gridLayout.addWidget(self.QSB_cutter_y_end, 17, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 4)
        self.canvas = Canvas(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 671, 591))
        self.canvas.setObjectName("canvas")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "lab_07. Простой алгоритм отсечения отрезка"))
        self.QPB_add_section.setText(
            _translate("MainWindow", "Ввести отрезок"))
        self.QPB_clear.setText(_translate("MainWindow", "Очистить холст"))
        self.QRB_section.setText(_translate("MainWindow", "Ввод отрезков"))
        self.QPB_add_cutter.setText(_translate(
            "MainWindow", "Ввести отсекатель"))
        self.QCB_color.setItemText(0, _translate("MainWindow", "Синий"))
        self.QCB_color.setItemText(1, _translate("MainWindow", "Черный"))
        self.QCB_color.setItemText(2, _translate("MainWindow", "Белый(фон)"))
        self.label_10.setText(_translate("MainWindow", "Yк"))
        self.label_8.setText(_translate("MainWindow", "Xн"))
        self.label_9.setText(_translate("MainWindow", "Xк"))
        self.label_3.setText(_translate("MainWindow", "Цвет отрезков"))
        self.label_2.setText(_translate("MainWindow", "Yн"))
        self.label_11.setText(_translate("MainWindow", "Yн"))
        self.QRB_cutter.setText(_translate(
            "MainWindow", "Ввод отсекателя по двум вершинам"))
        self.QPB_cut.setText(_translate("MainWindow", "Отсечь"))
        self.label_5.setText(_translate("MainWindow", "Ввод с клавиатуры"))
        self.label_6.setText(_translate("MainWindow", "Xк"))
        self.label_7.setText(_translate("MainWindow", "Yк"))
        self.label.setText(_translate("MainWindow", "Xн"))
        self.label_4.setText(_translate("MainWindow", "Ввод мышкой"))
        self.canvas.setText(_translate("MainWindow", "TextLabel"))
