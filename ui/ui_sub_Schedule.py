# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_ScheduleydmGGI.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
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
        self.calendarWidget = QCalendarWidget(mdi_schedule)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.horizontalLayout_2.addWidget(self.calendarWidget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget = QTableWidget(mdi_schedule)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 31):
            self.tableWidget.setRowCount(31)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(31)

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.frame = QFrame(mdi_schedule)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.graphWidget = QWidget(self.frame)
        self.graphWidget.setObjectName(u"graphWidget")

        self.gridLayout_2.addWidget(self.graphWidget, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.frame)

        self.verticalLayout_4.setStretch(0, 5)
        self.verticalLayout_4.setStretch(1, 5)

        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2.setStretch(0, 7)
        self.horizontalLayout_2.setStretch(1, 3)

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
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("mdi_schedule", u"PM", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("mdi_schedule", u"Filter", None));
    # retranslateUi

