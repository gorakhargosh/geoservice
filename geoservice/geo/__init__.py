# -*- coding: utf-8 -*-

from pkg_resources import resource_filename

import pygeoip

geoip_dat = resource_filename(__name__, "GeoIP.dat")
geolite_city_dat = resource_filename(__name__, "GeoLiteCity.dat")

geo_country = pygeoip.GeoIP(geoip_dat)
geo_city = pygeoip.GeoIP(geolite_city_dat)

