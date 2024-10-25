from flask import Flask
from flask_admin import Admin

from backend.models.engine import db_session
from backend.api.admin.view import *


async def admin_panel_init(app: Flask):  # initing admin_panel panel view
    admin = Admin(app, name='Admin', template_mode='bootstrap4', index_view=IndexView())
    async with db_session() as db:
        admin.add_view(BackView(name="Go back"))
