# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowvDsOQB.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSplitter,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 713)
        self.actionwefwefwef = QAction(MainWindow)
        self.actionwefwefwef.setObjectName(u"actionwefwefwef")
        self.mn_settings = QAction(MainWindow)
        self.mn_settings.setObjectName(u"mn_settings")
        self.actionOpen_FIle = QAction(MainWindow)
        self.actionOpen_FIle.setObjectName(u"actionOpen_FIle")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        self.tab_worklog = QWidget()
        self.tab_worklog.setObjectName(u"tab_worklog")
        self.gridLayout_3 = QGridLayout(self.tab_worklog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.worklog_splitter = QSplitter(self.tab_worklog)
        self.worklog_splitter.setObjectName(u"worklog_splitter")
        self.worklog_splitter.setFrameShape(QFrame.Shape.NoFrame)
        self.worklog_splitter.setFrameShadow(QFrame.Shadow.Plain)
        self.worklog_splitter.setLineWidth(0)
        self.worklog_splitter.setMidLineWidth(1)
        self.worklog_splitter.setOrientation(Qt.Orientation.Horizontal)
        self.worklog_splitter.setHandleWidth(3)
        self.verticalLayoutWidget = QWidget(self.worklog_splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.worklog_splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.worklog_splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.verticalLayoutWidget_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.worklog_splitter.addWidget(self.verticalLayoutWidget_2)

        self.gridLayout_3.addWidget(self.worklog_splitter, 0, 0, 1, 1)

        self.tab_widget.addTab(self.tab_worklog, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_widget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tab_widget.addTab(self.tab_3, "")

        self.gridLayout.addWidget(self.tab_widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuDB = QMenu(self.menubar)
        self.menuDB.setObjectName(u"menuDB")
        self.menuRecipe = QMenu(self.menubar)
        self.menuRecipe.setObjectName(u"menuRecipe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuDB.menuAction())
        self.menubar.addAction(self.menuRecipe.menuAction())
        self.menuFile.addAction(self.actionOpen_FIle)
        self.menuSettings.addAction(self.mn_settings)
        self.menuDB.addAction(self.actionwefwefwef)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionwefwefwef.setText(QCoreApplication.translate("MainWindow", u"wefwefwef", None))
        self.mn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionOpen_FIle.setText(QCoreApplication.translate("MainWindow", u"Open FIle", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_worklog), QCoreApplication.translate("MainWindow", u"\uc5c5\ubb34\uc77c\uc9c0", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\uc778\uc218\uc778\uacc4", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\uc124\ube44", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuDB.setTitle(QCoreApplication.translate("MainWindow", u"DB", None))
        self.menuRecipe.setTitle(QCoreApplication.translate("MainWindow", u"Recipes", None))
    # retranslateUi

