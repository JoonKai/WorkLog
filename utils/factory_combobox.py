from PySide6.QtWidgets import QComboBox

# ✅ 공용 함수: Enum을 받아 콤보박스 생성
def create_combo_from_enum(enum_class):
    combo = QComboBox()
    for item in enum_class:
        combo.addItem(item.name, item)
    return combo