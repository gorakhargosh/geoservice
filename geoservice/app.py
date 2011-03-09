# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from geoservice.handlers import IndexPageHandler


application = tornado.web.Application([
    (r'/', IndexPageHandler),
])

def run_server(port, address, args):
    application.listen(port=port, address=address)
    tornado.ioloop.IOLoop.instance().start()
