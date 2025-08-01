from PySide6.QtWidgets import QWidget
from ui.dialog.ui_Widget_PMSchedule import Ui_Form

class Open_PMSchedule(QWidget):
    def __init__(self, parent=None):  # ✅ parent 인자를 받도록 수정
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.resize(600, 300) 
        self.setWindowTitle("PM 카운트")

    def savetable(self):
        print("손준석")