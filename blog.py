from app import create_app, db
from app.models import User, Post
from flask_migrate import Migrate


app = create_app()
Migrate(app, db)

@app.shell_context_processor
def make_shell():
    return dict(db=db, User=User, Post=Post)

