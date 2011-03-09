# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from tornado.web import RequestHandler
from geoservice.serializers import json_encode
from geoservice import geo

class IndexPageHandler(RequestHandler):
    def get(self):
        self.write("Hello, world.")

class CountryIpAddressHandler(RequestHandler):
    def get(self, ip_address):
        try:
            country = geo.get_country_by_ip_address(ip_address)
            response = dict(status='OK', data=country)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))

class CountryHandler(RequestHandler):
    def get(self):
        try:
            ip_address = self.request.remote_ip
            country = geo.get_country_by_ip_address(ip_address)
            response = dict(status='OK', data=country)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))


class CountryDomainHandler(RequestHandler):
    def get(self, domain):
        try:
            country = geo.get_country_by_domain(domain)
            response = dict(status='OK', data=country)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))

class CityIpAddressHandler(RequestHandler):
    def get(self, ip_address):
        try:
            city = geo.get_city_by_ip_address(ip_address)
            response = dict(status='OK', data=city)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))

class CityHandler(RequestHandler):
    def get(self):
        try:
            ip_address = self.request.remote_ip
            city = geo.get_city_by_ip_address(ip_address)
            response = dict(status='OK', data=city)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))

class CityDomainHandler(RequestHandler):
    def get(self, domain):
        try:
            city = geo.get_city_by_domain(domain)
            response = dict(status='OK', data=city)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))

application = tornado.web.Application([
    (r'/', IndexPageHandler),
    (r'/country/?', CountryHandler),
    (r'/city/?', CityHandler),
    (r'/country/ip/([0-9\.]+)/?', CountryIpAddressHandler),
    (r'/country/domain/(.*)/?', CountryDomainHandler),
    (r'/city/ip/([0-9\.]+)/?', CityIpAddressHandler),
    (r'/city/domain/(.*)/?', CityDomainHandler),
])

def run_server(port, address, args):
    application.listen(port=port, address=address)
    tornado.ioloop.IOLoop.instance().start()
