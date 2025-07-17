import sys
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QMenuBar, QMenu, QVBoxLayout
from ui.ui_main_window import Ui_MainWindow
from sub_worklog_widget import SubWorklogForm
from layout.worklog_layout import setup_worklog_tab_ui
import mariadb


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        # 업무일지 탭에 서브 폼 삽입
        self.load_worklog_form()

    def load_worklog_form(self):
        container = self.tab_worklog  # 디자이너에서 만든 탭 내부 위젯

        # 레이아웃이 없으면 생성
        if container.layout() is None:
            layout = QVBoxLayout(container)
            container.setLayout(layout)
        else:
            layout = container.layout()

        # 기존 위젯 정리
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        # 새로운 폼 넣기
        self.sub_form = SubWorklogForm()
        layout.addWidget(self.sub_form)


app = QApplication(sys.argv)
with open("./style/darkstyle.qss", "r", encoding="utf-8") as f:
    style = f.read()
    app.setStyleSheet(style)
window = MainWindow()
window.show()
app.exec_()