from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from werkzeug.contrib.cache import SimpleCache
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import filters


app = Flask(__name__)
app.register_blueprint(filters.blueprint)

app.config.from_object(Configuration)
db = SQLAlchemy(app)

cache = SimpleCache()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Admin
from app.models import CurrencyRate, Currency
admin = Admin(app)
admin.add_view(ModelView(CurrencyRate, db.session))
admin.add_view(ModelView(Currency, db.session))

from . import views
