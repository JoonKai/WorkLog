from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QLabel


class Open_Settings(QDialog):
    def __init__(self, parent=None):  # ✅ parent 인자를 받도록 수정
        super().__init__(parent)