from PySide6.QtWidgets import QWidget, QComboBox, QHeaderView, QTableWidgetItem,QAbstractItemView,QDateEdit, QFileDialog
from PySide6.QtGui import QColor, QKeySequence, QShortcut
from PySide6.QtCore import QDate
from ui.dialog.ui_Widget_PMSchedule import Ui_Form
from utils.factory_combobox import create_combo_from_enum
from enums.epienums import eSite, eManuType, eEquipmentModel
import json


COLUMN_ENUM_MAP = {
    0: eSite,
    2: eManuType,
    3: eEquipmentModel,
}
class Open_PMSchedule(QWidget):
    def __init__(self, parent=None):  # ✅ parent 인자를 받도록 수정
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.resize(1000, 600)
        self.setWindowTitle("PM & Filter")
        self.copied_row_data = None  # 내부 버퍼

        # Ctrl+C, Ctrl+V 단축키 등록
        QShortcut(QKeySequence("Ctrl+C"), self.ui.mocvdTable, self.copy_row)
        QShortcut(QKeySequence("Ctrl+V"), self.ui.mocvdTable, self.paste_row)


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
        self.ui.mocvdTable.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.mocvdTable.horizontalHeader().setFixedHeight(50)
        self.ui.mocvdTable.verticalHeader().setFixedWidth(50)
        self.ui.mocvdTable.setSelectionBehavior(QAbstractItemView.SelectItems)  # ✅ 셀 단위 선택

        # ✅ 열 너비 설정
        column_widths = [70, 70, 70, 70, 90, 70, 70, 70, 70, 70, 70, 70, 120, 120, 450]
        for i, width in enumerate(column_widths):
            self.ui.mocvdTable.setColumnWidth(i, width)

        # ✅ Qt Designer에서 시그널 연결되어 있음 (itemSelectionChanged → changecolor)
    def copy_row(self):
        """선택된 행 복사"""
        table = self.ui.mocvdTable
        selected_rows = sorted(set(idx.row() for idx in table.selectedIndexes()))
        if not selected_rows:
            return

        row = selected_rows[0]
        self.copied_row_data = []

        for col in range(table.columnCount()):
            cell_widget = table.cellWidget(row, col)
            if isinstance(cell_widget, QComboBox):
                self.copied_row_data.append(cell_widget.currentData())
            else:
                item = table.item(row, col)
                self.copied_row_data.append(item.text() if item else "")

    def paste_row(self):
        """선택된 행에 붙여넣기"""
        if not self.copied_row_data:
            return

        table = self.ui.mocvdTable
        selected_rows = sorted(set(idx.row() for idx in table.selectedIndexes()))
        if not selected_rows:
            return

        target_row = selected_rows[0]

        for col, value in enumerate(self.copied_row_data):
            if col in COLUMN_ENUM_MAP:
                combo = table.cellWidget(target_row, col)
                if combo is None:
                    combo = create_combo_from_enum(COLUMN_ENUM_MAP[col])
                    table.setCellWidget(target_row, col, combo)

                idx = combo.findData(value)
                if idx == -1:
                    # Enum 객체가 아닌 name/text인 경우 보정
                    idx = combo.findText(value.name if hasattr(value, "name") else str(value))
                if idx >= 0:
                    combo.setCurrentIndex(idx)
            else:
                item = table.item(target_row, col)
                if item is None:
                    item = QTableWidgetItem()
                    table.setItem(target_row, col, item)
                item.setText(value)
                
    def addItem(self):
        row_count = self.ui.mocvdTable.rowCount()
        self.ui.mocvdTable.insertRow(row_count)

        for col in range(self.ui.mocvdTable.columnCount()):
            if col in COLUMN_ENUM_MAP:
                self.ui.mocvdTable.setCellWidget(row_count, col, create_combo_from_enum(COLUMN_ENUM_MAP[col]))
            elif col in (12, 13):  # ✅ 8번 열에 날짜 위젯 추가
                date_edit = QDateEdit()
                date_edit.setCalendarPopup(True)  # 달력 팝업 활성화
                date_edit.setDate(QDate.currentDate())  # 기본값 = 오늘 날짜
                date_edit.setEnabled(False)
                self.ui.mocvdTable.setCellWidget(row_count, col, date_edit)
            else:
                self.ui.mocvdTable.setItem(row_count, col, QTableWidgetItem(""))
        
    def changecolor(self):
        """셀 선택 시 색상 변경"""
        table = self.ui.mocvdTable
        print("셀 선택 이벤트 발생")

        # ✅ 모든 셀 초기화
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    item.setBackground(QColor("#2b2b2b"))  # 기본 배경 다크

        # ✅ 선택된 셀 색상 변경
        for item in table.selectedItems():
            item.setBackground(QColor("#E36C74"))  # 선택 색상

        # ✅ 강제 화면 갱신
        table.viewport().update()

    def saveRecipe(self):
        """테이블 데이터를 JSON 파일로 저장"""
        # 1) 파일 저장 경로 선택
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "레시피 저장",
            "",
            "JSON Files (*.json);;All Files (*)"
        )

        if not file_path:
            return  # 사용자가 취소하면 종료
        
        self.ui.recipeTextbox.setText(file_path)
        table = self.ui.mocvdTable
        data = []

        # 2) 테이블 데이터 수집
        for row in range(table.rowCount()):
            row_data = {}
            for col in range(table.columnCount()):
                cell_widget = table.cellWidget(row, col)
                if isinstance(cell_widget, QComboBox):
                    row_data[col] = cell_widget.currentData().name if hasattr(cell_widget.currentData(), "name") else cell_widget.currentText()
                elif isinstance(cell_widget, QDateEdit):
                    row_data[col] = cell_widget.date().toString("yyyy-MM-dd")
                else:
                    item = table.item(row, col)
                    row_data[col] = item.text() if item else ""
            data.append(row_data)

        # 3) JSON으로 저장
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"레시피가 저장되었습니다: {file_path}")
        except Exception as e:
            print(f"저장 중 오류 발생: {e}")
    def openRecipe(self):
        print("손준석")