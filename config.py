import logging
import os
import time

from flask.logging import default_handler


class UTCFormatter(logging.Formatter):
    converter = time.gmtime

def get_logger():
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                '()': UTCFormatter,
                'format': '[%(asctime)s][%(levelname)s] %(name)s '
                          '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
                },
            },
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'console',
                'filename': 'debug.log',
                'maxBytes': 1000000,
                'backupCount': 3
                },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'console'
                },
            },
        'loggers': {
            '': {
                'handlers': ['file', 'console'],
                'level': 'DEBUG',
                'propagate': False,
                },
            'application': {
                'level': 'DEBUG',
                'propagate': True,
            },
        }
    }
    return LOGGING