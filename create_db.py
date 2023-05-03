from application import db, app
from application.models import Users, UserSettings, Tasks

def delete_database():
    with app.app_context():
        db.drop_all()

def create_database():
    with app.app_context():
        db.create_all()

def add_entries():
    Users1 = Users(username='admin', email='admin@admin.com', password='admin')
    Users2 = Users(username='test', email='test@test.com', password='test')
    Settings1 = UserSettings(user_id=1, colour_scheme=3, push_notifications=2, points=1000)
    Settings2 = UserSettings(user_id=2, colour_scheme=2, push_notifications=1, points=50)
    Tasks1 = Tasks(user_id=1, category_name='Python', task_name='Python testing', task_url='https://realpython.com/python-testing/', task_desc='Try and understand the concept of unit testing with Python')
    Tasks2 = Tasks(user_id=1, category_name='Django', task_name='Django intro', task_url='https://www.w3schools.com/django/django_intro.php', task_desc='Start on Django')
    Tasks3 = Tasks(user_id=1, category_name='Design', task_name='Design plans', task_url='None', task_desc='Find some designs for a portfolio website')

    with app.app_context():
        db.session.add(Users1)
        db.session.add(Users2)
        db.session.add(Settings1)
        db.session.add(Settings2)
        db.session.add(Tasks1)
        db.session.add(Tasks2)
        db.session.add(Tasks3)
        db.session.commit()

def see_db_entries():
    with app.app_context():
        users = Users.query.all()
        for user in users:
            print(f"{user.username}, {user.email}, {user.password}")
        settings = UserSettings.query.all()
        for setting in settings:
            print(f"{setting.colour_scheme}")
        tasks = Tasks.query.all()
        for task in tasks:
            print(f"{task.category_name}, {task.task_name}, {task.task_desc}")

if __name__ == '__main__':
    delete_database()
    create_database()
    add_entries()
    see_db_entries()

