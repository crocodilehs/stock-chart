from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QPainter
import main
from UI import Ui_MainWindow


class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()  # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.radioBtn_today.clicked.connect(lambda: changeToday())
        self.ui.end_date.dateChanged.connect(lambda: cancelToday())
        self.ui.btn_confirm.clicked.connect(self.buttonClicked)

        def changeToday():
            self.ui.end_date.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui.radioBtn_today.setChecked(True)

        def cancelToday():
            self.ui.radioBtn_today.setChecked(False)


    def buttonClicked(self):
        target = self.ui.line_target.text()
        MACD_check = self.ui.checkBox_MACD.isChecked()
        RSI_check = self.ui.checkBox_RSI.isChecked()
        KD_check = self.ui.checkBox_KD.isChecked()
        BBAND_check = self.ui.checkBox_BBAND.isChecked()
        start_date = self.ui.start_date.date().toPyDate()
        end_date = self.ui.end_date.date().toPyDate()

        if self.ui.radioBtn_tai.isChecked():
            target = target+".TW"
        print(target)

        if self.ui.radioBtn_line.isChecked():
            type = "line"
        elif self.ui.radioBtn_candle:
            type = "candle"

        main.plotStock(target, type, MACD_check, RSI_check ,KD_check, BBAND_check, start_date, end_date)
        pixmap = QPixmap(f"{target}.jpg")
        self.ui.label_img.setPixmap(pixmap)
