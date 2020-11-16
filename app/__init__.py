from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.cache import SimpleCache
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

cache = SimpleCache()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


from . import views
