from application import db, app
from application.models import Users

def delete_database():
    with app.app_context():
        db.drop_all()

def create_database():
    with app.app_context():
        db.create_all()

def add_entries():
    entry1 = Users(username='admin', email='admin@admin.com', password='admin')
    entry2 = Users(username='test', email='test@test.com', password='test')
    with app.app_context():
        db.session.add(entry1)
        db.session.add(entry2)
        db.session.commit()

def see_db_entries():
    with app.app_context():
        entries = Users.query.all()
        for entry in entries:
            print(f"{entry.username}, {entry.email}, {entry.password}")

if __name__ == '__main__':
    delete_database()
    create_database()
    add_entries()
    see_db_entries()

