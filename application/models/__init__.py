def init_model(db_instance): 
     from application.models import User, UserSettings, Task, Sensory, Token, Message 
     db_instance.create_all()

