from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame, QSplitter, QListView, QHBoxLayout
from PySide6.QtCore import Qt

def setup_worklog_tab_ui(tab_widget):
    # 전체 탭 레이아웃
    layout = QVBoxLayout(tab_widget)

    # 1. 수평 splitter 생성
    splitter = QSplitter(Qt.Horizontal)
    
    # 2. 왼쪽 QWidget + VBoxLayout + ListView 3개
    left_widget = QWidget()
    left_layout = QVBoxLayout(left_widget)

    list_view1 = QListView()
    list_view2 = QListView()
    list_view3 = QListView()

    left_layout.addWidget(list_view1)
    left_layout.addWidget(list_view2)
    left_layout.addWidget(list_view3)

    splitter.addWidget(left_widget)

    # 3. 오른쪽 QWidget + VBoxLayout + Frame 2개
    right_widget = QWidget()
    right_layout = QVBoxLayout(right_widget)

    frame1 = QFrame()
    frame1.setFrameShape(QFrame.StyledPanel)

    frame2 = QFrame()
    frame2.setFrameShape(QFrame.StyledPanel)

    right_layout.addWidget(frame1)
    right_layout.addWidget(frame2)

    splitter.addWidget(right_widget)
    splitter.setSizes([100, 900])


    # splitter를 메인 레이아웃에 추가
    layout.addWidget(splitter)

    return list_view1, list_view2, list_view3, frame1, frame2