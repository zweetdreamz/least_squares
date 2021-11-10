from PySide2 import QtWidgets
from PySide2.QtCore import QRegExp, QDir
from PySide2.QtGui import QRegExpValidator
import pyqtgraph as pg
from PySide2.QtWidgets import QFileDialog
import csv

from pyqtgraph.exporters import ImageExporter

from UI.ui_ls import Ui_Form
from back import LeastSquares


class MainWindow(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        # инициализация интерфейса
        super().__init__()
        self.setupUi(self)
        # бинды кнопок
        self.calculate_button.clicked.connect(self.calculate)
        self.import_button.clicked.connect(self.calculate_imported)
        self.save_button.clicked.connect(self.save_image)
        # установка валидации входных данных
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

        # инициализация pg.PlotWidget
        self.graph_widget = pg.PlotWidget(self.image_widget)
        self.graph_widget.setObjectName(u"image_widget")
        self.graph_widget.setGeometry(*(0, 0, 960, 540))
        self.graph_widget.setBackground('w')
        styles = {"color": "black", "font-size": "20px"}
        self.graph_widget.setLabel("left", "Ox", **styles)
        self.graph_widget.setLabel("bottom", "Oy", **styles)
        self.graph_widget.showGrid(x=True, y=True, alpha=1.0)

        self.show()
        self.update()

    def calculate(self):
        """
        тут будем считать все по точкам
        :return:
        """
        self.graph_widget.clear()

        x = [
            self.x1_line_edit.text(),
            self.x2_line_edit.text(),
            self.x3_line_edit.text(),
            self.x4_line_edit.text(),
            self.x5_line_edit.text(),
            self.x6_line_edit.text(),
            self.x7_line_edit.text(),
            self.x8_line_edit.text(),
            self.x9_line_edit.text(),
            self.x10_line_edit.text(),
        ]
        # убираем недействительные значения
        x = [i for i in x if i]
        # приведение типа данных
        x = list(map(float, x))

        y = [
            self.y1_line_edit.text(),
            self.y2_line_edit.text(),
            self.y3_line_edit.text(),
            self.y4_line_edit.text(),
            self.y5_line_edit.text(),
            self.y6_line_edit.text(),
            self.y7_line_edit.text(),
            self.y8_line_edit.text(),
            self.y9_line_edit.text(),
            self.y10_line_edit.text(),
        ]
        # убираем недействительные значения
        y = [i for i in y if i]
        # приведение типа данных
        y = list(map(float, y))

        s = [
            self.sigma1_line_edit.text(),
            self.sigma2_line_edit.text(),
            self.sigma3_line_edit.text(),
            self.sigma4_line_edit.text(),
            self.sigma5_line_edit.text(),
            self.sigma6_line_edit.text(),
            self.sigma7_line_edit.text(),
            self.sigma8_line_edit.text(),
            self.sigma9_line_edit.text(),
            self.sigma10_line_edit.text(),
        ]
        # убираем недействительные значения
        s = [i for i in s if i]
        # приведение типа данных
        s = list(map(float, s))

        # инициализация мат ядра
        core = LeastSquares.LeastSquares(x, y, s)
        a, b, s_a, s_b, r = core.get_result()

        # построение графика
        self.graph_widget.plot(x, [a * i + b for i in x], pen=pg.mkPen(color=self.comboBox.currentText(), width=3))
        self.graph_widget.scatterPlot(x, y, pen=pg.mkPen(color=(255, 0, 0), width=1))
        styles = {"color": "black", "font-size": "20px"}
        self.graph_widget.setLabel("left", "Ox " + self.lineEdit_2.text(), **styles)
        self.graph_widget.setLabel("bottom", "Oy " + self.lineEdit.text(), **styles)
        self.result_label.setText(f's_a = {s_a}\ns_b = {s_b}\nr = {r}')

    def calculate_imported(self):
        """
        тут будем считать все по точкам из фала
        :return:
        """
        self.graph_widget.clear()

        curPath = QDir.currentPath()  # Get the current directory of the system
        title = "Open a file"  # Dialog title
        filter = "CSV file (*.csv);; All files (*.*)"  # File filter
        filename, flt = QFileDialog.getOpenFileName(self, title, curPath, filter)
        if not filename:
            return

        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            data = list([*row] for row in reader)

        # приведение типа данных
        x = list(float(row[0]) for row in data)
        y = list(float(row[1]) for row in data)
        s = list(float(row[2]) for row in data)

        # инициализация мат ядра
        core = LeastSquares.LeastSquares(x, y, s)
        a, b, s_a, s_b, r = core.get_result()

        # построение графика
        self.graph_widget.plot(x, [a*i + b for i in x], pen=pg.mkPen(color=self.comboBox.currentText(), width=3))
        self.graph_widget.scatterPlot(x, y, pen=pg.mkPen(color=(255, 0, 0), width=1))
        styles = {"color": "black", "font-size": "20px"}
        self.graph_widget.setLabel("left", "Ox " + self.lineEdit_2.text(), **styles)
        self.graph_widget.setLabel("bottom", "Oy " + self.lineEdit.text(), **styles)
        self.result_label.setText(f's_a = {s_a}\ns_b = {s_b}\nr = {r}')

    def save_image(self):
        """
        тут будем сохранять картинку в файл
        :return:
        """

        # инициализация класса экспортера
        exporter = ImageExporter(self.graph_widget.plotItem)

        exporter.params.param('width').setValue(1280, blockSignal=exporter.widthChanged)
        exporter.params.param('height').setValue(720, blockSignal=exporter.heightChanged)

        # сохранение в файл
        exporter.export('fileName.png')
