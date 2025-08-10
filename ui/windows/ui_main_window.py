# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowVLskaY.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMdiArea,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QWidget)

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
        self.mn_Schedule = QAction(MainWindow)
        self.mn_Schedule.setObjectName(u"mn_Schedule")
        self.mn_webControl = QAction(MainWindow)
        self.mn_webControl.setObjectName(u"mn_webControl")
        self.mn_datavisualize = QAction(MainWindow)
        self.mn_datavisualize.setObjectName(u"mn_datavisualize")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")

        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)

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
        self.menuWindows = QMenu(self.menubar)
        self.menuWindows.setObjectName(u"menuWindows")
        self.menu_3 = QMenu(self.menuWindows)
        self.menu_3.setObjectName(u"menu_3")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuDB.menuAction())
        self.menubar.addAction(self.menuRecipe.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menuFile.addAction(self.actionOpen_FIle)
        self.menuSettings.addAction(self.mn_settings)
        self.menuDB.addAction(self.actionwefwefwef)
        self.menuWindows.addAction(self.mn_Schedule)
        self.menuWindows.addAction(self.mn_webControl)
        self.menuWindows.addAction(self.menu_3.menuAction())
        self.menu_3.addAction(self.mn_datavisualize)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionwefwefwef.setText(QCoreApplication.translate("MainWindow", u"wefwefwef", None))
        self.mn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.actionOpen_FIle.setText(QCoreApplication.translate("MainWindow", u"Open FIle", None))
        self.mn_Schedule.setText(QCoreApplication.translate("MainWindow", u"PM&Filter \uc2a4\ucf00\uc974\ub7ec", None))
        self.mn_webControl.setText(QCoreApplication.translate("MainWindow", u"Parts \uad00\ub9ac", None))
        self.mn_datavisualize.setText(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130\ubd84\uc11d", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuDB.setTitle(QCoreApplication.translate("MainWindow", u"DB", None))
        self.menuRecipe.setTitle(QCoreApplication.translate("MainWindow", u"\uc81c\uc870", None))
        self.menuWindows.setTitle(QCoreApplication.translate("MainWindow", u"\uc124\ube44", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\uce21\uc815", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\uacf5\uc815", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\uae30\ud0c0", None))
    # retranslateUi

