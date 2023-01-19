# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QWidget, QFileDialog
from uic.save import Ui_Form


class Save(QWidget, Ui_Form):
    def __init__(self, default_path):
        super().__init__()
        self.setupUi(self)
        self.text_input.setText(default_path)
        self.button_select.clicked.connect(self.slot_select_path)

    def slot_select_path(self):
        save_file_path = QFileDialog.getExistingDirectory(self, '请选择保存目录')
        if save_file_path:
            self.text_input.setText(save_file_path)

    def open(self):
        if self.isMinimized():
            self.showNormal()
        else:
            self.raise_()
        self.show()
