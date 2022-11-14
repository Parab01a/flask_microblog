# @Time: 2022/11/8 10:35
import logging

from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager
from flask_mail import Mail

from logging.handlers import RotatingFileHandler
import os

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

mail = Mail(app)
bootstrap = Bootstrap(app)

if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Microblog startup')

from app import routes, models, errors

# from app import routes 放在最后避免循环引用，这句代码相当于以下代码，会重复导入app导致报错
# from app import app
#
# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World!"
