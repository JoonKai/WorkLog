# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_ScheduleMNsENz.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QGridLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_mdi_schedule(object):
    def setupUi(self, mdi_schedule):
        if not mdi_schedule.objectName():
            mdi_schedule.setObjectName(u"mdi_schedule")
        mdi_schedule.resize(805, 592)
        self.gridLayout = QGridLayout(mdi_schedule)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_opencount = QPushButton(mdi_schedule)
        self.btn_opencount.setObjectName(u"btn_opencount")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_opencount.sizePolicy().hasHeightForWidth())
        self.btn_opencount.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.btn_opencount)

        self.pushButton = QPushButton(mdi_schedule)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.calendarWidget = QCalendarWidget(mdi_schedule)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.verticalLayout.addWidget(self.calendarWidget)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 20)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(mdi_schedule)
        self.btn_opencount.clicked.connect(mdi_schedule.opencount)

        QMetaObject.connectSlotsByName(mdi_schedule)
    # setupUi

    def retranslateUi(self, mdi_schedule):
        mdi_schedule.setWindowTitle(QCoreApplication.translate("mdi_schedule", u"Form", None))
        self.btn_opencount.setText(QCoreApplication.translate("mdi_schedule", u"Open PM Count", None))
        self.pushButton.setText(QCoreApplication.translate("mdi_schedule", u"\uc2a4\ucf00\uc974 \uc801\uc6a9", None))
    # retranslateUi

