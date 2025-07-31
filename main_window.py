import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMenuBar, QMenu, QVBoxLayout, QSplitter, QMdiSubWindow
from PySide6.QtCore import Qt
from settings_window import Open_Settings
from ui.ui_main_window import Ui_MainWindow
from sub_worklog_widget import SubWorklogForm
from sub_schedule_widget import SubScheduleForm
from layout.worklog_layout import setup_worklog_tab_ui
import mariadb


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.mn_settings.triggered.connect(self.open_settings_dialog)
        self.mn_Schedule.triggered.connect(self.open_mdi_Schedule)
        
    def open_settings_dialog(self):
        dlg = Open_Settings(self)
        dlg.exec()

    def open_mdi_Schedule(self):
        sub_widget = SubScheduleForm(self)
        sub = QMdiSubWindow()
        sub.setWidget(sub_widget)
        sub.setWindowTitle("PM 스케쥴쥴")
        sub.resize(500, 400)
        self.mdiArea.addSubWindow(sub)
        sub.show()
    


app = QApplication(sys.argv)
with open("./style/darkstyle.qss", "r", encoding="utf-8") as f:
    style = f.read()
    app.setStyleSheet(style)
window = MainWindow()
window.show()
app.exec_()