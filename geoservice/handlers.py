# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

class IndexPageHandler(RequestHandler):
    def get(self):
        self.write("Hello, world.")

