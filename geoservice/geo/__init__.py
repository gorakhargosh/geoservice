# -*- coding: utf-8 -*-

from pkg_resources import resource_filename
from geoservice.geo.countries import COUNTRY_NAME_ISO_ALPHA_2_TABLE

import pygeoip

# Load the MaxMind Databases.
geoip_dat = resource_filename(__name__, "GeoIP.dat")
geolite_city_dat = resource_filename(__name__, "GeoLiteCity.dat")

# API.
geoip_country = pygeoip.GeoIP(geoip_dat)
geoip_city = pygeoip.GeoIP(geolite_city_dat)


def _get_country_code_by_domain(domain):
    return geoip_country.country_code_by_name(domain)


def _get_country_code_by_ip_address(ip_address):
    return geoip_country.country_code_by_addr(ip_address)


def get_country_by_domain(domain):
    country_code = _get_country_code_by_domain(domain)
    country_name = COUNTRY_NAME_ISO_ALPHA_2_TABLE.get(country_code, country_code)

    return {'country_code': country_code, 'country_name': country_name}


def get_country_by_ip_address(ip_address):
    country_code = _get_country_code_by_ip_address(ip_address)
    country_name = COUNTRY_NAME_ISO_ALPHA_2_TABLE.get(country_code, country_code)

    return {'country_code': country_code, 'country_name': country_name}


def get_city_by_domain(domain):
    return geoip_city.record_by_name(domain)


def get_city_by_ip_address(ip_address):
    return geoip_city.record_by_addr(ip_address)
