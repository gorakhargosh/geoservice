# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from geoservice.serializers import json_encode
from geoservice import geo
from geoservice.logger import logger


class BaseRequestHandler(tornado.web.RequestHandler):
    def get_remote_addr(self):
        ip_address = self.request.remote_ip
        if ip_address == '127.0.0.1':
            real_ip = self.request.headers.get('X-Real-Ip')
            if real_ip and real_ip != '127.0.0.1':
                ip_address = real_ip
        return ip_address


class IndexPageHandler(BaseRequestHandler):
    def get(self):
        self.write("Hello, world.")


class CountryIpAddressHandler(BaseRequestHandler):
    def get(self, ip_address):
        try:
            country = geo.get_country_by_ip_address(ip_address)
            response = dict(status='OK', data=country)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))


class CountryHandler(BaseRequestHandler):
    def get(self):
        try:
            ip_address = self.get_remote_addr()
            logger.info('Remote IP address is: %s' % ip_address)
            country = geo.get_country_by_ip_address(ip_address)
            response = dict(status='OK', data=country)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))


class CountryDomainHandler(BaseRequestHandler):
    def get(self, domain):
        try:
            country = geo.get_country_by_domain(domain)
            response = dict(status='OK', data=country)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))


class CityIpAddressHandler(BaseRequestHandler):
    def get(self, ip_address):
        try:
            city = geo.get_city_by_ip_address(ip_address)
            response = dict(status='OK', data=city)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))


class CityHandler(BaseRequestHandler):
    def get(self):
        try:
            ip_address = self.get_remote_addr()
            logger.info('Remote IP address is: %s' % ip_address)
            city = geo.get_city_by_ip_address(ip_address)
            response = dict(status='OK', data=city)
        except:
            response = dict(status='ERROR')
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(response))


class CityDomainHandler(BaseRequestHandler):
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
