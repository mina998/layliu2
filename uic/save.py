# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import assets_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 70)
        Form.setMinimumSize(QSize(450, 70))
        Form.setMaximumSize(QSize(450, 70))
        icon = QIcon()
        icon.addFile(u":/ico/images/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon/images/folder.png", QSize(), QIcon.Disabled, QIcon.On)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 8, 9, 8)
        self.text_input = QLineEdit(Form)
        self.text_input.setObjectName(u"text_input")
        self.text_input.setEnabled(False)
        self.text_input.setMinimumSize(QSize(0, 29))
        self.text_input.setMaximumSize(QSize(16777215, 29))
        self.text_input.setDragEnabled(False)
        self.text_input.setReadOnly(False)

        self.horizontalLayout.addWidget(self.text_input)

        self.button_select = QPushButton(Form)
        self.button_select.setObjectName(u"button_select")
        self.button_select.setMinimumSize(QSize(65, 30))
        self.button_select.setMaximumSize(QSize(60, 30))

        self.horizontalLayout.addWidget(self.button_select)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6587\u4ef6\u4fdd\u5b58\u8bbe\u7f6e", None))
        self.button_select.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8def\u5f84", None))
    # retranslateUi

