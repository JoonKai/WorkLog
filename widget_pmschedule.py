from PySide6.QtWidgets import QWidget, QComboBox, QHeaderView
from ui.dialog.ui_Widget_PMSchedule import Ui_Form

class Open_PMSchedule(QWidget):
    def __init__(self, parent=None):  # ✅ parent 인자를 받도록 수정
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.resize(1000, 600) 
        self.setWindowTitle("PM & Filter")
        self.ui.mocvdTable.setColumnCount(15)
        self.ui.mocvdTable.setHorizontalHeaderLabels([
            "위치", 
            "MOCVD", 
            "현황", 
            "장비명", 
            "MES \n Code", 
            "Chamber \n Count", 
            "Filter \n Count",
            "PM \n 주기",
            "Filter \n 주기",
            "Daily \n Run",
            "PM \n 예정 횟수",
            "Filter \n 예정 횟수",
            "PM \n 예상 날짜",
            "Filter \n 예상 날짜",
            "비고",
        ])
        self.ui.mocvdTable.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.mocvdTable.horizontalHeader().setFixedHeight(50)
        
        self.ui.mocvdTable.setColumnWidth(0,60)
        self.ui.mocvdTable.setColumnWidth(1,60)
        self.ui.mocvdTable.setColumnWidth(2,60)
        self.ui.mocvdTable.setColumnWidth(3,70)
        self.ui.mocvdTable.setColumnWidth(4,90)
        self.ui.mocvdTable.setColumnWidth(5,60)
        self.ui.mocvdTable.setColumnWidth(6,60)
        self.ui.mocvdTable.setColumnWidth(7,60)
        self.ui.mocvdTable.setColumnWidth(8,60)
        self.ui.mocvdTable.setColumnWidth(9,60)
        self.ui.mocvdTable.setColumnWidth(10,70)
        self.ui.mocvdTable.setColumnWidth(11,70)
        self.ui.mocvdTable.setColumnWidth(12,70)
        self.ui.mocvdTable.setColumnWidth(13,70)
        self.ui.mocvdTable.setColumnWidth(14,450)
        
    def addItem(self):
        """행 추가 및 첫 번째 열 콤보박스 자동 생성"""
        row_count = self.ui.mocvdTable.rowCount()
        self.ui.mocvdTable.insertRow(row_count)  # 새 행 추가

        # 첫 번째 열 콤보박스 생성
        combo = QComboBox()
        combo.addItems(["B1F", "B2F", "B3F", "B4F", "C3F", "D1F", "D2F"])
        self.ui.mocvdTable.setCellWidget(row_count, 0, combo)

    def savetable(self):
        print("손준석")