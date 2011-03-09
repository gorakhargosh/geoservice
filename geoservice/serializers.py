# -*- coding: utf-8 -*-

from tornado.escape import \
    json_encode as _json_encode, \
    json_decode as _json_decode
from geoservice.jsmin_v8 import JavaScriptMinifier
from geoservice.jsmin import jsmin as minify

def minify_v8(value):
    minifier = JavaScriptMinifier()
    return minifier.JSMinify(value)

def json_encode(value, _minify=minify_v8):
    return _minify(_json_encode(value))

def json_decode(value):
    return _json_decode(value)
