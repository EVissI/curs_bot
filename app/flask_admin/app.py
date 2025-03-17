import asyncio
import flask
from flask import Flask, request, redirect, url_for, render_template
from app.config import setup_logger
logger = setup_logger("admin_panel")
from flask import Flask
from flask_admin import Admin,AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from app.db.database import sync_session
from app.db.models import Сurrency
from app.flask_admin.model_views import СurrencyView


app = Flask(__name__)

app.config['SECRET_KEY'] = 'AJKClasc6x5z1i2S3Kx3zcdo23'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


USERNAME = "admin"
LOGIN = "I7oiIE8CCUywrnv"
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == LOGIN:
            flask.session['logged_in'] = True
            return redirect('/admin')
        else:
            return render_template('login.html', error='Invalid credentials!')  # передаем ошибку в шаблон
    return render_template('login.html')  # Просто отображаем форму при GET запросе

@app.before_request
def check_login():
    if not flask.session.get('logged_in') and request.endpoint not in ['login', 'static']:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    flask.session.clear()  # Remove all data from the session
    return redirect(url_for('login'))

class MyAdminIndexView(AdminIndexView):
    form_base_class = SecureForm
    def is_visible(self):
        return False

admin = Admin(app, name='curs', template_mode='bootstrap4',index_view=MyAdminIndexView())


admin.add_view(СurrencyView(Сurrency, sync_session,name = 'Валюты'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2444)