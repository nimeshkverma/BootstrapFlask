
from logging import ERROR, CRITICAL, Formatter
from logging.handlers import TimedRotatingFileHandler, SMTPHandler


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    SERVER_NAME = 'www.api.craftsvilla.com:8000'

    FILE_LOGGER_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    FILE_LOGGER_LOCATION = 'app.log'
    FILE_LOGGER_LEVEL = ERROR
    FILE_LOGGER_DURATION = 'D'
    FILE_LOGGER_BACKUP = 30
    FILE_LOGGER_FORMAT = '%(asctime)s %(levelname)s: %(message)s in %(pathname)s:%(funcName)s:%(lineno)d]'

    EMAIL_LOGGER_RECIPIENTS = ['nimesh.verma@craftsvilla.com']
    EMAIL_LOGGER_SERVER = 'www.api.craftsvilla.com:80'
    EMAIL_LOGGER_SENDER = 'error@craftsvilla.com'
    EMAIL_LOGGER_LEVEL = CRITICAL
    EMAIL_LOGGER_SUBJECT = 'Android App serving API failed!'
    EMAIL_LOGGER_FORMAT = '''
    Message type:       %(levelname)s
    Location:           %(pathname)s:%(lineno)d
    Module:             %(module)s
    Function:           %(funcName)s
    Time:               %(asctime)s

    Message:

    %(message)s
    '''


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):

    EMAIL_LOGGER_SERVER = '127.0.0.1:8000'
    SERVER_NAME = '127.0.0.1:8000'
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


def configure_and_run_server(app, environ_type='ProductionConfig'):
    app.config.from_object(environ_type)
    file_handler = TimedRotatingFileHandler(app.config.get('FILE_LOGGER_LOCATION'), when=app.config.get(
        'FILE_LOGGER_DURATION'), backupCount=app.config.get('FILE_LOGGER_BACKUP'))
    file_handler.setLevel(app.config.get('FILE_LOGGER_LEVEL'))
    file_handler.setFormatter(
        Formatter(app.config.get('FILE_LOGGER_FORMAT')))
    app.logger.addHandler(file_handler)

    if environ_type == 'ProductionConfig':
        email_handler = SMTPHandler(app.config.get('EMAIL_LOGGER_SERVER'), app.config.get(
            'EMAIL_LOGGER_SENDER'), app.config.get('EMAIL_LOGGER_RECIPIENTS'), app.config.get('EMAIL_LOGGER_SUBJECT'))
        email_handler.setLevel(app.config.get('EMAIL_LOGGER_LEVEL'))
        email_handler.setFormatter(
            Formatter(app.config.get('EMAIL_LOGGER_FORMAT')))
        app.logger.addHandler(email_handler)
    app.run()
