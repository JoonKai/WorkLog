from PySide6.QtWidgets import QMainWindow
from ui.ui_settings_window import Ui_SettingsWindow


class Open_Settings(QMainWindow, Ui_SettingsWindow):
    def __init__(self, parent=None):  # ✅ parent 인자를 받도록 수정
        super().__init__(parent)
        self.resize(1000, 600) 
        self.setWindowTitle("Settings")