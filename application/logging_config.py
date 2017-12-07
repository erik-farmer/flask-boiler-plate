from pathlib import Path

p = Path('.')
LOGS_DIR = p / 'application' / 'logs' / 'info.txt'

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOGS_DIR
        },
        # 'sentry': {
        #     'level': 'ERROR',
        #     'class': 'raven.handlers.logging.SentryHandler',
        #     'dsn': SENTRY_DSN,
        # },
    },
    'loggers': {
        'application': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        }
    }
}
