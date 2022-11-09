# @Time: 2022/11/8 10:41
from app import app
from flask import render_template, redirect, flash, url_for
from forms import LoginForm


# 2个路由
@app.route('/')
@app.route('/index')
# 1个视图函数
def index():
    user = {'username': 'Barney'}
    posts = [  # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # 如果点击提交，浏览器发送POST请求，form.validate_on_submit()收集数据并验证
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))  # 由登录界面跳转到应用程序界面
    return render_template('login.html', title='Sign In', form=form)
