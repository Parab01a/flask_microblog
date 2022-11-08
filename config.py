# @Time: 2022/11/8 21:14
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'  # os.environ os环境变量
