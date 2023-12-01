# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StockChart(object):
    def setupUi(self, StockChart):
        StockChart.setObjectName("StockChart")
        StockChart.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StockChart.sizePolicy().hasHeightForWidth())
        StockChart.setSizePolicy(sizePolicy)
        StockChart.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(StockChart)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 40, 483, 581))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(35, 20, 35, 20)
        self.gridLayout.setVerticalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_confirm = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_confirm.sizePolicy().hasHeightForWidth())
        self.btn_confirm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.btn_confirm.setFont(font)
        self.btn_confirm.setStyleSheet("")
        self.btn_confirm.setIconSize(QtCore.QSize(20, 20))
        self.btn_confirm.setCheckable(False)
        self.btn_confirm.setObjectName("btn_confirm")
        self.gridLayout.addWidget(self.btn_confirm, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.line_target = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_target.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_target.sizePolicy().hasHeightForWidth())
        self.line_target.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.line_target.setFont(font)
        self.line_target.setAutoFillBackground(False)
        self.line_target.setText("")
        self.line_target.setClearButtonEnabled(False)
        self.line_target.setObjectName("line_target")
        self.horizontalLayout_2.addWidget(self.line_target, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioBtn_tai = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioBtn_tai.sizePolicy().hasHeightForWidth())
        self.radioBtn_tai.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.radioBtn_tai.setFont(font)
        self.radioBtn_tai.setChecked(True)
        self.radioBtn_tai.setObjectName("radioBtn_tai")
        self.T_or_A = QtWidgets.QButtonGroup(StockChart)
        self.T_or_A.setObjectName("T_or_A")
        self.T_or_A.addButton(self.radioBtn_tai)
        self.verticalLayout.addWidget(self.radioBtn_tai)
        self.radioBtn_usa = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioBtn_usa.sizePolicy().hasHeightForWidth())
        self.radioBtn_usa.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.radioBtn_usa.setFont(font)
        self.radioBtn_usa.setChecked(False)
        self.radioBtn_usa.setObjectName("radioBtn_usa")
        self.T_or_A.addButton(self.radioBtn_usa)
        self.verticalLayout.addWidget(self.radioBtn_usa)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem1, 3, 1, 1, 1)
        self.label_end = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_end.sizePolicy().hasHeightForWidth())
        self.label_end.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_end.setFont(font)
        self.label_end.setObjectName("label_end")
        self.gridLayout_3.addWidget(self.label_end, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        self.label_start = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_start.sizePolicy().hasHeightForWidth())
        self.label_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_start.setFont(font)
        self.label_start.setObjectName("label_start")
        self.gridLayout_3.addWidget(self.label_start, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.radioBtn_candle = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioBtn_candle.setFont(font)
        self.radioBtn_candle.setChecked(True)
        self.radioBtn_candle.setObjectName("radioBtn_candle")
        self.candle_or_line = QtWidgets.QButtonGroup(StockChart)
        self.candle_or_line.setObjectName("candle_or_line")
        self.candle_or_line.addButton(self.radioBtn_candle)
        self.gridLayout_3.addWidget(self.radioBtn_candle, 2, 1, 1, 1)
        self.start_date = QtWidgets.QDateEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_date.sizePolicy().hasHeightForWidth())
        self.start_date.setSizePolicy(sizePolicy)
        self.start_date.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.start_date.setFont(font)
        self.start_date.setCalendarPopup(True)
        self.start_date.setDate(QtCore.QDate(2023, 1, 1))
        self.start_date.setObjectName("start_date")
        self.gridLayout_3.addWidget(self.start_date, 0, 1, 1, 1)
        self.end_date = QtWidgets.QDateEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_date.sizePolicy().hasHeightForWidth())
        self.end_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.end_date.setFont(font)
        self.end_date.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.end_date.setProperty("showGroupSeparator", False)
        self.end_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.end_date.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.end_date.setCalendarPopup(True)
        self.end_date.setDate(QtCore.QDate(2023, 1, 1))
        self.end_date.setObjectName("end_date")
        self.gridLayout_3.addWidget(self.end_date, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 3, 3, 1, 1)
        self.radioBtn_today = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioBtn_today.setFont(font)
        self.radioBtn_today.setObjectName("radioBtn_today")
        self.gridLayout_3.addWidget(self.radioBtn_today, 1, 3, 1, 1)
        self.radioBtn_line = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.radioBtn_line.setFont(font)
        self.radioBtn_line.setObjectName("radioBtn_line")
        self.candle_or_line.addButton(self.radioBtn_line)
        self.gridLayout_3.addWidget(self.radioBtn_line, 2, 3, 1, 1)
        self.gridLayout_3.setRowStretch(0, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_MACD = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_MACD.setFont(font)
        self.checkBox_MACD.setObjectName("checkBox_MACD")
        self.verticalLayout_3.addWidget(self.checkBox_MACD)
        self.checkBox_RSI = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_RSI.setFont(font)
        self.checkBox_RSI.setObjectName("checkBox_RSI")
        self.verticalLayout_3.addWidget(self.checkBox_RSI)
        self.checkBox_ADX = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_ADX.setFont(font)
        self.checkBox_ADX.setObjectName("checkBox_ADX")
        self.verticalLayout_3.addWidget(self.checkBox_ADX)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_KD = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_KD.setFont(font)
        self.checkBox_KD.setObjectName("checkBox_KD")
        self.verticalLayout_2.addWidget(self.checkBox_KD)
        self.checkBox_ATR = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_ATR.setFont(font)
        self.checkBox_ATR.setObjectName("checkBox_ATR")
        self.verticalLayout_2.addWidget(self.checkBox_ATR)
        self.checkBox_volume = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.checkBox_volume.setFont(font)
        self.checkBox_volume.setObjectName("checkBox_volume")
        self.verticalLayout_2.addWidget(self.checkBox_volume)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_3 = QtWidgets.QFrame(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line_3.setFont(font)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_EMA = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_EMA.setFont(font)
        self.checkBox_EMA.setObjectName("checkBox_EMA")
        self.ma_or_bol = QtWidgets.QButtonGroup(StockChart)
        self.ma_or_bol.setObjectName("ma_or_bol")
        self.ma_or_bol.addButton(self.checkBox_EMA)
        self.horizontalLayout.addWidget(self.checkBox_EMA)
        self.checkBox_BBAND = QtWidgets.QCheckBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.checkBox_BBAND.setFont(font)
        self.checkBox_BBAND.setObjectName("checkBox_BBAND")
        self.ma_or_bol.addButton(self.checkBox_BBAND)
        self.horizontalLayout.addWidget(self.checkBox_BBAND)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 0, 1, 1)
        self.label_img = QtWidgets.QLabel(self.centralwidget)
        self.label_img.setGeometry(QtCore.QRect(500, 40, 718, 575))
        self.label_img.setText("")
        self.label_img.setObjectName("label_img")
        StockChart.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StockChart)
        self.statusbar.setObjectName("statusbar")
        StockChart.setStatusBar(self.statusbar)

        self.retranslateUi(StockChart)
        QtCore.QMetaObject.connectSlotsByName(StockChart)

    def retranslateUi(self, StockChart):
        _translate = QtCore.QCoreApplication.translate
        StockChart.setWindowTitle(_translate("StockChart", "MainWindow"))
        self.btn_confirm.setText(_translate("StockChart", "confirm"))
        self.radioBtn_tai.setText(_translate("StockChart", "台股"))
        self.radioBtn_usa.setText(_translate("StockChart", "美股"))
        self.label_end.setText(_translate("StockChart", "end"))
        self.label_start.setText(_translate("StockChart", "start"))
        self.radioBtn_candle.setText(_translate("StockChart", "candle"))
        self.radioBtn_today.setText(_translate("StockChart", "today"))
        self.radioBtn_line.setText(_translate("StockChart", "line"))
        self.label.setText(_translate("StockChart", "指標"))
        self.checkBox_MACD.setText(_translate("StockChart", "MACD"))
        self.checkBox_RSI.setText(_translate("StockChart", "RSI"))
        self.checkBox_ADX.setText(_translate("StockChart", "ADX"))
        self.checkBox_KD.setText(_translate("StockChart", "KD"))
        self.checkBox_ATR.setText(_translate("StockChart", "ATR"))
        self.checkBox_volume.setText(_translate("StockChart", "交易量"))
        self.checkBox_EMA.setText(_translate("StockChart", "EMA"))
        self.checkBox_BBAND.setText(_translate("StockChart", "Bollinger Band"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StockChart = QtWidgets.QMainWindow()
    ui = Ui_StockChart()
    ui.setupUi(StockChart)
    StockChart.show()
    sys.exit(app.exec_())
