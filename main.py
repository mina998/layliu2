# -*- coding: utf-8 -*-
import os
import sys
import time

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QPushButton, QHBoxLayout, QWidget

from misc import Util
from misc.threads import TableWidgetThread, VideoDownThread
from proxy import Proxy
from save import Save
from uic.main import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self):
        # 重载父类构造方法
        super().__init__()
        # 定义路径
        self.run_path = os.getcwd().replace('\\', '/')
        self.cmd_path = self.run_path + '/cmd'
        # 子窗口
        self.save = Save(self.run_path)
        self.mitm = Proxy(self.run_path)
        # 创建一个表格处理线程
        self.thr2 = TableWidgetThread()
        # 任务列表
        self.workers = dict()
        # 安装UI界面
        self.setupUi(self)
        # 显示UI界面
        self.show()
        # 初始化应用设置
        self.apply()

    def apply(self):
        # 创建所需要文件夹
        Util.create_folder(self.run_path + '/temp')
        # 显示其他窗口
        self.pathselect.triggered.connect(self.save.open)
        self.mitmdump.triggered.connect(self.mitm.open)
        # 表格设置
        self.table.setColumnWidth(0, 180)
        self.table.setColumnWidth(1, 140)
        self.table.setColumnWidth(2, 45)
        # 动态从文件加载表格内容
        self.thr2.table.connect(self.table_append_row)
        self.thr2.start()

    def closeEvent(self, event):
        """关闭子线程"""
        if self.workers.__len__() > 0:
            # 杀死 FFMpeg 程序
            cmd = 'taskkill /F /IM ffmpeg.exe'
            # 执行命令
            os.system(cmd)

        self.mitm.server_stop()
        self.mitm.destroy()
        self.thr2.stop()

    def button_table_row(self, row, col, **kwargs):
        """创建表格行按钮组"""
        btn1 = QPushButton('拉取')
        btn2 = QPushButton('删除')
        btn2.setObjectName('del')

        layout = QHBoxLayout()
        layout.setObjectName('lay')
        layout.setContentsMargins(5, 3, 5, 3)
        layout.addWidget(btn1)
        layout.addWidget(btn2)

        widget = QWidget()
        widget.setLayout(layout)
        self.table.setCellWidget(row, col, widget)

        btn1.clicked.connect(lambda: self.create_task(widget, **kwargs))
        btn2.clicked.connect(lambda: self.delete_table_row(widget))

    @Slot()
    def table_append_row(self, items):
        # 表格当前总行数
        row = self.table.rowCount()
        # 插入行
        self.table.insertRow(row)
        # 添加列内容
        self.table.setItem(row, 0, QTableWidgetItem(items['user']))
        self.table.setItem(row, 1, QTableWidgetItem(items['file']))
        self.table.setItem(row, 2, QTableWidgetItem('等侍'))
        self.table.item(row, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        # 添加按钮组
        self.button_table_row(row, 3, **items)
        # 更新任务栏表格行数
        self.label_statusbar_num.setText(str(row + 1))

    @Slot()
    def delete_table_row(self, widget):
        # 点击时获取控件位置才有效
        pos = widget.pos()
        # 获取表格行
        row = self.table.indexAt(pos).row()
        # 删除表格行
        self.table.removeRow(row)
        # 更新任务栏表格行数
        row = self.table.rowCount()
        self.label_statusbar_num.setText(str(row))

    @Slot()
    def create_task(self, widget, **kwargs):
        """创建任务"""
        # 是否获取链接成功
        if not kwargs.get('link'):
            self.label_statusbar_msg.setText('获取链接失败.')
            return False
        # 作务是否存在
        if self.workers.get(kwargs['void']):
            self.label_statusbar_msg.setText('任务已存在.')
            return False
        # 禁用按钮
        for i in widget.children():
            if i.isWidgetType():
                i.setEnabled(False)
        # 折包变量
        user, link, void, file = kwargs.values()
        # 生成文件保存路径
        save_path = '{}/{}/'.format(self.save.text_input.text(), user)
        # 创建文件夹
        Util.create_folder(save_path)
        # 生成执行命令
        cmd = '{}/ffmpeg.exe -i "{}" -c copy {}'.format(self.cmd_path, link, save_path + file)
        # 获取表格当前行
        row = self.table.indexAt(widget.pos()).row()
        # 设置表格行状态为开始
        self.table.item(row, 2).setText('开始')
        # 开始线程任务
        self.workers[void] = VideoDownThread(cmd, void, widget)
        self.workers[void].task_run.connect(self.statusbar_update_run)
        self.workers[void].task_row_table.connect(self.table_update_row)
        # 设置程序状态为运行中
        self.label_statusbar_msg.setText('运行中')
        # 启动任务
        self.workers[void].start()

    @Slot()
    def statusbar_update_run(self, ok, vid):
        """更新任务运行数"""
        time.sleep(1)
        if ok == 1:  # 删除已完成任务
            # 等侍线程结束
            self.workers[vid].wait()
            # 从任务列表删除
            del self.workers[vid]
        # 获取任务运行数
        num = self.workers.__len__()
        # 没有任务运行 设置程序状态为等侍中
        if num == 0:
            self.label_statusbar_msg.setText('等侍中')
        # 更新运行数
        self.label_statusbar_run.setText(str(num))

    @Slot()
    def table_update_row(self, widget: QWidget, msg):
        """更新表格行信息"""
        row = self.table.indexAt(widget.pos()).row()
        self.table.item(row, 2).setText(msg)
        button_del = self.table.cellWidget(row, 3).findChild(QPushButton, 'del')
        button_del.setEnabled(True)


if __name__ == '__main__':
    app2 = QApplication(sys.argv)
    main = Main()
    sys.exit(app2.exec())
