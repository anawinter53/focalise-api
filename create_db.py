from application import db, app

def create_database():
    with app.app_context():
        db.create_all()

def delete_database():
    with app.app_context():
        db.drop_all()

if __name__ == '__main__':
    delete_database()
    create_database()
    add_entries()
    see_db_entries()

