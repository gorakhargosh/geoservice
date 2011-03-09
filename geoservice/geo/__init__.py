# -*- coding: utf-8 -*-

from pkg_resources import resource_filename

import pygeoip

geoip_dat = resource_filename(__name__, "GeoIP.dat")
geolite_city_dat = resource_filename(__name__, "GeoLiteCity.dat")

country = pygeoip.GeoIP(geoip_dat)
city = pygeoip.GeoIP(geolite_city_dat)
