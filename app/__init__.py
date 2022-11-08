# @Time: 2022/11/8 10:35
from flask import Flask

app = Flask(__name__)

from app import routes

# from app import routes 放在最后避免循环引用，这句代码相当于以下代码，会重复导入app导致报错
# from app import app
#
# @app.route('/')
# @app.route('/index')
# def index():
#     return "Hello, World!"
