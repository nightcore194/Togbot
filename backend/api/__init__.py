import logging
import os
import sys

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from backend.api.admin import admin_panel_init
from backend.models.engine import db_session
from backend.models.models import User
from backend.settings.settings import BACKEND_DIR, ENV_FILE


async def create_app():
    load_dotenv(ENV_FILE)
    config = os.environ
    app = Flask(__name__, template_folder=f'{BACKEND_DIR}/api/template', static_folder=f'{BACKEND_DIR}/api/static')
    # Secret key for session, mail settings
    app.config.from_mapping(
        SECRET_KEY=config['SECRET_KEY'],
        MAIL_DEFAULT_SENDER=config['MAIL_DEFAULT_SENDER'],
        MAIL_SERVER=config['MAIL_SERVER'],
        MAIL_PORT=config['MAIL_PORT'],
        MAIL_USE_TLS=False,
        MAIL_USE_SSL=True,
        MAIL_DEBUG=False,
        MAIL_USERNAME=config["MAIL_USERNAME"],
        MAIL_PASSWORD=config["MAIL_PASSWORD"],
    )

    # Register blueprints
    from backend.api.login import login_view
    from backend.api.voice import voice_view
    from backend.api.view import api_view
    app.register_blueprint(login_view)
    app.register_blueprint(voice_view)
    app.register_blueprint(api_view)

    # Setting up Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Setting up Flask-admin
    await admin_panel_init(app)

    # Setting up mail-server
    from backend.api.login import mail
    mail.init_app(app)

    @login_manager.user_loader
    async def load_user(user_id):
        async with db_session() as db:
            return await db.get(User, int(user_id))

    # Initializing logger
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    return app
