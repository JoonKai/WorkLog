from PySide6.QtWidgets import QDialog
from ui.widget.ui_Widget_Settings import Ui_Settings


class OpenSettings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)