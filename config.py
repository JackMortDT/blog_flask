class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:avatar65@localhost/Blog"
