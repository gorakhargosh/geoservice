# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from tornado.web import RequestHandler

class IndexPageHandler(RequestHandler):
    def get(self):
        self.write("Hello, world.")


application = tornado.web.Application([
    (r'/', IndexPageHandler),
])

def run_server(port, address, args):
    application.listen(port=port, address=address)
    tornado.ioloop.IOLoop.instance().start()
