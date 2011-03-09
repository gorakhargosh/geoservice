#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 Yesudeep Mangalapilly <yesudeep@gmail.com>

import sys
import imp
import os.path

from setuptools import setup

version = imp.load_source('version',
                          os.path.join('geoservice', '__init__.py'))


def read_file(filename):
    """
    Reads the contents of a given file relative to the directory
    containing this file and returns it.

    :param filename:
        The file to open and read contents from.
    """
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


if sys.version_info < (3,):
    extra = {}
else:
    extra = dict(use_2to3=True)

install_requires = [
    'tornado >=1.2.1',
    'pygeoip >=0.1.5',
]
if sys.version_info < (2, 7, 0):
# argparse is merged into Python 2.7 in the Python 2x series
# and Python 3.2 in the Python 3x series.
    install_requires.append('argparse >=1.1')

setup(name="geoservice",
      version=version.__version_string__,
      description="Filesystem events monitoring",
      long_description=read_file('README'),
      author="Yesudeep Mangalapilly",
      author_email="yesudeep@gmail.com",
      license="MIT License",
      url="http://github.com/gorakhargosh/geoservice",
      keywords=' '.join([
                            'python',
                            'geolocation',
                            'geoip',
                            ]
                        ),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: C',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities',
          ],
      packages=['geoservice', 'geoservice.data'],
      include_package_data=True,
      install_requires=install_requires,
      entry_points={
          'console_scripts': [
              'geoservice = geoservice:main',
              ]
          },
      zip_safe=False,
      **extra
      )
