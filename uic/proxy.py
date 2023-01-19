# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'proxy.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)
import assets_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(220, 190)
        Form.setMinimumSize(QSize(220, 190))
        Form.setMaximumSize(QSize(220, 190))
        icon = QIcon()
        iconThemeName = u"face-kiss"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/ico/images/bug.png", QSize(), QIcon.Normal, QIcon.Off)
            icon.addFile(u":/icon/images/bug.png", QSize(), QIcon.Disabled, QIcon.On)

        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.port_proxy = QSpinBox(Form)
        self.port_proxy.setObjectName(u"port_proxy")
        self.port_proxy.setMaximumSize(QSize(1000, 28))
        self.port_proxy.setMinimum(2000)
        self.port_proxy.setMaximum(60000)
        self.port_proxy.setValue(8080)

        self.verticalLayout.addWidget(self.port_proxy)

        self.layout_midde = QHBoxLayout()
        self.layout_midde.setObjectName(u"layout_midde")
        self.layout_midde.setContentsMargins(-1, 8, -1, -1)
        self.layout_vertical_2 = QVBoxLayout()
        self.layout_vertical_2.setSpacing(6)
        self.layout_vertical_2.setObjectName(u"layout_vertical_2")
        self.button_proxy_run = QPushButton(Form)
        self.button_proxy_run.setObjectName(u"button_proxy_run")
        self.button_proxy_run.setMinimumSize(QSize(90, 30))
        self.button_proxy_run.setMaximumSize(QSize(90, 30))

        self.layout_vertical_2.addWidget(self.button_proxy_run)

        self.button_system_run = QPushButton(Form)
        self.button_system_run.setObjectName(u"button_system_run")
        self.button_system_run.setMinimumSize(QSize(90, 30))
        self.button_system_run.setMaximumSize(QSize(90, 30))

        self.layout_vertical_2.addWidget(self.button_system_run)


        self.layout_midde.addLayout(self.layout_vertical_2)

        self.horizontalSpacer = QSpacerItem(13, 65, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.layout_midde.addItem(self.horizontalSpacer)

        self.layout_vertical_1 = QVBoxLayout()
        self.layout_vertical_1.setSpacing(6)
        self.layout_vertical_1.setObjectName(u"layout_vertical_1")
        self.button_proxy_stop = QPushButton(Form)
        self.button_proxy_stop.setObjectName(u"button_proxy_stop")
        self.button_proxy_stop.setMinimumSize(QSize(90, 30))
        self.button_proxy_stop.setMaximumSize(QSize(80, 30))
        self.button_proxy_stop.setProperty("row_id", 888)

        self.layout_vertical_1.addWidget(self.button_proxy_stop)

        self.button_system_stop = QPushButton(Form)
        self.button_system_stop.setObjectName(u"button_system_stop")
        self.button_system_stop.setMinimumSize(QSize(90, 30))
        self.button_system_stop.setMaximumSize(QSize(80, 30))

        self.layout_vertical_1.addWidget(self.button_system_stop)


        self.layout_midde.addLayout(self.layout_vertical_1)


        self.verticalLayout.addLayout(self.layout_midde)

        self.layout_foot = QHBoxLayout()
        self.layout_foot.setSpacing(3)
        self.layout_foot.setObjectName(u"layout_foot")
        self.layout_foot.setContentsMargins(-1, 3, -1, -1)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 0))
        self.label.setMaximumSize(QSize(30, 26))

        self.layout_foot.addWidget(self.label)

        self.label_status_msg = QLabel(Form)
        self.label_status_msg.setObjectName(u"label_status_msg")

        self.layout_foot.addWidget(self.label_status_msg)


        self.verticalLayout.addLayout(self.layout_foot)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6293\u5305\u5de5\u5177", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6293\u5305\u4ee3\u7406\u670d\u52a1\u7aef\u53e3:", None))
        self.button_proxy_run.setText(QCoreApplication.translate("Form", u"\u542f\u52a8\u670d\u52a1", None))
        self.button_system_run.setText(QCoreApplication.translate("Form", u"\u5f00\u542f\u4ee3\u7406", None))
        self.button_proxy_stop.setText(QCoreApplication.translate("Form", u"\u505c\u6b62\u670d\u52a1", None))
        self.button_system_stop.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88\u4ee3\u7406", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u72b6\u6001:", None))
        self.label_status_msg.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u672a\u8fd0\u884c", None))
    # retranslateUi

