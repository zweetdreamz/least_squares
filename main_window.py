from PySide2 import QtWidgets
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator

from ui_ls import Ui_Form


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.calculate_button.clicked.connect(self.calculate)
        self.import_button.clicked.connect(self.calculate_imported)
        self.save_button.clicked.connect(self.save_image)

        float_validator = QRegExpValidator(QRegExp(r'[0-9].+'))
        self.x1_line_edit.setValidator(float_validator)
        self.x2_line_edit.setValidator(float_validator)
        self.x3_line_edit.setValidator(float_validator)
        self.x4_line_edit.setValidator(float_validator)
        self.x5_line_edit.setValidator(float_validator)
        self.x6_line_edit.setValidator(float_validator)
        self.x7_line_edit.setValidator(float_validator)
        self.x8_line_edit.setValidator(float_validator)
        self.x9_line_edit.setValidator(float_validator)
        self.x10_line_edit.setValidator(float_validator)
        self.y1_line_edit.setValidator(float_validator)
        self.y2_line_edit.setValidator(float_validator)
        self.y3_line_edit.setValidator(float_validator)
        self.y4_line_edit.setValidator(float_validator)
        self.y5_line_edit.setValidator(float_validator)
        self.y6_line_edit.setValidator(float_validator)
        self.y7_line_edit.setValidator(float_validator)
        self.y8_line_edit.setValidator(float_validator)
        self.y9_line_edit.setValidator(float_validator)
        self.y10_line_edit.setValidator(float_validator)
        self.sigma1_line_edit.setValidator(float_validator)
        self.sigma2_line_edit.setValidator(float_validator)
        self.sigma3_line_edit.setValidator(float_validator)
        self.sigma4_line_edit.setValidator(float_validator)
        self.sigma5_line_edit.setValidator(float_validator)
        self.sigma6_line_edit.setValidator(float_validator)
        self.sigma7_line_edit.setValidator(float_validator)
        self.sigma8_line_edit.setValidator(float_validator)
        self.sigma9_line_edit.setValidator(float_validator)
        self.sigma10_line_edit.setValidator(float_validator)
        self.comboBox.addItems(['Black', 'Green', 'Blue', 'Yellow'])
        self.show()
        self.update()

    def calculate(self):
        """
        тут будем считать все по точкам
        :return:
        """
        pass

    def calculate_imported(self):
        """
        тут будем считать все по точкам из фала
        :return:
        """
        pass

    def save_image(self):
        """
        тут будем сохранять картинку в файл
        :return:
        """
        pass
