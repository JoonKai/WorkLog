from PySide6.QtWidgets import QWidget, QVBoxLayout
from ui.ui_sub_Schedule import Ui_mdi_schedule 
from widget_pmschedule import Open_PMSchedule
from PySide6.QtCore import Qt
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice

class SubScheduleForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mdi_schedule()
        self.ui.setupUi(self)  # Form은 self가 대신함
        
        # ✅ graphWidget 안에 파이차트 생성
        self.add_pie_chart()

    def add_pie_chart(self):
        # 데이터 준비
        data = [("PM", 30), ("Filter", 70)]
        total = sum([value for _, value in data])

        # ✅ 파이차트 시리즈 생성
        series = QPieSeries()
        slices = []

        # 각 조각에 퍼센트 값만 표기 (내부 표시)
        for legend_name, value in data:
            slice_item = series.append(legend_name, value)
            percent = (value / total) * 100
            slice_item.setLabel(f"{percent:.1f}%")  # 파이조각 내부는 퍼센트
            slice_item.setLabelVisible(True)
            slice_item.setLabelPosition(QPieSlice.LabelPosition.LabelInsideHorizontal)
            slices.append((slice_item, legend_name))

        # ✅ 차트 생성
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("PM&Filter 비율")
        chart.legend().setVisible(True)

        # ✅ 범례 이름 강제 변경
        markers = chart.legend().markers(series)
        for marker, (_, legend_name) in zip(markers, slices):
            marker.setLabel(legend_name)  # 범례는 원하는 이름 유지

        # ✅ 테마 적용 (다크 테마)
        chart.setTheme(QChart.ChartThemeDark)

        # ✅ 차트 뷰 생성
        chart_view = QChartView(chart)
        chart_view.setRenderHint(chart_view.renderHints())

        # ✅ graphWidget에 삽입
        layout = self.ui.graphWidget.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.graphWidget)
            self.ui.graphWidget.setLayout(layout)
        else:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()

        layout.addWidget(chart_view)

    def opencount(self):
        self.pm_win = Open_PMSchedule()
        self.pm_win.setWindowModality(Qt.WindowModality.ApplicationModal)  # 앱 전체 모달
        self.pm_win.show()