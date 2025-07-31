from PySide6.QtWidgets import QWidget
from ui.dialog import ui_pm_count
from ui.ui_sub_Schedule import Ui_mdi_schedule 
from ui.dialog.ui_pm_count import Ui_Dialog
from dialog_pmcount import Open_PMCount

class SubScheduleForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mdi_schedule()
        self.ui.setupUi(self)  # Form은 self가 대신함
        

        print('손준석입니다.')
    def opencount(self):
        dlg = Open_PMCount(self)
        dlg.exec()