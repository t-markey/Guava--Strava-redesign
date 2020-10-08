import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # this sets up email for errors
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['genericemail@gmail.com']
    POSTS_PER_PAGE = 5
    LANGUAGES = ['en', 'ko']
    # run ElASTICSEARCH_URL=http://localhost.9200  in terminal
    # Should be the next line...
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    #ElASTICSEARCH_URL = http://localhost.9200