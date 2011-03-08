#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
IP Address to geolocation Web service.
"""

__version__ = (0, 0, 1)
__version_string__ = '.'.join(map(str, __version__))


from geoservice.logger import logger, set_up_logging


def parse_command_line():
    """
    Parses the command line and returns a ``Namespace`` object
    containing options and their values.

    :return:
        A ``Namespace`` object containing options and their values.
    """
    import argparse

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("-p",
                        "--port",
                        dest='port',
                        metavar='PORT',
                        default=8080,
                        type=int,
                        help='Port number to listen on.'
                        )
    parser.add_argument('-a',
                        '--address',
                        dest='address',
                        metavar='HOST',
                        type=str,
                        default='0.0.0.0',
                        help='The address on which to listen.')
    parser.add_argument('-q',
                        '--quiet',
                        dest='should_be_quiet',
                        action='store_true',
                        default=False,
                        help="Disables verbose logging")
    parser.add_argument('-L',
                        '--log-level',
                        '--logging-level',
                        dest='logging_level',
                        choices=[
                            'DEBUG',
                            'INFO',
                            'WARNING',
                            'ERROR',
                            'CRITICAL',
                            'NONE',
                            ],
                        default='INFO',
                        help="Logging level.")
    return parser.parse_args()


def main():
    """
    Entry-point function.
    """
    from geoservice.app import run_server

    args = parse_command_line()
    set_up_logging(logger, args.logging_level, args.should_be_quiet)
    run_server(port=args.port, address=args.address, args=args)
