# -*- coding: utf-8 -*-
import json
import os


class Util:

    @staticmethod
    def create_folder(path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def json_from_file(file):

        with open(file, 'r') as fb:
            text = fb.read()
        try:
            text = json.loads(text)
        except ValueError:
            text = {}
        return text
