import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMdiSubWindow
from PySide6.QtCore import Qt
from controller.widget_settings import OpenSettings
from ui.windows.ui_main_window import Ui_MainWindow
from controller.widget_schedule import SubScheduleForm
from controller.widget_webcontrol import WebControl
import mariadb


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.mn_settings.triggered.connect(self.open_settings_dialog)
        self.mn_Schedule.triggered.connect(self.open_mdi_Schedule)
        self.mn_webControl.triggered.connect(self.open_web_control)
        
    def open_settings_dialog(self):
        dlg = OpenSettings(self)
        dlg.exec()

    def open_mdi_Schedule(self):
        # 이미 열려 있는지 확인
        for sub in self.mdiArea.subWindowList():
            if isinstance(sub.widget(), SubScheduleForm):  # 같은 타입인지 확인
                sub.activateWindow()
                self.mdiArea.setActiveSubWindow(sub)
                return  # 이미 있으므로 새로 안 띄움

        # 없으면 새로 열기
        sub_widget = SubScheduleForm(self)
        sub = QMdiSubWindow()
        sub.setWidget(sub_widget)
        sub.setWindowTitle("PM 스케쥴")
        # sub.resize(500, 400)
        sub.setAttribute(Qt.WA_DeleteOnClose, True)
        self.mdiArea.addSubWindow(sub)
        sub.show()

    def open_web_control(self):
        # 이미 열려 있는지 확인
        for sub in self.mdiArea.subWindowList():
            if isinstance(sub.widget(), WebControl):  # 같은 타입인지 확인
                sub.activateWindow()
                self.mdiArea.setActiveSubWindow(sub)
                return  # 이미 있으므로 새로 안 띄움

        # 없으면 새로 열기
        sub_widget = WebControl(self)
        sub = QMdiSubWindow()
        sub.setWidget(sub_widget)
        sub.setWindowTitle("PM 스케쥴")
        # sub.resize(500, 400)
        sub.setAttribute(Qt.WA_DeleteOnClose, True)
        self.mdiArea.addSubWindow(sub)
        sub.show()
    


app = QApplication(sys.argv)
with open("./style/darkstyle.qss", "r", encoding="utf-8") as f:
    style = f.read()
    app.setStyleSheet(style)
window = MainWindow()
window.show()
app.exec_()