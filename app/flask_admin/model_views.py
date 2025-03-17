from flask_admin.contrib.sqla import ModelView
import flask
from flask import redirect, url_for
from wtforms.fields import DateField
from flask_admin.form import DatePickerWidget
from datetime import datetime

class AuthModelView(ModelView):
    def is_accessible(self):
        return flask.session.get('logged_in')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))
    
class СurrencyView(AuthModelView):
    can_create = True
    can_delete = True
    edit_modal = True
    column_list = ['currency_name', 'currency_name_for_bot','value']
    column_searchable_list = ['currency_name']
    column_filters = ['value']
    column_editable_list = ['value','currency_name_for_bot']
    column_default_sort = 'currency_name'
    form_excluded_columns = ['created_at', 'updated_at']
    column_descriptions = {
        'currency_name': 'Название валюты',
        'currency_name_for_bot': 'Название валюты для бота',
        'value': 'Курс валюты'
    }

