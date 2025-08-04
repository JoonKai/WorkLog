from PySide6.QtWidgets import QWidget, QVBoxLayout, QSplitter, QTableWidget
from PySide6.QtCore import Qt
from PySide6.QtCharts import QChart, QChartView, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, QAbstractBarSeries
from ui.ui_sub_Schedule import Ui_mdi_schedule
from widget_pmschedule import Open_PMSchedule

class SubScheduleForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mdi_schedule()
        self.ui.setupUi(self)
        self.ui.pmfilterTable.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.ScheduleSplitter.setSizes([700,300])


        # 막대그래프 생성
        self.create_bar_chart()
        
    def create_bar_chart(self):
        
        # 샘플 데이터
        pm_data = [5,3]
        filter_data = [5,6]
        categories = ["Total"]

        # PM 시리즈
        bar_set_pm = QBarSet("PM")
        bar_set_pm.append(pm_data)

        # Filter 시리즈
        bar_set_filter = QBarSet("Filter")
        bar_set_filter.append(filter_data)

        # BarSeries 추가
        series = QBarSeries()
        series.append(bar_set_pm)
        series.append(bar_set_filter)

        # ✅ 막대 안에 숫자 표시
        series.setLabelsVisible(True)
        series.setLabelsPosition(QAbstractBarSeries.LabelsInsideEnd)  # 또는 LabelsOutsideEnd

        # 차트 생성
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("PM && Filter 건수")
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTheme(QChart.ChartThemeDark)

        # X축 카테고리
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        # Y축 값
        axisY = QValueAxis()
        axisY.setRange(0, max(pm_data + filter_data) + 2)
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        # 범례
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        # 차트뷰 생성
        chart_view = QChartView(chart)
        chart_view.setRenderHint(chart_view.renderHints())

        # 기존 graphWidget 레이아웃에 삽입
        layout = QVBoxLayout(self.ui.graphWidget)
        layout.addWidget(chart_view)
        self.ui.graphWidget.setLayout(layout)

    def opencount(self):
        self.pm_win = Open_PMSchedule()
        self.pm_win.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.pm_win.show()
