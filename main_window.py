import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMdiSubWindow
from PySide6.QtCore import Qt
from controller.widget_settings import OpenSettings
from ui.windows.ui_main_window import Ui_MainWindow
from controller.widget_schedule import SubScheduleForm
from controller.widget_webcontrol import WebControl
from controller.widget_datavisualize import OpenDataVisualize
import mariadb


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.resize(1000, 700)
        self.mn_settings.triggered.connect(self.open_settings_dialog)
        self.mn_Schedule.triggered.connect(self.open_mdi_Schedule)
        self.mn_webControl.triggered.connect(self.open_web_control)
        self.mn_datavisualize.triggered.connect(self.open_data_visualize)
        
    def open_settings_dialog(self):
        dlg = OpenSettings(self)
        dlg.exec()

    def open_mdi_Schedule(self):
        for sub in self.mdiArea.subWindowList():
            if isinstance(sub.widget(), SubScheduleForm):
                sub.activateWindow()
                self.mdiArea.setActiveSubWindow(sub)
                return  
        sub_widget = SubScheduleForm(self)
        sub = QMdiSubWindow()
        sub.setWidget(sub_widget)
        sub.setWindowTitle("PM 스케쥴")
        sub.resize(800, 600)
        sub.setAttribute(Qt.WA_DeleteOnClose, True)
        self.mdiArea.addSubWindow(sub)
        sub.show()

    def open_data_visualize(self):
        for sub in self.mdiArea.subWindowList():
            if isinstance(sub.widget(), OpenDataVisualize):
                sub.activateWindow()
                self.mdiArea.setActiveSubWindow(sub)
                return  
        sub_widget = OpenDataVisualize(self)
        sub = QMdiSubWindow()
        sub.setWidget(sub_widget)
        sub.setWindowTitle("데이터분석")
        sub.resize(800, 600)
        sub.setAttribute(Qt.WA_DeleteOnClose, True)
        self.mdiArea.addSubWindow(sub)
        sub.show()

    def open_web_control(self):
        for sub in self.mdiArea.subWindowList():
            if isinstance(sub.widget(), WebControl): 
                sub.activateWindow()
                self.mdiArea.setActiveSubWindow(sub)
                return  
        sub_widget = WebControl(self)
        sub = QMdiSubWindow()
        sub.setWidget(sub_widget)
        sub.setWindowTitle("웹컨트롤롤")
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