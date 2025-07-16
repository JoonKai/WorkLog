import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMenuBar, QMenu
from ui_main_window import Ui_MainWindow
from layout.worklog_layout import setup_worklog_tab_ui
import mariadb


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)

        # 📌 업무일지 탭 구성 함수 호출
        self.list_view1, self.list_view2, self.list_view3, self.frame1, self.frame2 = setup_worklog_tab_ui(self.tab)
        


app = QApplication(sys.argv)
with open("./style/darkstyle.qss", "r", encoding="utf-8") as f:
    style = f.read()
    app.setStyleSheet(style)
window = MainWindow()
window.show()
app.exec_()