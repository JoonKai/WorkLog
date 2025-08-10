# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget_DataVisualizezZXxut.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QSizePolicy, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_DataVisualize(object):
    def setupUi(self, DataVisualize):
        if not DataVisualize.objectName():
            DataVisualize.setObjectName(u"DataVisualize")
        DataVisualize.resize(771, 552)
        self.dockWidget = QDockWidget(DataVisualize)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setGeometry(QRect(9, 9, 415, 236))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_2 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeWidget = QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setObjectName(u"treeWidget")

        self.horizontalLayout.addWidget(self.treeWidget)

        self.frame = QFrame(self.dockWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 5)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.dockWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.dockWidget.setWidget(self.dockWidgetContents)
        self.dockWidget_2 = QDockWidget(DataVisualize)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidget_2.setGeometry(QRect(20, 250, 415, 236))
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.gridLayout_3 = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.treeWidget_2 = QTreeWidget(self.dockWidgetContents_2)
        self.treeWidget_2.setObjectName(u"treeWidget_2")

        self.horizontalLayout_2.addWidget(self.treeWidget_2)

        self.frame_2 = QFrame(self.dockWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 5)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.tabWidget_2 = QTabWidget(self.dockWidgetContents_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 1, 1, 1)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)

        self.retranslateUi(DataVisualize)

        QMetaObject.connectSlotsByName(DataVisualize)
    # setupUi

    def retranslateUi(self, DataVisualize):
        DataVisualize.setWindowTitle(QCoreApplication.translate("DataVisualize", u"Form", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("DataVisualize", u"1", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DataVisualize", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DataVisualize", u"Tab 2", None))
        ___qtreewidgetitem1 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem1.setText(8, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem1.setText(7, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem1.setText(6, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem1.setText(5, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("DataVisualize", u"\uc0c8 \ud589", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("DataVisualize", u"1", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("DataVisualize", u"Tab 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("DataVisualize", u"Tab 2", None))
    # retranslateUi

