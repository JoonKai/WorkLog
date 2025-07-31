from PySide6.QtWidgets import QDialog
from ui.dialog.ui_pm_count import Ui_Dialog

class Open_PMCount(QDialog):
    def __init__(self, parent=None):  # ✅ parent 인자를 받도록 수정
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.resize(600, 300) 
        self.setWindowTitle("PM 카운트")

    def savetable(table_widget, finename):
