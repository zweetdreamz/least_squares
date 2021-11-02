# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_mnk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1468, 739)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1471, 741))
        font = QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.image_widget = QFrame(self.tab)
        self.image_widget.setObjectName(u"image_widget")
        self.image_widget.setGeometry(QRect(480, 10, 960, 540))
        self.result_label = QLabel(self.tab)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setGeometry(QRect(480, 600, 961, 71))
        font1 = QFont()
        font1.setPointSize(12)
        self.result_label.setFont(font1)
        self.result_label.setTextFormat(Qt.PlainText)
        self.calculate_button = QPushButton(self.tab)
        self.calculate_button.setObjectName(u"calculate_button")
        self.calculate_button.setGeometry(QRect(260, 600, 201, 81))
        self.calculate_button.setFont(font)
        self.import_button = QPushButton(self.tab)
        self.import_button.setObjectName(u"import_button")
        self.import_button.setGeometry(QRect(40, 600, 101, 81))
        self.import_button.setFont(font)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 50, 55, 31))
        self.label.setFont(font)
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 50, 55, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(350, 50, 71, 31))
        self.label_3.setFont(font)
        self.save_button = QPushButton(self.tab)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(150, 600, 101, 81))
        self.save_button.setFont(font)
        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(480, 3, 960, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(480, 545, 960, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(468, 10, 20, 541))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(1430, 10, 20, 541))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 90, 421, 471))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.y1_line_edit = QLineEdit(self.widget)
        self.y1_line_edit.setObjectName(u"y1_line_edit")

        self.gridLayout.addWidget(self.y1_line_edit, 0, 1, 1, 1)

        self.sigma1_line_edit = QLineEdit(self.widget)
        self.sigma1_line_edit.setObjectName(u"sigma1_line_edit")

        self.gridLayout.addWidget(self.sigma1_line_edit, 0, 2, 1, 1)

        self.x2_line_edit = QLineEdit(self.widget)
        self.x2_line_edit.setObjectName(u"x2_line_edit")

        self.gridLayout.addWidget(self.x2_line_edit, 1, 0, 1, 1)

        self.y2_line_edit = QLineEdit(self.widget)
        self.y2_line_edit.setObjectName(u"y2_line_edit")

        self.gridLayout.addWidget(self.y2_line_edit, 1, 1, 1, 1)

        self.sigma2_line_edit = QLineEdit(self.widget)
        self.sigma2_line_edit.setObjectName(u"sigma2_line_edit")

        self.gridLayout.addWidget(self.sigma2_line_edit, 1, 2, 1, 1)

        self.x3_line_edit = QLineEdit(self.widget)
        self.x3_line_edit.setObjectName(u"x3_line_edit")

        self.gridLayout.addWidget(self.x3_line_edit, 2, 0, 1, 1)

        self.y3_line_edit = QLineEdit(self.widget)
        self.y3_line_edit.setObjectName(u"y3_line_edit")

        self.gridLayout.addWidget(self.y3_line_edit, 2, 1, 1, 1)

        self.sigma3_line_edit = QLineEdit(self.widget)
        self.sigma3_line_edit.setObjectName(u"sigma3_line_edit")

        self.gridLayout.addWidget(self.sigma3_line_edit, 2, 2, 1, 1)

        self.x4_line_edit = QLineEdit(self.widget)
        self.x4_line_edit.setObjectName(u"x4_line_edit")

        self.gridLayout.addWidget(self.x4_line_edit, 3, 0, 1, 1)

        self.y4_line_edit = QLineEdit(self.widget)
        self.y4_line_edit.setObjectName(u"y4_line_edit")

        self.gridLayout.addWidget(self.y4_line_edit, 3, 1, 1, 1)

        self.x1_line_edit = QLineEdit(self.widget)
        self.x1_line_edit.setObjectName(u"x1_line_edit")

        self.gridLayout.addWidget(self.x1_line_edit, 0, 0, 1, 1)

        self.y7_line_edit = QLineEdit(self.widget)
        self.y7_line_edit.setObjectName(u"y7_line_edit")

        self.gridLayout.addWidget(self.y7_line_edit, 6, 1, 1, 1)

        self.sigma8_line_edit = QLineEdit(self.widget)
        self.sigma8_line_edit.setObjectName(u"sigma8_line_edit")

        self.gridLayout.addWidget(self.sigma8_line_edit, 7, 2, 1, 1)

        self.x5_line_edit = QLineEdit(self.widget)
        self.x5_line_edit.setObjectName(u"x5_line_edit")

        self.gridLayout.addWidget(self.x5_line_edit, 4, 0, 1, 1)

        self.sigma6_line_edit = QLineEdit(self.widget)
        self.sigma6_line_edit.setObjectName(u"sigma6_line_edit")

        self.gridLayout.addWidget(self.sigma6_line_edit, 5, 2, 1, 1)

        self.sigma10_line_edit = QLineEdit(self.widget)
        self.sigma10_line_edit.setObjectName(u"sigma10_line_edit")

        self.gridLayout.addWidget(self.sigma10_line_edit, 9, 2, 1, 1)

        self.x7_line_edit = QLineEdit(self.widget)
        self.x7_line_edit.setObjectName(u"x7_line_edit")

        self.gridLayout.addWidget(self.x7_line_edit, 6, 0, 1, 1)

        self.y8_line_edit = QLineEdit(self.widget)
        self.y8_line_edit.setObjectName(u"y8_line_edit")

        self.gridLayout.addWidget(self.y8_line_edit, 7, 1, 1, 1)

        self.y10_line_edit = QLineEdit(self.widget)
        self.y10_line_edit.setObjectName(u"y10_line_edit")

        self.gridLayout.addWidget(self.y10_line_edit, 9, 1, 1, 1)

        self.sigma9_line_edit = QLineEdit(self.widget)
        self.sigma9_line_edit.setObjectName(u"sigma9_line_edit")

        self.gridLayout.addWidget(self.sigma9_line_edit, 8, 2, 1, 1)

        self.sigma4_line_edit = QLineEdit(self.widget)
        self.sigma4_line_edit.setObjectName(u"sigma4_line_edit")

        self.gridLayout.addWidget(self.sigma4_line_edit, 3, 2, 1, 1)

        self.sigma5_line_edit = QLineEdit(self.widget)
        self.sigma5_line_edit.setObjectName(u"sigma5_line_edit")

        self.gridLayout.addWidget(self.sigma5_line_edit, 4, 2, 1, 1)

        self.y5_line_edit = QLineEdit(self.widget)
        self.y5_line_edit.setObjectName(u"y5_line_edit")

        self.gridLayout.addWidget(self.y5_line_edit, 4, 1, 1, 1)

        self.y6_line_edit = QLineEdit(self.widget)
        self.y6_line_edit.setObjectName(u"y6_line_edit")

        self.gridLayout.addWidget(self.y6_line_edit, 5, 1, 1, 1)

        self.sigma7_line_edit = QLineEdit(self.widget)
        self.sigma7_line_edit.setObjectName(u"sigma7_line_edit")

        self.gridLayout.addWidget(self.sigma7_line_edit, 6, 2, 1, 1)

        self.x8_line_edit = QLineEdit(self.widget)
        self.x8_line_edit.setObjectName(u"x8_line_edit")

        self.gridLayout.addWidget(self.x8_line_edit, 7, 0, 1, 1)

        self.x6_line_edit = QLineEdit(self.widget)
        self.x6_line_edit.setObjectName(u"x6_line_edit")

        self.gridLayout.addWidget(self.x6_line_edit, 5, 0, 1, 1)

        self.x10_line_edit = QLineEdit(self.widget)
        self.x10_line_edit.setObjectName(u"x10_line_edit")

        self.gridLayout.addWidget(self.x10_line_edit, 9, 0, 1, 1)

        self.y9_line_edit = QLineEdit(self.widget)
        self.y9_line_edit.setObjectName(u"y9_line_edit")

        self.gridLayout.addWidget(self.y9_line_edit, 8, 1, 1, 1)

        self.x9_line_edit = QLineEdit(self.widget)
        self.x9_line_edit.setObjectName(u"x9_line_edit")

        self.gridLayout.addWidget(self.x9_line_edit, 8, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.widget1 = QWidget(self.tab_2)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 30, 521, 291))
        self.gridLayout_2 = QGridLayout(self.widget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.widget1)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)

        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.result_label.setText("")
        self.calculate_button.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.import_button.setText(QCoreApplication.translate("Form", u"Import", None))
        self.label.setText(QCoreApplication.translate("Form", u"X", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Y", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Sigma", None))
        self.save_button.setText(QCoreApplication.translate("Form", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Main tab", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Color              ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ox", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Oy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Settings", None))
    # retranslateUi

