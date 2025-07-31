# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_SchedulenoEoKo.ui'
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
    QHBoxLayout, QPushButton, QSizePolicy, QWidget)

class Ui_mdi_schedule(object):
    def setupUi(self, mdi_schedule):
        if not mdi_schedule.objectName():
            mdi_schedule.setObjectName(u"mdi_schedule")
        mdi_schedule.resize(790, 569)
        self.gridLayout = QGridLayout(mdi_schedule)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(mdi_schedule)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.calendarWidget = QCalendarWidget(self.frame)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_2.addWidget(self.calendarWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(mdi_schedule)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_opencount = QPushButton(self.frame_2)
        self.btn_opencount.setObjectName(u"btn_opencount")
        self.btn_opencount.setGeometry(QRect(10, 10, 141, 24))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_opencount.sizePolicy().hasHeightForWidth())
        self.btn_opencount.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.frame_2)

        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 3)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(mdi_schedule)
        self.btn_opencount.clicked.connect(mdi_schedule.opencount)

        QMetaObject.connectSlotsByName(mdi_schedule)
    # setupUi

    def retranslateUi(self, mdi_schedule):
        mdi_schedule.setWindowTitle(QCoreApplication.translate("mdi_schedule", u"Form", None))
        self.btn_opencount.setText(QCoreApplication.translate("mdi_schedule", u"Open PM Count", None))
    # retranslateUi

