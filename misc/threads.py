# -*- coding: utf-8 -*-
import os

from PySide6.QtCore import Signal, QThread
from PySide6.QtWidgets import QWidget

from misc import Util


class TableWidgetThread(QThread):
    table = Signal(dict)

    def __init__(self):
        super().__init__()
        self.status = False
        self.temp = './temp/'

    def run(self):
        """执行任务"""
        while not self.status:
            files = os.listdir(self.temp)
            for item in files:
                if self.status:
                    break
                content = Util.json_from_file(self.temp + item)
                if content:
                    self.table.emit(content)

                os.remove(self.temp + item)
                self.sleep(1)

    def stop(self):
        """停止任务"""
        self.status = True
        self.wait()


class VideoDownThread(QThread):
    task_run = Signal(int, str)
    task_row_table = Signal(QWidget, str)

    def __init__(self, cmd, vid, widget):
        super().__init__()
        self.vid = vid
        self.cmd = cmd
        self.widget = widget

    def run(self):
        # 1 任务开始
        self.task_run.emit(0, self.vid)
        # 执行命令
        ret = os.system(self.cmd)
        # 执行信息
        msg = '失败' if ret > 0 else '成功'
        # 发送信息
        self.task_row_table.emit(self.widget, msg)
        # 0 任务完成
        self.task_run.emit(1, self.vid)
