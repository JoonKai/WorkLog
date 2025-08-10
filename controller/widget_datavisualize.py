from PySide6.QtWidgets import QWidget
from ui.widget.ui_Widget_DataVisualize import Ui_DataVisualize


class OpenDataVisualize(QWidget):
    def __init__(self, parent=None):  # ✅ parent 인자를 받도록 수정
        super().__init__(parent)
        self.ui = Ui_DataVisualize()
        self.ui.setupUi(self)
        self.resize(600, 300) 
        self.setWindowTitle("데이터 분석")