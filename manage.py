from flask_script import Manager

from flaskr.server import app, db
from flaskr.server.models import Category, Post

manager = Manager(app)


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all()
    print(333333333333)

@manager.command
def create_tables():
    print(555555555555555555)
    py = Category('Python')
    p = Post('Hello Python!', 'Python is pretty cool', py)
    db.session.add(py)
    db.session.add(p)
    db.session.commit()


if __name__ == "__main__":
    manager.run()