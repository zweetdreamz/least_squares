from PySide2 import QtWidgets
from PySide2.QtCore import QRegExp, QDir
from PySide2.QtGui import QRegExpValidator
import pyqtgraph as pg
import pyqtgraph.exporters
from PySide2.QtWidgets import QFileDialog
import csv

from pyqtgraph.exporters import ImageExporter

from UI.ui_ls import Ui_Form
from back import LeastSquares


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

        self.graph_widget = pg.PlotWidget(self.image_widget)
        self.graph_widget.setObjectName(u"image_widget")
        self.graph_widget.setGeometry(*(0, 0, 960, 540))
        self.graph_widget.setBackground('w')
        styles = {"color": "#f00", "font-size": "20px"}
        self.graph_widget.setLabel("left", "Ox", **styles)
        self.graph_widget.setLabel("bottom", "Oy", **styles)

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
        y = list(map(float, y))

        s = [
            self.s1_line_edit.text(),
            self.s2_line_edit.text(),
            self.s3_line_edit.text(),
            self.s4_line_edit.text(),
            self.s5_line_edit.text(),
            self.s6_line_edit.text(),
            self.s7_line_edit.text(),
            self.s8_line_edit.text(),
            self.s9_line_edit.text(),
            self.s10_line_edit.text(),
        ]
        s = list(map(float, s))


        pass

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
            data = list([row[0], row[1]] for row in reader)

        x = list(float(row[0]) for row in data)
        y = list(float(row[1]) for row in data)
        self.graph_widget.plot(x, y, pen=pg.mkPen(color=(255, 0, 0), width=2.5))
        pass

    def save_image(self):
        """
        тут будем сохранять картинку в файл
        :return:
        """

        exporter = ImageExporter(self.graph_widget.plotItem)

        exporter.params.param('width').setValue(1024, blockSignal=exporter.widthChanged)
        exporter.params.param('height').setValue(1024, blockSignal=exporter.heightChanged)

        # save to file
        exporter.export('fileName.png')
