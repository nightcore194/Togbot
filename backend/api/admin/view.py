from flask_admin import AdminIndexView, expose, BaseView
from flask_login import current_user
from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView


# TODO ADD ALL MODELS
class IndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('admin_view.login', next=request.url))
        return self.render('admin_panel/home.html')


class BackView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('admin_view.admin_views'))
