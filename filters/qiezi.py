# -*- coding: utf-8 -*-
import json
import re
from time import strftime

api = 'https://gw.szsbtech.com/app/video/watch'


class QieZi(object):

    def __init__(self, url, content):

        if url == api:
            self.body = re.sub(r'\\u\w{4}', '', content, re.I)
            self.url = url
            self.file_name = strftime('%Y%m%d%H%M%S')
            self.save()

    def user_get(self):
        # 作者名称
        user = re.search(r'"nickname":"([^"]+)"', self.body, re.I)
        user = user.group(1) if user else '其他人'
        return user

    def link_get(self):
        # 获取流链接
        link = re.search(r'rtmp://([^"]+)', self.body, re.I)
        link = link.group().replace(' ', '') if link else False
        return link

    def void_get(self, text):
        # 获取视频ID
        void = re.search(r'record/(.+?)\?', text, re.I)
        void = 'vid_' + void.group(1) if void else 'miss_' + self.file_name
        return void

    def save(self):

        link = self.link_get()
        if not link:
            return False

        void = self.void_get(link)

        text = dict(
            user=self.user_get(),
            link=link,
            void=void,
            file='{}.ts'.format(self.file_name)
        )

        text = json.dumps(text)
        with open('./temp/' + void, mode='w', encoding='gbk') as fb:
            fb.write(text)
