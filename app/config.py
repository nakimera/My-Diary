class Config:
    SECRET_KEY = "TcQsWISFjRG4243XobHPIaDxMioisOba"
    DEBUG = False
    TESTING = False 
    DEVELOPMENT = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass
    
configuration = {
    "development" : DevelopmentConfig,
    "testing" : TestingConfig,
    "production" : ProductionConfig
}
