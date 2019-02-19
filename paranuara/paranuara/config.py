from aumbry import Attr, YamlConfig

class AppConfig(YamlConfig):
    __mapping__ = {
        'mongo': Attr('mongo', dict),
    }

    def __init__(self):
        self.mongo = {}
