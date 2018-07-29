class Config:
    SECRET_KEY = "TcQsWISFjRG4243XobHPIaDxMioisOba"
    DEBUG = False
    TESTING = False 
    DEVELOPMENT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Annemellisa1@localhost/mydiary'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Annemellisa1@localhost/mydiary_test'

class ProductionConfig(Config):
    DEBUG = False
    
app_config = {
    "development" : DevelopmentConfig,
    "testing" : TestingConfig,
    "production" : ProductionConfig
}
