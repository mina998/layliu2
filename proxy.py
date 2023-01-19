# -*- coding: utf-8 -*-
import os
import threading

from PySide6.QtWidgets import QWidget, QMessageBox
from winproxy import ProxySetting

from uic.proxy import Ui_Form


class Proxy(QWidget, Ui_Form):
    # 创建代理对象
    system_proxy = ProxySetting()
    # 本机代理IP
    proxy_ip = '127.0.0.1'
    # 默认代理端口
    proxy_port = 8080

    def __init__(self, run_path):
        super().__init__()
        self.setupUi(self)
        self.cmd_exe = run_path + '/cmd/proxy/mitmdump.exe'
        self.filters = run_path + '/filters/scripts.py'
        # 子线程开启MitmDump服务
        self.sub_thread = threading.Thread(daemon=True)
        # MitmDump服务按钮
        self.button_proxy_run.clicked.connect(self.mitmdump_run)
        self.button_proxy_stop.clicked.connect(self.server_stop)
        # 系统代理服务按钮
        self.button_system_run.clicked.connect(self.system_proxy_run)
        self.button_system_stop.clicked.connect(self.system_proxy_stop)

    def mitmdump_run(self):
        """开启子线程"""
        if self.sub_thread.is_alive() is False:
            self.sub_thread.run = self.server_run
            self.sub_thread.start()
            self.button_proxy_run.setEnabled(False)

    def server_run(self):
        """运行 MitmDump 程序"""
        # 获取代理服务端口
        self.proxy_port = self.port_proxy.value()
        # 启动Mitmweb服务进程命令
        cmd = '{} -p {} -s {} -q'.format(self.cmd_exe, self.proxy_port, self.filters)
        self.label_status_msg.setText('服务已启动')
        ret = os.system(cmd)
        if ret > 0:
            self.label_status_msg.setText('服务已停止')
            self.button_proxy_run.setEnabled(True)

    def server_stop(self):
        """结束MitmDump程序"""
        if self.sub_thread.is_alive():
            # 先杀死 MitmDump 服务进程 在停止子线程
            ret = os.system('taskkill /F /IM mitmdump.exe')
            if ret == 0:
                # 按钮设置为启用
                self.button_proxy_run.setEnabled(True)
                # 等侍线程结束
                self.sub_thread.join()
                # 重新开启线程
                self.sub_thread = threading.Thread()
            # 取消系统代理
            self.system_proxy_stop()

    def system_proxy_run(self):
        """启用系统代理服务"""
        # MitmDump服务已开启
        if self.sub_thread.is_alive():
            # 是否开启代理
            self.system_proxy.enable = True
            # 设置代理参数
            self.system_proxy.server = '{}:{}'.format(self.proxy_ip, self.proxy_port)
            # 写入注册信息
            self.system_proxy.registry_write()
            # 开启成功禁用按钮
            self.button_system_run.setEnabled(False)
        else:
            QMessageBox.information(self, '错误信息', '服务未启动')

    def system_proxy_stop(self):
        # 是否开启系统代理
        if self.system_proxy.enable:
            # 设置系统代理状态
            self.system_proxy.enable = False
            # 写入注册信息
            self.system_proxy.registry_write()
            # 启用按钮
            self.button_system_run.setEnabled(True)

    def open(self):
        """显示窗口"""
        if self.isMinimized():
            self.showNormal()
        else:
            self.raise_()
        self.show()
