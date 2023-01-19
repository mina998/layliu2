# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QSizePolicy,
    QTableWidget, QTableWidgetItem, QToolBar, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 600)
        MainWindow.setMinimumSize(QSize(540, 600))
        MainWindow.setMaximumSize(QSize(540, 600))
        icon = QIcon()
        icon.addFile(u":/ico/images/qiezi.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(32, 32))
        self.mitmdump = QAction(MainWindow)
        self.mitmdump.setObjectName(u"mitmdump")
        self.pathselect = QAction(MainWindow)
        self.pathselect.setObjectName(u"pathselect")
        self.about = QAction(MainWindow)
        self.about.setObjectName(u"about")
        self.layout_root = QWidget(MainWindow)
        self.layout_root.setObjectName(u"layout_root")
        self.gridLayout = QGridLayout(self.layout_root)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table = QTableWidget(self.layout_root)
        if (self.table.columnCount() < 4):
            self.table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table.setObjectName(u"table")
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.setAutoScroll(True)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)

        self.layout_hm = QHBoxLayout()
        self.layout_hm.setObjectName(u"layout_hm")
        self.title_msg = QLabel(self.layout_root)
        self.title_msg.setObjectName(u"title_msg")
        self.title_msg.setMaximumSize(QSize(28, 16777215))

        self.layout_hm.addWidget(self.title_msg)

        self.label_statusbar_msg = QLabel(self.layout_root)
        self.label_statusbar_msg.setObjectName(u"label_statusbar_msg")

        self.layout_hm.addWidget(self.label_statusbar_msg)

        self.title_run = QLabel(self.layout_root)
        self.title_run.setObjectName(u"title_run")
        self.title_run.setMaximumSize(QSize(55, 1000))

        self.layout_hm.addWidget(self.title_run)

        self.label_statusbar_run = QLabel(self.layout_root)
        self.label_statusbar_run.setObjectName(u"label_statusbar_run")
        self.label_statusbar_run.setMaximumSize(QSize(30, 16777215))

        self.layout_hm.addWidget(self.label_statusbar_run)

        self.title_num = QLabel(self.layout_root)
        self.title_num.setObjectName(u"title_num")
        self.title_num.setMaximumSize(QSize(50, 16777215))

        self.layout_hm.addWidget(self.title_num)

        self.label_statusbar_num = QLabel(self.layout_root)
        self.label_statusbar_num.setObjectName(u"label_statusbar_num")
        self.label_statusbar_num.setMaximumSize(QSize(20, 16777215))
        self.label_statusbar_num.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.layout_hm.addWidget(self.label_statusbar_num)


        self.gridLayout.addLayout(self.layout_hm, 2, 0, 1, 1)

        self.title_tasks = QLabel(self.layout_root)
        self.title_tasks.setObjectName(u"title_tasks")
        font = QFont()
        font.setPointSize(9)
        self.title_tasks.setFont(font)
        self.title_tasks.setStyleSheet(u"#label_task_title{\n"
"	padding-:5px 0;\n"
"}")
        self.title_tasks.setMargin(0)

        self.gridLayout.addWidget(self.title_tasks, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.layout_root)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.pathselect)
        self.toolBar.addAction(self.mitmdump)
        self.toolBar.addAction(self.about)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u76f4\u64ad\u95f4\u62c9\u6d41\u5de5\u5177", None))
        self.mitmdump.setText(QCoreApplication.translate("MainWindow", u"\u6293\u5305\u5de5\u5177(&P)", None))
        self.pathselect.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u4fdd\u5b58(&S)", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None));
        self.title_msg.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001:", None))
        self.label_statusbar_msg.setText(QCoreApplication.translate("MainWindow", u"\u7b49\u4f8d\u4e2d", None))
        self.title_run.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5728\u4e0b\u8f7d:", None))
        self.label_statusbar_run.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.title_num.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u603b\u6570:", None))
        self.label_statusbar_num.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.title_tasks.setText(QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u5217\u8868:", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

