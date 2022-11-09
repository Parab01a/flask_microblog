# @Time: 2022/11/8 10:35
from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models

# from app import routes 放在最后避免循环引用，这句代码相当于以下代码，会重复导入app导致报错
# from app import app
#
# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World!"
