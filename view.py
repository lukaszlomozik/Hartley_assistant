from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(450, 380))
        MainWindow.setMaximumSize(QtCore.QSize(450, 380))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont("Arial", 11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.coefficient_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.coefficient_spinBox.setMinimum(2)
        self.coefficient_spinBox.setProperty("value", 3)
        self.coefficient_spinBox.setObjectName("coefficient_spinBox")
        self.coefficient_spinBox.setMaximumSize(50, 30)
        self.coefficient_spinBox.setMaximumSize(50, 30)
        self.coefficient_spinBox.setFont(font)
        self.horizontalLayout_2.addWidget(self.coefficient_spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.repetitions_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.repetitions_spinBox.setMinimum(2)
        self.repetitions_spinBox.setProperty("value", 3)
        self.repetitions_spinBox.setObjectName("repetitions_spinBox")
        self.repetitions_spinBox.setMaximumSize(50, 30)
        self.repetitions_spinBox.setMaximumSize(50, 30)
        self.repetitions_spinBox.setFont(font)
        self.horizontalLayout_3.addWidget(self.repetitions_spinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.significante_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.significante_doubleSpinBox.setWrapping(False)
        self.significante_doubleSpinBox.setSpecialValueText("")
        self.significante_doubleSpinBox.setSingleStep(0.01)
        self.significante_doubleSpinBox.setFont(font)
        #self.significante_doubleSpinBox.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.significante_doubleSpinBox.setProperty("value", 0.05)
        self.significante_doubleSpinBox.setObjectName("significante_doubleSpinBox")
        self.significante_doubleSpinBox.setMaximumSize(50, 20)
        self.significante_doubleSpinBox.setMinimumSize(50, 20)
        self.horizontalLayout.addWidget(self.significante_doubleSpinBox)

        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setFont(font)
        self.verticalLayout.addWidget(self.checkBox)
        # self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        # self.checkBox_2.setObjectName("checkBox_2")
        # self.verticalLayout.addWidget(self.checkBox_2)

        self.template_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.template_pushButton.sizePolicy().hasHeightForWidth())

        def set_font(size=11, bold=True, weight=60, object=None):
            font = QtGui.QFont()
            font.setPointSize(size)
            font.setBold(bold)
            font.setWeight(weight)
            object.setFont(font)
            object.setObjectName(str(object))

        self.template_pushButton.setSizePolicy(sizePolicy)
        set_font(object=self.template_pushButton)
        self.verticalLayout.addWidget(self.template_pushButton)

        self.load_pushButton = QtWidgets.QPushButton(self.centralwidget)
        set_font(object=self.load_pushButton)
        self.verticalLayout.addWidget(self.load_pushButton)

        self.analysis_pushButton = QtWidgets.QPushButton(self.centralwidget)
        set_font(object=self.analysis_pushButton)
        self.verticalLayout.addWidget(self.analysis_pushButton)

        self.scatterplot_pushButton = QtWidgets.QPushButton(self.centralwidget)
        set_font(object=self.scatterplot_pushButton)
        self.verticalLayout.addWidget(self.scatterplot_pushButton)

        self.plot3d_pushButton = QtWidgets.QPushButton(self.centralwidget)
        set_font(object=self.plot3d_pushButton)
        self.verticalLayout.addWidget(self.plot3d_pushButton)

        self.optimalization_pushButton = QtWidgets.QPushButton(self.centralwidget)
        set_font(object=self.optimalization_pushButton)
        self.verticalLayout.addWidget(self.optimalization_pushButton)

        self.report_pushButton = QtWidgets.QPushButton(self.centralwidget)
        set_font(object=self.report_pushButton)
        self.verticalLayout.addWidget(self.report_pushButton)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        self.menut = QtWidgets.QMenu(self.menubar)
        self.menut.setObjectName("menut")
        self.menuMotyw = QtWidgets.QMenu(self.menut)
        self.menuMotyw.setObjectName("menuMotyw")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.themes = ["light_yellow.xml", "light_teal.xml", "dark_purple.xml", "light_amber.xml", "light_blue.xml",
                       "light_purple.xml", "dark_pink.xml", "light_cyan.xml", "dark_blue.xml", "dark_teal.xml",
                       "dark_lightgreen.xml", "light_lightgreen.xml", "light_pink.xml", "dark_amber.xml",
                       "dark_cyan.xml", "dark_red.xml"]

        self.actions = []

        for i in range(len(self.themes)):
            self.actions.append(QtWidgets.QAction(MainWindow))
            self.actions[i].setObjectName(self.themes[i])
            self.menuMotyw.addAction(self.actions[i])
        self.menut.addAction(self.menuMotyw.menuAction())
        self.menubar.addAction(self.menut.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hartley v3.0"))
        self.label_2.setText(_translate("MainWindow", "Ilość czynników"))
        self.label_3.setText(_translate("MainWindow", "Ilość powtórzeń"))
        self.label.setText(_translate("MainWindow", "Istotność"))
        self.checkBox.setText(_translate("MainWindow", "Optymalizuj dane wejściowe"))
        self.template_pushButton.setText(_translate("MainWindow", "Szablon"))
        self.load_pushButton.setText(_translate("MainWindow", "Wczytaj"))
        self.analysis_pushButton.setText(_translate("MainWindow", "Analizuj"))
        self.scatterplot_pushButton.setText(_translate("MainWindow", "Wykres rozrzutu"))
        self.plot3d_pushButton.setText(_translate("MainWindow", "Wykresy 3d"))
        self.optimalization_pushButton.setText(_translate("MainWindow", "Optymalizacja"))
        self.report_pushButton.setText(_translate("MainWindow", "Raport"))
        self.menut.setTitle(_translate("MainWindow", "Opcje"))
        self.menuMotyw.setTitle(_translate("MainWindow", "Motyw"))
        for i in range(len(self.themes)):
            self.actions[i].setText(_translate("MainWindow", self.themes[i]))


class Ui_PlotWindow(object):
    def __init__(self, numb_coef, factors_name):
        self.numb_coef = numb_coef
        self.factors_name = factors_name

    def setupUi(self, PlotWindow):
        PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(122, 122)
        self.centralwidget = QtWidgets.QWidget(PlotWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        font = QtGui.QFont("Arial", 11)

        self.labels = {}
        for i in range(self.numb_coef):
            self.labels[f"labels_{i}"] = QtWidgets.QLabel(self.centralwidget)
            self.labels[f"labels_{i}"].setFont(font)

        for i in range(self.numb_coef):
            self.labels[f"labels_{i}"].setObjectName(f"label_{i}")
            self.verticalLayout_2.addWidget(self.labels[f"labels_{i}"])

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.comboBox = {}
        for i in range(self.numb_coef):
            self.comboBox[f"comboBox_{i}"] = QtWidgets.QComboBox(self.centralwidget)
            self.comboBox[f"comboBox_{i}"].setFont(font)

        for i in range(self.numb_coef):
            self.comboBox[f"comboBox_{i}"].setObjectName(f"comboBox_{i}")
            self.verticalLayout.addWidget(self.comboBox[f"comboBox_{i}"])

        for i in range(self.numb_coef):
            for n in range(5):
                self.comboBox[f"comboBox_{i}"].addItem("")

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        PlotWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PlotWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 122, 21))
        self.menubar.setObjectName("menubar")
        PlotWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PlotWindow)
        self.statusbar.setObjectName("statusbar")
        PlotWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PlotWindow)
        QtCore.QMetaObject.connectSlotsByName(PlotWindow)

    def retranslateUi(self, PlotWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotWindow.setWindowTitle(_translate("PlotWindow", "Wykresy 3D"))
        for i in range(self.numb_coef):
            self.labels[f"labels_{i}"].setText(_translate("PlotWindow", self.factors_name[i]))

        for i in range(self.numb_coef):
            self.comboBox[f"comboBox_{i}"].setItemText(0, _translate("PlotWindow", "X"))
            self.comboBox[f"comboBox_{i}"].setItemText(1, _translate("PlotWindow", "Y"))
            self.comboBox[f"comboBox_{i}"].setItemText(2, _translate("PlotWindow", "1"))
            self.comboBox[f"comboBox_{i}"].setItemText(3, _translate("PlotWindow", "0"))
            self.comboBox[f"comboBox_{i}"].setItemText(4, _translate("PlotWindow", "-1"))

        self.pushButton.setText(_translate("PlotWindow", "Rysuj"))


class ReportView(object):
    def __init__(self, numb_coef, factors_name):
        self.numb_coef = numb_coef
        self.factors_name = factors_name

    def setupUi(self, report_window):
        report_window.setObjectName("MainWindow")
        report_window.resize(300, 258)
        self.centralwidget = QtWidgets.QWidget(report_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        font = QtGui.QFont("Arial", 11)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setValue(5)
        self.horizontalLayout_4.addWidget(self.spinBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setValue(4)
        self.horizontalLayout_3.addWidget(self.spinBox_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(20)
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFont(font)
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        report_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(report_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 216, 21))
        self.menubar.setObjectName("menubar")
        report_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(report_window)
        self.statusbar.setObjectName("statusbar")
        report_window.setStatusBar(self.statusbar)

        self.cmaps = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Greys', 'Purples', 'Blues', 'Greens',
                      'Oranges',
                      'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn', 'binary', 'gist_yarg', 'gist_gray', 'gray',
                      'bone',
                      'pink',
                      'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
                      'hot', 'afmhot', 'gist_heat', 'copper', 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
                      'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic', 'twilight', 'twilight_shifted',
                      'hsv',
                      'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
                      'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
                      'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral',
                      'gist_ncar']
        for i in range(len(self.cmaps)):
            self.comboBox.addItem("")
        self.retranslateUi(report_window)
        QtCore.QMetaObject.connectSlotsByName(report_window)

    def retranslateUi(self, report_window):
        _translate = QtCore.QCoreApplication.translate
        report_window.setWindowTitle(_translate("MainWindow", "Ustawienia wykresów 3D w raporcie"))
        self.groupBox.setTitle(_translate("MainWindow", "Ustawienia wykresów 3D"))
        self.label_3.setText(_translate("MainWindow", "Szerokość"))
        self.label_4.setText(_translate("MainWindow", "Wysokość"))
        self.label.setText(_translate("MainWindow", "Kolor wykresu"))
        for i in range(len(self.cmaps)):
            self.comboBox.setItemText(i, _translate("MainWindow", self.cmaps[i]))
        self.label_2.setText(_translate("MainWindow", "Pochylenie "))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.pushButton.setText(_translate("MainWindow", "Generuj"))


class OptimizationView(object):
    def __init__(self, numb_coef, factors_name):
        self.numb_coef = numb_coef
        self.factors_name = factors_name

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(390, 298)
        font = QtGui.QFont("Arial", 11)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.optimization_method_label = QtWidgets.QLabel(self.centralwidget)
        self.optimization_method_label.setFont(font)
        self.optimization_method_label.setObjectName("optimization_method_label")
        self.horizontalLayout_4.addWidget(self.optimization_method_label)
        self.optimization_method_label_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.optimization_method_label_comboBox.setFont(font)
        self.optimization_method_label_comboBox.setEnabled(True)
        self.optimization_method_label_comboBox.setMaximumSize(80, 20)
        self.optimization_method_label_comboBox.setMaximumSize(80, 20)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optimization_method_label_comboBox.sizePolicy().hasHeightForWidth())
        self.optimization_method_label_comboBox.setSizePolicy(sizePolicy)
        self.optimization_method_label_comboBox.setObjectName("optimization_method_label_comboBox")
        self.optimization_method_label_comboBox.addItem("")
        self.optimization_method_label_comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.optimization_method_label_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(28)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.goal_label = QtWidgets.QLabel(self.centralwidget)
        self.goal_label.setFont(font)
        self.goal_label.setObjectName("goal_label")
        self.horizontalLayout_5.addWidget(self.goal_label)
        self.goal_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.goal_comboBox.setFont(font)
        self.goal_comboBox.setMaximumSize(80, 20)
        self.goal_comboBox.setMaximumSize(80, 20)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.goal_comboBox.sizePolicy().hasHeightForWidth())
        self.goal_comboBox.setSizePolicy(sizePolicy)
        self.goal_comboBox.setObjectName("goal_comboBox")
        self.goal_comboBox.addItem("")
        self.goal_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.goal_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.steps_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.steps_groupBox.setFont(font)
        self.steps_groupBox.setObjectName("steps_groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.steps_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.variables_labels = {}
        self.variables_doubleSpinBox = {}
        for i in range(self.numb_coef):
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.variables_labels[f"variables_labels_{i}"] = QtWidgets.QLabel(self.steps_groupBox)
            self.variables_labels[f"variables_labels_{i}"].setObjectName("variable_label_1")
            self.variables_labels[f"variables_labels_{i}"].setFont(font)
            self.horizontalLayout.addWidget(self.variables_labels[f"variables_labels_{i}"])
            self.variables_doubleSpinBox[f"variables_doubleSpinBox {i}"] = QtWidgets.QDoubleSpinBox(self.steps_groupBox)
            self.variables_doubleSpinBox[f"variables_doubleSpinBox {i}"].setDecimals(6)
            self.variables_doubleSpinBox[f"variables_doubleSpinBox {i}"].setMaximum(1000000.0)
            self.variables_doubleSpinBox[f"variables_doubleSpinBox {i}"].setObjectName("variable_doubleSpinBox_1")
            self.horizontalLayout.addWidget(self.variables_doubleSpinBox[f"variables_doubleSpinBox {i}"])
            self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.steps_groupBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.OK_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.OK_pushButton.setFont(font)
        self.OK_pushButton.setObjectName("OK_pushButton")
        self.verticalLayout_4.addWidget(self.OK_pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_6.addWidget(self.textEdit)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 390, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Optymalizacja"))
        self.optimization_method_label.setText(_translate("MainWindow", "Metoda optymalizacji"))
        self.optimization_method_label_comboBox.setItemText(0, _translate("MainWindow", "Siłowa"))
        self.optimization_method_label_comboBox.setItemText(1, _translate("MainWindow", "Min-max"))
        self.goal_label.setText(_translate("MainWindow", "Funkcja celu"))
        self.goal_comboBox.setItemText(0, _translate("MainWindow", "Min"))
        self.goal_comboBox.setItemText(1, _translate("MainWindow", "Max"))
        self.steps_groupBox.setTitle(_translate("MainWindow", "Kroki zmienności"))
        for i in range(self.numb_coef):
            self.variables_labels[f"variables_labels_{i}"].setText(_translate("MainWindow", self.factors_name[i]))
        self.OK_pushButton.setText(_translate("MainWindow", "OK"))
