class Config:
    SECRET-KEY = " "
    DEBUG = False
    TESTING = False
    DEVELOPEMENT = False

    class DevelopmentConfig(Config):
        DEBUG = True
        DEVELOPEMENT = True

    class TestingConfig(Config):
        TESTING = True

    class ProductionConfig(Config):
        pass

    configuration = {
        "development" : DevelopmentConfig,
        "testing" : TestingConfig,
        "production" :ProductionConfig
    }
