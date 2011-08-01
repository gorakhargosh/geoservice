# Shared logger.

import logging

logger = logging.getLogger("geoservice")


def create_logger(name, level):
    logger = logging.getLogger(name)
    _set_up_logger(logger, level=level)


class NullLoggingHandler(logging.Handler):
    """
    Attach this handler to your logger to disable all logging.
    """
    def emit(self, record):
        pass


def _set_up_logger(logger, level='INFO'):
    """
    Sets up logging for pepe.

    :param logger:
        The logger object to update.
    :param level:
        Logging level specified at command line.
    :return:
        logging level ``int`` or None
    """
    LOGGING_LEVELS = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL,
        'NONE': None,
    }

    logging_level = LOGGING_LEVELS.get(level)
    if  logging_level is None:
        logging_handler = NullLoggingHandler()
    else:
        logger.setLevel(logging_level)
        logging_handler = logging.StreamHandler()
        logging_handler.setLevel(logging_level)
        logging_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s:%(name)s:%(levelname)s: %(message)s"
                )
            )

    logger.addHandler(logging_handler)
    return logging_level
