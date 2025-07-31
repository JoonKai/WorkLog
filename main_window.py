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
        # Settings 메뉴 클릭 시 다이얼로그 띄우기
        self.mn_settings.triggered.connect(self.open_settings_dialog)
        self.mn_Schedule.triggered.connect(self.open_mdi_Schedule)
        
    def open_settings_dialog(self):
        dlg = Open_Settings(self)
        dlg.exec()  # modal

    def open_mdi_Schedule(self):
        # QWidget 기반 UI를 QMdiSubWindow로 감싸기
        sub_widget = SubScheduleForm(self)   # QWidget 기반 UI라 가정
        sub = QMdiSubWindow()
        sub.setWidget(sub_widget)
        sub.setWindowTitle("Schedule Window")
        sub.resize(500, 400)

        # mdi_area는 Ui_MainWindow에서 선언된 QMdiArea 위젯의 objectName과 같아야 함
        self.mdiArea.addSubWindow(sub)
        sub.show()
    


app = QApplication(sys.argv)
with open("./style/darkstyle.qss", "r", encoding="utf-8") as f:
    style = f.read()
    app.setStyleSheet(style)
window = MainWindow()
window.show()
app.exec_()