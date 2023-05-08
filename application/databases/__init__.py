from application.models import init_model

class Database:
    instance = None

    def __init__(self):
        pass

    def init_app(self, instance):
        self.instance = instance
        init_model(instance)

database = Database()
