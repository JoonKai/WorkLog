# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_ScheduleJGlBBC.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QGridLayout, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSplitter,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_mdi_schedule(object):
    def setupUi(self, mdi_schedule):
        if not mdi_schedule.objectName():
            mdi_schedule.setObjectName(u"mdi_schedule")
        mdi_schedule.resize(805, 592)
        self.gridLayout = QGridLayout(mdi_schedule)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_opencount = QPushButton(mdi_schedule)
        self.btn_opencount.setObjectName(u"btn_opencount")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_opencount.sizePolicy().hasHeightForWidth())
        self.btn_opencount.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.btn_opencount)

        self.pushButton = QPushButton(mdi_schedule)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ScheduleSplitter = QSplitter(mdi_schedule)
        self.ScheduleSplitter.setObjectName(u"ScheduleSplitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ScheduleSplitter.sizePolicy().hasHeightForWidth())
        self.ScheduleSplitter.setSizePolicy(sizePolicy1)
        self.ScheduleSplitter.setOrientation(Qt.Orientation.Horizontal)
        self.ScheduleSplitter.setHandleWidth(3)
        self.verticalLayoutWidget = QWidget(self.ScheduleSplitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.calendarWidget = QCalendarWidget(self.verticalLayoutWidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy1.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy1)
        self.calendarWidget.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.calendarWidget.setGridVisible(True)

        self.verticalLayout_2.addWidget(self.calendarWidget)

        self.ScheduleSplitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.ScheduleSplitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.pmfilterTable = QTableWidget(self.verticalLayoutWidget_2)
        if (self.pmfilterTable.columnCount() < 2):
            self.pmfilterTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.pmfilterTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pmfilterTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.pmfilterTable.rowCount() < 31):
            self.pmfilterTable.setRowCount(31)
        self.pmfilterTable.setObjectName(u"pmfilterTable")
        font = QFont()
        font.setPointSize(6)
        font.setUnderline(True)
        self.pmfilterTable.setFont(font)
        self.pmfilterTable.setLineWidth(1)
        self.pmfilterTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.pmfilterTable.setRowCount(31)

        self.verticalLayout_3.addWidget(self.pmfilterTable)

        self.graphWidget = QWidget(self.verticalLayoutWidget_2)
        self.graphWidget.setObjectName(u"graphWidget")

        self.verticalLayout_3.addWidget(self.graphWidget)

        self.verticalLayout_3.setStretch(0, 5)
        self.verticalLayout_3.setStretch(1, 5)
        self.ScheduleSplitter.addWidget(self.verticalLayoutWidget_2)

        self.verticalLayout_4.addWidget(self.ScheduleSplitter)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(mdi_schedule)
        self.btn_opencount.clicked.connect(mdi_schedule.opencount)

        QMetaObject.connectSlotsByName(mdi_schedule)
    # setupUi

    def retranslateUi(self, mdi_schedule):
        mdi_schedule.setWindowTitle(QCoreApplication.translate("mdi_schedule", u"Form", None))
        self.btn_opencount.setText(QCoreApplication.translate("mdi_schedule", u"Open PM Count", None))
        self.pushButton.setText(QCoreApplication.translate("mdi_schedule", u"\uc2a4\ucf00\uc974 \uc801\uc6a9", None))
        ___qtablewidgetitem = self.pmfilterTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mdi_schedule", u"PM", None));
        ___qtablewidgetitem1 = self.pmfilterTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mdi_schedule", u"Filter", None));
    # retranslateUi

