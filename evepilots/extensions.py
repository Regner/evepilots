

from flask.ext.celery import Celery
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.debugtoolbar import DebugToolbarExtension

from evelink.eve import EVE

db = SQLAlchemy()
celery = Celery()
migrate = Migrate()
debug_toolbar = DebugToolbarExtension()

evelink_eve = EVE()


def configure_extensions(app):
    """ Registers all relevant extensions. """

    db.init_app(app)
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)
    celery.init_app(app)
