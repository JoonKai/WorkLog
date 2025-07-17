# sub_worklog_widget.py
from PySide6.QtWidgets import QWidget
from ui.ui_sub_worklog import Ui_Form  # 이게 당신이 올린 그 코드

class SubWorklogForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)  # Form은 self가 대신함

        print('손준석입니다.')